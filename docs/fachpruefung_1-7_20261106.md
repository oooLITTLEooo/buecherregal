# Gezielte Nachprüfung Fach 1-7 – 06.11.2026

## Vorgabe und Quelle

- In diesem Durchgang wurde **ausschließlich Regalfach 1-7** behandelt und **nur der bisher prüfpflichtige Eintrag B00034** erneut identifiziert. Keine erneute Vollanalyse der 14 bereits als `lesbar` erfassten Bücher.
- Git-Originalfoto: `bilder/originale/PXL_20261105_151044826.jpg` (`FOTO0004`, laut `daten/fotos.csv` 8160 × 4590 Pixel). Kein Originalbild verändert.
- Gezielte Sichtung der originalpixelbasierten Ausschnitte `daten/bildanalyse/fullres/FOTO0004_teil_01.jpg.base64.txt` und `FOTO0004_teil_02.jpg.base64.txt`.
- Auf **Teil 2** sind direkt am Rücken **„B. Ludwig“** sowie **„Anleitung zum Herzinfarkt“** lesbar. Pos. 5 steht zwischen Henning Mankell, *Die falsche Fährte*, und Nelson Mandela, *Der lange Weg zur Freiheit*.

## Bibliografische Abklärung B00034

| Feld | Vorher | Nachher |
| --- | --- | --- |
| `buch_id` | B00034 | unverändert |
| Fach / physische Position | 1-7 / 5 | unverändert |
| `autor_nachname` | Ludwig | unverändert |
| `autor_vorname` | B. | **Bernhard** |
| `titel` | Anleitung zum Herzinfarkt | unverändert |
| `identifikationsstatus` | pruefen | **lesbar** |

**Quellenabgrenzung:** Das Git-Original zeigt nur den Anfangsbuchstaben `B.`. Der ausgeschriebene Vorname **Bernhard** wird durch übereinstimmende bibliografische Nachweise zum gleichnamigen Buch bestätigt:

- https://buch-schaden.at/produkt/anleitung-zum-herzinfarkt-leb-schneller-besser-kuerzer/
- https://bookbot.at/g/1051979

Damit ist die Titelzuordnung in Verbindung mit der eindeutigen Rückenbeschriftung geklärt. Die genaue Auflage des fotografierten Exemplars wurde **nicht** bestimmt; keine unbewiesenen Auflagen- oder ISBN-Daten ergänzt.

## Git-Änderungen

1. `daten/buecher.csv`: bei `B00034` Vorname `Bernhard` ergänzt, Status auf `lesbar` gesetzt und Bild-/Katalogbeleg in der Bemerkung dokumentiert.
2. `daten/bildanalyse/feinpruefung_unsicher.csv`: B00034 auf `korrigiert_und_lesbar` gesetzt; begründender Bild-/Katalognachweis hinterlegt.
3. `daten/fachstatus.csv`: Fach 1-7 als **vorläufig abgehakt** gekennzeichnet.
4. `daten/pruefplan_faecher.csv`: Fach 1-7 von `gezielte_pruefung` auf `vorlaeufig_abgehakt` gesetzt; **15 lesbar, 0 pruefen, 0 offen**.
5. `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: Übersichtsstand entsprechend nachgeführt.

Alle 14 übrigen bereits als lesbar erfassten Exemplare, sämtliche Positionen, Buch-IDs, Fotoquellen und Originalfotos bleiben unverändert. **Vorläufig abgehakt** bedeutet keine unabhängige vollständige Zweitsichtung dieser 14 Einträge.

## Ergebnis

- Fach 1-7: **15** physische Bucheinträge, **15 lesbar, 0 pruefen, 0 offen**.
- Global: **1048** vorläufige Bucheinträge, **948 lesbar, 59 pruefen, 41 offen** (100 ungeklärte).
- Nun **11** fotografierte Fächer vorläufig abgehakt, **40** fotografierte Fächer mit mindestens einem offenen/prüfpflichtigen Eintrag. Davon **33** noch gezielt zu untersuchen und **7** bereits eingehend geprüft, die auf bessere Fotos warten.
- **Nächstes Fach erst auf erneutes „Weiter“:** `1-8`, nur der noch unsichere Eintrag `B00055`.
