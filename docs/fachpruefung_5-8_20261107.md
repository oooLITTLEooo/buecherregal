# Gezielte Nachprüfung Fach 5-8 – 07.11.2026

## Verbindliche Git-Bildgrundlage

- Unverändertes Original: `bilder/originale/PXL_20261105_151533806.jpg` (`FOTO0037`, 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Byteidentische, nach Standort benannte Kopie: `bilder/umbenannt/Regal_5-8.jpg`.
- Alle vier im Git bereits enthaltenen nativen Bildteile `daten/bildanalyse/fullres/FOTO0037_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` **einzeln** betrachtet; die für B00711 relevanten Teile 01/02 und die für B00718 und B00719 relevanten Teile 03/04 gezielt bewertet.
- **Ausschließlich die drei zuvor unsicheren Buch-IDs B00711, B00718 und B00719 inhaltlich aktualisiert.** Die 17 weiteren als lesbar eingestuften Einträge nicht erneut inventarisiert; keine Änderung an Originalen, Positionen, Buch-IDs oder Fotoreferenzen.

## Einzelfallentscheidungen

| Buch-ID | Vorläufige Position | Befund am Git-Original | Entscheidung |
| --- | ---: | --- | --- |
| **B00711** | 5 | Im Übergang der Teile 01/02 zwischen Thomas Mann *Die Erzählungen* und Donna Leon *Das goldene Ei* ist am teilweise verdeckten hellen Band **Colleen McCullough** zu erkennen; das Titelwort ist nicht vollständig sichtbar. Ein bestimmtes Buch von McCullough wäre geraten. | **offen**; kein Titel ergänzt |
| **B00718** | 12 | FOTO0037 Teil 03: breiter cremefarbener Band mit **James A. Michener – Die Kinder von Torremolinos**. Buchrücken mit Schrift und Autor gut erkennbar; die Zeilentrennung des Titels ändert dessen Schreibweise nicht. | **lesbar** (zuvor `pruefen`) |
| **B00719** | 13 | FOTO0037 Teil 03: schmaler petrol-/türkisgrüner Suhrkamp-Band zeigt **Miller – Du sollst nicht merken** und die **st-Reihennummer 952**. Suhrkamp nennt zu dieser Reihennummer ausdrücklich **Alice Miller**. Bisheriger Vorname **Arthur** war falsch; der benachbarte Band *Arthur Miller – Hexenjagd* ist ein separates Buch. | **lesbar**, Autorin **Alice Miller** (vorher `pruefen`) |

### Bibliografische Nachweise

- **B00718:** [Google Books – James Albert Michener, Die Kinder von Torremolinos (Goldmann)](https://books.google.com/books/about/Die_Kinder_von_Torremolinos.html?id=645gAAAACAAJ). Das unterstützt die auf dem Rücken lesbare Werkzuordnung; Jahr oder ISBN dieses individuellen Exemplars sind **nicht** aus Katalogdaten übertragen worden.
- **B00719:** [Suhrkamp Verlag – Alice Miller, Du sollst nicht merken, suhrkamp taschenbuch 952](https://www.suhrkamp.de/buch/alice-miller-du-sollst-nicht-merken-t-9783518374528) und [offizielle Werkseite von Alice Miller](https://www.alice-miller.com/de/du-sollst-nicht-merken-3/). Die direkt sichtbare Nummer `st 952` ist ein belastbarer Verlagsbeleg zur Autorenkorrektur. Keine konkrete Auflage des abgebildeten Exemplars abgeleitet.
- **B00711:** Keine belastbare Werktitelidentifikation, daher kein bibliografischer Titelersatz.

## Genau benötigtes Nachfoto

**Nur B00711**: Den teilweise verdeckten Band mit *Colleen McCullough* **zwischen Thomas Mann *Die Erzählungen* und Donna Leon *Das goldene Ei*** kurz herausziehen und von vorn den **vollständigen Rücken** fotografieren; zusätzlich ein **Titelblattfoto** machen. Die beiden Nachbarbände zur Positionssicherung im Überblick mit aufnehmen. Bis dahin keine mutmaßliche Titelergänzung.

## Git-Nachführung

- `daten/buecher.csv`: nur B00711 (Bemerkung), B00718 (`lesbar`, Bildnachweis) und B00719 (`lesbar`, Autorenkorrektur Arthur → Alice, Nachweis) verändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: genau diese drei Fallentscheidungen dokumentiert; B00711 bleibt `bleibt_unsicher_nach_hochaufloesungspruefung`.
- `daten/pruefplan_faecher.csv`: Fach 5-8 nun `neues_detailfoto_bei_bedarf`, zweite Sichtprüfung `ja`, 20 vorläufige Einträge = 19 lesbar, 0 prüfen, 1 offen, unsichere ID B00711.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: Status und nächster Arbeitsschritt synchronisiert.
- Alle Originalbilder, Positionskopien, andere Buchdatensätze, IDs, Fach-/Positionsnummern und `foto_referenz` unverändert.

## Bilanz und Halt

- **Fach 5-8:** 20 vorläufige Bucheinträge, davon **19 lesbar, 0 prüfen, 1 offen**. Nicht abgehakt – für B00711 wird ein neues Titelblatt-/Rückenfoto benötigt.
- **Gesamt:** 1048 vorläufige Bucheinträge, **997 lesbar, 14 prüfen, 37 offen** = **51 unsicher**.
- **20** fotografierte Fächer vorläufig abgehakt; **3** weitere Fächer in dieser gezielten Prüfrunde noch ausständig, **27** nachgeprüfte Fächer mit Restunsicherheiten; Fach 3-3 zusätzlich mit gesondertem Zähl-/Positionsabgleich.
- **Nächstes Fach erst bei neuem „Weiter“: 6-1**, ausschließlich B00727 und B00748.
