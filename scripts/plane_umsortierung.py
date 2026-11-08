#!/usr/bin/env python3
"""Create a separate, approximate A-Z shelving plan without changing the inventory."""
import argparse
import collections
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path


def alphabet(text):
    text = text.casefold().replace('ß', 'ss').replace('ø', 'o').replace('æ', 'ae')
    text = ''.join(c for c in unicodedata.normalize('NFKD', text)
                   if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', text).strip()


def first_surname(row):
    name = re.split(r'\s*/\s*|\s+und\s+|\s*&\s*', row['autor_nachname'])[0]
    # German filing convention for the three particles present in this inventory.
    return re.sub(r'^(von|du|le)\s+', '', name, flags=re.I)


def sort_key(row):
    surname = first_surname(row)
    given = re.split(r'\s*/\s*|\s+und\s+|\s*&\s*', row['autor_vorname'])[0]
    return (not bool(surname.strip()), alphabet(surname), alphabet(given),
            alphabet(row['titel']), row['buch_id'])


def display_author(row):
    last, first = row['autor_nachname'].strip(), row['autor_vorname'].strip()
    if not last:
        return 'Ohne Autorenangabe'
    names = re.split(r'\s*/\s*|\s+und\s+', last)
    given = re.split(r'\s*/\s*|\s+und\s+', first)
    if len(names) > 1 and len(names) == len(given):
        return ' / '.join((f + ' ' + l).strip() for f, l in zip(given, names))
    if len(names) == 1 and len(given) > 1:
        return ' / '.join((f + ' ' + last).strip() for f in given)
    return (first + ' ' + last).strip()


def mdcell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def run(inventory, estimate, output):
    raw = inventory.read_bytes()
    config = json.loads(estimate.read_text())
    assert hashlib.sha256(raw).hexdigest() == config['inventory_sha256'], 'Inventarstand geaendert: Schaetzung neu pruefen.'
    with inventory.open(newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter=';'))
    assert len(rows) == 1048 and len({r['buch_id'] for r in rows}) == len(rows)
    books = sorted((r for r in rows if r['identifikationsstatus'] == 'lesbar'), key=sort_key)
    assert len(books) == 1022
    physical = collections.Counter(r['standort'] for r in rows if r['identifikationsstatus'] != 'kein_buch')
    widths = {}
    for shelf, info in config['source_shelves'].items():
        assert physical[shelf] == info['physical_rows']
        assert 0 < info['book_fill_fraction'] <= 1
        col = shelf.split('-')[0]
        widths[shelf] = config['column_widths'][col] * info['book_fill_fraction'] / physical[shelf]
    assert all(r['standort'] in widths for r in books)
    shelves = [f'{col}-{level}' for col in range(1, 9) for level in range(1, 9)]
    allocations = []
    groups = collections.defaultdict(list)
    used_width = collections.defaultdict(float)
    index = 0
    for book in books:
        width = widths[book['standort']]
        while index < len(shelves):
            target = shelves[index]
            capacity = config['column_widths'][target.split('-')[0]]
            new_count = len(groups[target]) + 1
            new_width = used_width[target] + width
            reserve = config['reserve_books'] * new_width / new_count
            if new_width + reserve <= capacity + 1e-10:
                break
            index += 1
        assert index < len(shelves), 'Nicht genug geschaetzter Regalplatz.'
        position = len(groups[target]) + 1
        item = {'ID': book['buch_id'], 'Autor': display_author(book), 'Titel': book['titel'],
                'Regal': book['standort'], 'Position': int(book['position_im_fach']),
                'Nach Regal': target, 'Nach Position': position}
        allocations.append(item)
        groups[target].append(item)
        used_width[target] += width
    assert len(allocations) == len(books)
    assert {a['ID'] for a in allocations} == {b['buch_id'] for b in books}
    assert len({(a['Nach Regal'], a['Nach Position']) for a in allocations}) == len(books)
    assert [a['ID'] for a in allocations] == [b['buch_id'] for b in books]
    source_by_id = {r['buch_id']: r for r in rows}
    for a in allocations:
        source = source_by_id[a['ID']]
        assert (a['Regal'], a['Position']) == (source['standort'], int(source['position_im_fach']))
    for shelf, group in groups.items():
        assert [a['Nach Position'] for a in group] == list(range(1, len(group) + 1))
        cap = config['column_widths'][shelf.split('-')[0]]
        assert cap - used_width[shelf] >= config['reserve_books'] * used_width[shelf] / len(group) - 1e-10
    output.mkdir(parents=True, exist_ok=True)
    headers = ['ID', 'Autor', 'Titel', 'Regal', 'Position', 'Nach Regal', 'Nach Position']
    with (output / 'umraeumliste.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=headers, delimiter=';')
        writer.writeheader()
        writer.writerows(allocations)
    lines = ['# Umräumliste nach Autoren-Nachnamen', '',
             'Stand: 08.11.2026 · **1.022 erkannte Bücher** · Zielpositionen sind ein grober Breitenplan.', '',
             '**Regal / Position** sind die ursprünglichen Standorte. **Nach Regal / Nach Position** sind die geplanten Standorte. Positionen zählen von links nach rechts ab 1.', '',
             'Fachfolge: 1-1 bis 1-8, dann 2-1 bis 2-8 usw. In jedem belegten Fach sind rechnerisch mindestens 2,5 durchschnittliche Buchrücken als Reserve vorgesehen. Die letzte belegte Ablage darf mehr frei lassen.', '',
             'Breiten sind aus der sichtbaren Füllung der Herkunftsfächer geschätzt, keine Messungen einzelner Bücher. Die Lampe in 1-4 und andere Gegenstände in Zielfächern vorher entfernen. Die elf offenen Einträge sind nicht umgeplant.', '',
             'Ein erkanntes Lesebuch ohne Autorenangabe steht am Schluss. Mehrfachautoren werden unter dem ersten genannten Nachnamen eingeordnet; bei Gleichstand Vorname und Titel. Ä/Ö/Ü wie A/O/U, ß wie ss. Namensvorsätze von/du/le werden für die Ablage übergangen.', '',
             '[CSV herunterladen](umraeumliste.csv) · [Belegung je Fach](regalbelegung.md) · [Methode](../../docs/umsortierung_2026-11-08.md)', '']
    for shelf in shelves:
        if not groups[shelf]:
            continue
        lines += [f'## Nach Regal {shelf}', '', '| ' + ' | '.join(headers) + ' |',
                  '|---|---|---|---|---:|---|---:|']
        lines += ['| ' + ' | '.join(mdcell(a[h]) for h in headers) + ' |' for a in groups[shelf]]
        lines.append('')
    (output / 'umraeumliste.md').write_text('\n'.join(lines) + '\n')
    overview = ['# Geplante Regalbelegung', '',
                'Breiten in relativen Facheinheiten. Nur grobe Schätzung aus den vorhandenen Fotos; keine Zentimeterangaben.', '',
                '| Nach Regal | Bücher | Autoren von – bis | Belegung geschätzt | Freie durchschnittliche Buchbreiten | Hinweis |',
                '|---|---:|---|---:|---:|---|']
    shelf_rows = []
    for shelf in shelves:
        group = groups[shelf]
        cap = config['column_widths'][shelf.split('-')[0]]
        ratio = used_width[shelf] / cap
        reserve = (cap - used_width[shelf]) / (used_width[shelf] / len(group)) if group else None
        note = 'Lampe vorher entfernen' if shelf == '1-4' and group else ''
        if not group:
            note = 'Kein erkanntes Buch zugewiesen'
        names = f"{group[0]['Autor']} – {group[-1]['Autor']}" if group else '–'
        free = f'{reserve:.1f}' if reserve is not None else 'leer geplant'
        overview.append(f'| {shelf} | {len(group)} | {mdcell(names)} | {ratio:.0%} | {free} | {note} |')
        shelf_rows.append({'regal': shelf, 'buecher': len(group), 'belegung_anteil': round(ratio, 4),
                           'freie_buchbreiten': round(reserve, 2) if reserve is not None else None})
    (output / 'regalbelegung.md').write_text('\n'.join(overview) + '\n')
    summary = {'stand': config['stand'], 'source_ref': config['source_ref'],
               'inventory_sha256': config['inventory_sha256'], 'erkannte_buecher': len(books),
               'offen_ausgeschlossen': sum(r['identifikationsstatus'] not in ('lesbar', 'kein_buch') for r in rows),
               'kein_buch_ausgeschlossen': sum(r['identifikationsstatus'] == 'kein_buch' for r in rows),
               'belegte_faecher': len(groups), 'erstes_zielfach': allocations[0]['Nach Regal'],
               'letztes_zielfach': allocations[-1]['Nach Regal'], 'faecher': shelf_rows,
               'pruefung': 'Alle erkannten IDs genau einmal, Quellpositionen erhalten, Zielpositionen eindeutig und fortlaufend, Reserve in jedem belegten Fach mindestens 2,5 geschaetzte mittlere Buchbreiten.'}
    (output / 'pruefung.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    # Verify the exported table, not only the in-memory objects.
    with (output / 'umraeumliste.csv').open(encoding='utf-8-sig', newline='') as stream:
        saved = list(csv.DictReader(stream, delimiter=';'))
    assert len(saved) == len(books) and {r['ID'] for r in saved} == set(source_by_id) - {r['buch_id'] for r in rows if r['identifikationsstatus'] != 'lesbar'}
    assert sum(line.startswith('| B') for line in (output / 'umraeumliste.md').read_text().splitlines()) == len(books)
    assert inventory.read_bytes() == raw
    print(json.dumps({k: summary[k] for k in summary if k != 'faecher'}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventar', type=Path, default=Path('daten/buecher.csv'))
    parser.add_argument('--schaetzung', type=Path, default=Path('daten/umsortierung/breitenschaetzung.json'))
    parser.add_argument('--ausgabe', type=Path, default=Path('daten/umsortierung'))
    args = parser.parse_args()
    run(args.inventar, args.schaetzung, args.ausgabe)
