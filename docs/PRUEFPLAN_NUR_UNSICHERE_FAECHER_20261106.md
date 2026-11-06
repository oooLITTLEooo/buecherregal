# Gezielte Nachprüfung nur unsicherer Regalfächer (Stand 2026-11-06)

## Beschluss und Regeln

Ab sofort **ausschließlich Bücher prüfen, deren `identifikationsstatus` in `daten/buecher.csv` `pruefen` oder `offen` ist**, sowie gesonderte Unklarheiten bei Anzahl oder physischer Zuordnung. Kein erneutes vollständiges Lesen sicher erfasster Fächer. **Genau ein Fach pro Benutzeraufforderung `Weiter`**, anschließend Bericht und überprüfter Git-Commit. Die 51 bisher vorhandenen Fachfotos bleiben unverändert. Nie Titel erraten.

Dies ist ein Arbeitsplan aus der **momentanen Git-Inventarliste**, keine neue Bildprüfung der hier vorläufig abgehakten Fächer. `lesbar` kann im ersten Inventurdurchgang gesetzt worden sein; ein vorläufiges Abhaken ist deshalb **keine unabhängige zweite Sichtprüfung**. Bei später entdeckten Widersprüchen, Zählfehlern oder neuen Detailfotos wird ein Fach erneut geöffnet.

Maschinenlesbare vollständige Übersicht: `daten/pruefplan_faecher.csv`. Nach jeder weiteren gezielten Fachprüfung muss auch dieser Arbeitsplan bei veränderten Unsicherheiten aktualisiert werden; **`daten/buecher.csv` bleibt maßgeblich**.

## Zusammenfassung

- Raster: **64** Fachpositionen, davon **51** mit Foto und vorhandenen Bucheinträgen.
- **12** fotografierte Fächer mit `0` offenen/prüfpflichtigen Bucheinträgen → **vorläufig abhaken**.
- **39** fotografierte Fächer mit zusammen **99** `pruefen`/`offen`-Einträgen.
- Von diesen 39 sind **31** noch nicht in der neuen fachweisen Nachkontrolle behandelt worden → als nächstes **gezielt nur die unsicheren Bücher prüfen**.
- **8** weitere wurden bereits mit allen vier Fotoausschnitten erneut geprüft, bleiben aber ungeklärt → erneute identische Bildprüfung ohne neuen Hinweis vermeiden; bei Bedarf neues Detailfoto.
- Daneben **13 Positionen ohne Fachdetailfoto**: 3 mit Foto- oder Sichtbedarf, 6 mit unklarer/leer wirkender Belegung, 4 laut Übersicht leer oder mit Lampe.
- Global: **1048** vorläufige Exemplare, davon **949 lesbar, 59 prüfen, 40 offen**. Fotos, Buch-IDs und positionsbezogene Originalreferenzen werden nicht geändert.

## Vorläufig abgehakt — 12 Fächer

- `1-5` — zweite Sichtprüfung durchgeführt
- `1-6` — zweite Sichtprüfung durchgeführt
- `1-7` — gezielte Nachprüfung B00034 erfolgreich, siehe `docs/fachpruefung_1-7_20261106.md`
- `1-8` — gezielte Nachprüfung B00055 erfolgreich, siehe `docs/fachpruefung_1-8_20261106.md`
- `3-8` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `4-1` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `4-4` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `6-3` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `6-5` — zweite Sichtprüfung durchgeführt
- `6-7` — zweite Sichtprüfung durchgeführt
- `7-2` — zweite Sichtprüfung durchgeführt
- `7-4` — zweite Sichtprüfung durchgeführt

## Noch gezielt prüfen — 31 Fächer

Reihenfolge folgt der Regalnummerierung. Nur die betroffenen IDs öffnen und einen passenden Bildausschnitt lesen; klar lesbare Bücher nicht erneut bearbeiten.

