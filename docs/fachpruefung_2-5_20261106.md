# Gezielte Nachprüfung Fach 2-5 – 06.11.2026

## Bildgrundlage und Umfang

- Original im Git: `bilder/originale/PXL_20261105_151120024.jpg` (FOTO0010, 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Aus den im Git versionierten Originalpixel-Ausschnitten `daten/bildanalyse/fullres/FOTO0010_teil_02.jpg.base64.txt` und `FOTO0010_teil_03.jpg.base64.txt` gezielt nur die beiden unsicheren Bände B00155 und B00161 nachgelesen.
- Kein neues Foto und keine Buch-IDs, Fachpositionen oder Originalfotodateien verändert. Bereits als lesbar markierte Einträge nicht systematisch zweitgeprüft.

## Ergebnis

| Buch-ID | Pos. | Beobachtung | Neuer Status |
| --- | ---: | --- | --- |
| **B00155** | 6 | Weißer Goldmann-Rücken zeigt klar `Helen Fielding` und `Bridget Jones` (FOTO0010 Teil 02), direkt nach Joy Fielding *Bevor der Abend kommt*. Kein zusätzlicher Untertitel auf dieser Ansicht gesichert. | **lesbar** |
| **B00161** | 12 | Schmaler dunkelblauer Heyne-Rücken zwischen John Grisham *Die Schuld* und Elizabeth George *Vergiss nie, dass ich dich liebe* zeigt `MARY HIGGINS CLARK` und `DASS DU EWIG DENKST AN MICH` (FOTO0010 Teil 03). Eindeutig ein eigener Band. | **lesbar** |

## Git-Nachführung

- In `daten/buecher.csv`: B00155 auf lesbar; B00161 vollständiger Autor Mary Higgins Clark und Status lesbar. Übrige Bücher unangetastet.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Nachprüfbelege aktualisiert.
- `daten/pruefplan_faecher.csv`: Fach 2-5 mit 17 lesbar, 0 prüfen, 0 offen vorläufig abgehakt.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: Status synchronisiert.

## Zählstand

- Fach 2-5: **17** vorläufige Exemplare, **17 lesbar**, keine unklaren.
- Gesamt: **1048** vorläufige Bucheinträge: **955 lesbar**, **53 prüfen**, **40 offen** (= 93 unsicher).
- **13** Fächer vorläufig abgehakt; **27** noch gezielt zu überprüfen; 11 trotz Nachprüfung noch mit Unsicherheiten.
- **Nächstes Fach erst nach „Weiter“:** `2-6`, ausschließlich B00170.
