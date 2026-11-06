# Gezielte Nachprüfung Fach 2-7 – 06.11.2026

## Umfang

- **Einzige Bildquelle im Git:** `bilder/originale/PXL_20261105_151131380.jpg` (Foto-ID `FOTO0012`, 8160 × 4590 Pixel nach `daten/fotos.csv`).
- Geprüft: die drei vorhandenen nativen Pixelbereiche `daten/bildanalyse/fullres/FOTO0012_teil_01.jpg.base64.txt`, `_teil_02.jpg.base64.txt` und `_teil_03.jpg.base64.txt`.
- Nur die drei bisher unsicheren Buchdatensätze **B00185, B00188, B00198** nachgeprüft, alle übrigen 26 bereits als `lesbar` markierten Buchdatensätze unverändert.

## Ergebnisse

| ID | Pos. | Lesung und Belege | Ergebnis |
| --- | ---: | --- | --- |
| B00185 | 2 | Zwischen Per Olov Enquist *Der Besuch des Leibarztes* und Petra Hammesfahr *Seine große Liebe*. FOTO0012 Teil 01 zeigt auf einem schmalen Rücken *Die Liebe ist doch sehr überschätzt* und den Namen *Giraud*. Bibliografisch eindeutig **Brigitte Giraud**, *Die Liebe ist doch sehr überschätzt*. | **lesbar** |
| B00188 | 5 | Zwischen Elke Heidenreich *Kolonien der Liebe* und *Der Welt den Rücken*. FOTO0012 Teil 01 zeigt auf schmalem Rücken *Petra Hammesfahr* und *BILD Bestseller-Bibliothek 6*. Bibliografisch ist Band 6 dieser Reihe **Das Geheimnis der Puppe** von Petra Hammesfahr. Die Titellesung ist über diese eindeutig zugeordnete Reihennummer gesichert. | **lesbar** |
| B00198 | 15 | Zwischen Judith Hermann *Nichts als Gespenster* und Maria Hauser *Valeries Baum*. FOTO0012 Teil 03 zeigt *Die feinen Leute* mit dem Untertitel *Von der vornehmen Art, durchs Leben zu gehen*; Verlagsvermerk Campus sichtbar. Bibliografisch eindeutig **Roland Girtler**. | **lesbar** |

### Bibliografische Kontrollquellen

- Brigitte Giraud: https://mein.perlentaucher.de/buch/brigitte-giraud/die-liebe-ist-doch-sehr-ueberschaetzt.html
- Petra Hammesfahr, `Bild Bestseller-Bibliothek` Band 6: https://diebuchsuche.at/buch-isbn-9783898971096.html
- Roland Girtler: https://www.zvab.com/9783853297407/feinen-Leute-vornehmen-Art-durchs-3853297404/plp

Die Quellen helfen bei der Identifikation; **die Ausgabe/ISBN des jeweils abgebildeten Exemplars wird nicht behauptet**, wo nicht eindeutig vom Buchrücken ablesbar.

## Geänderte Daten

- `daten/buecher.csv`: nur B00185, B00188 und B00198 durch vollständigen Autor/Titel ergänzt und auf `lesbar` gestellt.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: je eine konkrete Bild- und Katalognachprüfung dokumentiert.
- `daten/fachstatus.csv`, `daten/pruefplan_faecher.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md`: synchronisiert.
- Fotos, Kopien, Buch-IDs, Fachzuordnungen und Positionen nicht verändert.

## Bilanz und Fortsetzung

- Fach 2-7: **29** vorläufige Bucheinträge, **29 lesbar**, **0 prüfen**, **0 offen**. Damit vorläufig abgehakt.
- Gesamtbestand: **1048** vorläufige Bucheinträge, **959 lesbar**, **49 prüfen**, **40 offen** = **89** noch unsicher.
- **15** Fächer vorläufig abgehakt, **25** bislang nicht erneut gezielt geprüft; **11** bereits erneut geprüft mit verbliebenem Fotobedarf.
- **Nächstes Fach erst auf „Weiter“:** `2-8`, ausschließlich B00226.