| Fach | Unsichere Bücher | IDs |
| --- | ---: | --- |
| 2-2 | 1 | `B00094` |
| 2-3 | 4 | `B00107`, `B00117`, `B00123`, `B00125` |
| 2-4 | 2 | `B00131`, `B00149` |
| 2-5 | 2 | `B00155`, `B00161` |
| 2-6 | 1 | `B00170` |
| 2-7 | 3 | `B00185`, `B00188`, `B00198` |
| 2-8 | 1 | `B00226` |
| 3-1 | 8 | `B00232`, `B00235`, `B00240`, `B00241`, `B00247`, `B00249`, `B00257`, `B00258` |
| 3-2 | 1 | `B00277` |
| 3-3 | 2 | `B00292`, `B00300` |
| 3-4 | 1 | `B00318` |
| 3-5 | 4 | `B00329`, `B00330`, `B00332`, `B00333` |
| 3-6 | 2 | `B00340`, `B00360` |
| 3-7 | 1 | `B00373` |
| 4-2 | 2 | `B00418`, `B00433` |
| 4-3 | 2 | `B00448`, `B00454` |
| 4-5 | 3 | `B00474`, `B00475`, `B00486` |
| 4-6 | 1 | `B00492` |
| 4-7 | 6 | `B00516`, `B00518`, `B00526`, `B00528`, `B00535`, `B00540` |
| 4-8 | 2 | `B00545`, `B00558` |
| 5-1 | 4 | `B00560`, `B00563`, `B00575`, `B00579` |
| 5-2 | 2 | `B00585`, `B00599` |
| 5-3 | 5 | `B00600`, `B00604`, `B00614`, `B00615`, `B00619` |
| 5-4 | 3 | `B00627`, `B00631`, `B00642` |
| 5-5 | 2 | `B00645`, `B00647` |
| 5-6 | 6 | `B00668`, `B00671`, `B00673`, `B00680`, `B00686`, `B00688` |
| 5-7 | 2 | `B00701`, `B00706` |
| 5-8 | 3 | `B00711`, `B00718`, `B00719` |
| 6-1 | 2 | `B00727`, `B00748` |
| 6-2 | 1 | `B00767` |
| 6-4 | 2 | `B00804`, `B00811` |

**Nächstes Fach:** `2-2`, nur **B00094**.

## Bereits erneut geprüft, aber weiterhin ungeklärt — 8 Fächer

Diese Fächer sind **nicht** abgehakt. Ohne neue Fotodetails oder einen anderen konkret vielversprechenden Bildansatz nicht erneut dieselben Ausschnitte verarbeiten:

| Fach | Offen/Prüfen | IDs | Fachbericht |
| --- | ---: | --- | --- |
| 2-1 | 3 | `B00061`, `B00071`, `B00078` | `docs/fachpruefung_2-1_20261106.md` |
| 6-6 | 3 | `B00848`, `B00860`, `B00869` | `docs/fachpruefung_6-6_20261106.md` |
| 6-8 | 1 | `B00896` | `docs/fachpruefung_6-8_20261106.md` |
| 7-1 | 1 | `B00916` | `docs/fachpruefung_7-1_20261106.md` |
| 7-3 | 3 | `B00953`, `B00954`, `B00957` | `docs/fachpruefung_7-3_20261106.md` |
| 7-5 | 3 | `B01001`, `B01007`, `B01008` | `docs/fachpruefung_7-5_20261106.md` |
| 7-6 | 3 | `B01017`, `B01030`, `B01031` | `docs/fachpruefung_7-6_20261106.md` |
| 7-7 | 1 | `B01035` | `docs/fachpruefung_7-7_20261106.md` |

## Fächer ohne eigene Detailbilder

- `7-8`: durch Gegenstand verdeckt, Belegung unklar — zusätzliches Foto/Einblick.
- `8-1`, `8-2`: Bücher laut Gesamtansicht vorhanden — Detailbilder erforderlich.
- `8-3` bis `8-8`: laut Gesamtbild leer/unklar — tatsächliche Belegung bestätigen.
- `1-1` bis `1-3`: laut Gesamtbild leer. `1-4`: Lampe.

## Aktualisierung nach jeder Fachprüfung

1. Nur ein Fach und dessen unsichere Buch-IDs anhand der vorhandenen Originalpixel prüfen.
2. `daten/buecher.csv` und `daten/bildanalyse/feinpruefung_unsicher.csv` nur bei belegbaren Korrekturen ändern; Besonderheiten in einem Fachprüfbericht nachweisen.
3. Den vorhandenen Fotostatus in `daten/fachstatus.csv` erhalten; keine vorgetäuschte Gewissheit.
4. `daten/pruefplan_faecher.csv` synchronisieren, sobald ein Unsicherheitsstatus wechselt.
5. Nach Commit die CSV-Strukturen, Anzahl, IDs und die Änderung im Git verifizieren. Dann STOP und Ergebnis berichten.
