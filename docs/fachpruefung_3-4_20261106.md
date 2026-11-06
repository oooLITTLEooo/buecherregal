# Gezielte Nachprüfung Fach 3-4 – 06.11.2026

## Quelle und Umfang

- Aktueller Git-Stand vor der Prüfung: `f89e79527b7cbea2a10d92b35ac0165e09a2645f` (Branch `main`).
- Unverändertes Originalfoto aus dem Git: `bilder/originale/PXL_20261105_151321696.jpg`, FOTO0017; laut `daten/fotos.csv` 8160 × 4590 Pixel.
- Native Git-Pixelausschnitte `daten/bildanalyse/fullres/FOTO0017_teil_03.jpg.base64.txt` und `daten/bildanalyse/fullres/FOTO0017_teil_04.jpg.base64.txt` gezielt geprüft.
- Einziger bisher unsicherer Datensatz im Fach: **B00318** (Position 17). Die 21 übrigen als lesbar markierten Exemplare wurden nicht erneut systematisch bearbeitet.

## Einzelfall B00318

| Merkmal | Ergebnis |
| --- | --- |
| Fach / bisherige Position | **3-4 / 17** |
| Bisheriger Identifikationsstatus | `offen` |
| Direkt links laut Inventar | B00317 – **John Irving**, *Eine Mittelgewichts-Ehe* (Pos. 16) |
| Direkt rechts laut Inventar | B00319 – **John Irving**, *Zirkuskind* (Pos. 18) |
| Befund | In den Originalpixel-Bildteilen 03/04 sind an dieser Stelle nur sehr schmale, teilweise überlagerte bzw. nicht eindeutig trennbare Buchkanten erkennbar. Ob **B00318** ein eigener physischer Band ist, lässt sich nicht sicher feststellen. Autor/Titel nicht belegbar. |
| Entscheidung | **Bleibt `offen`**. Kein Titel geraten, keine Bandzahl als bestätigt ausgegeben. |

### Nötige Zusatzaufnahme

Den Bereich von **John Irving – *Eine Mittelgewichts-Ehe*** über die mögliche zusätzliche Buchkante bis **John Irving – *Zirkuskind*** frontal und scharf fotografieren. Ideal: Beide bekannten Bände kurz auseinanderziehen und prüfen, ob dazwischen tatsächlich ein eigenständiges drittes Exemplar steht. Bei einem eigenständigen Buch auch Titelblatt abbilden.

## Git-Änderungen und Abgrenzung

- `daten/buecher.csv`: nur die Belegbemerkung von B00318 konkretisiert. Buch-ID, `offen`-Status, Standort, Positionsnummer und Fotoquelle unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: dokumentiert, dass die gezielte Nachprüfung erfolgte und die physische Buchabgrenzung weiterhin ungesichert ist.
- `daten/fachstatus.csv` und `daten/pruefplan_faecher.csv`: Fach von `gezielte_pruefung` zu `neues_detailfoto_bei_bedarf` mit `zweite_sichtpruefung=ja` nachgeführt.
- Gesamtprüfplan und chronologische Protokolle aktualisiert. Originalfotos, Positionskopien und alle anderen Bucheinträge unverändert.

## Ergebnis und Fortsetzung

- Fach 3-4: **22 vorläufige Einträge**, **21 lesbar**, **0 prüfen**, **1 offen** (B00318). Die physische Bandzahl muss an Position 17 noch geprüft werden; Fach nicht abgehakt.
- Gesamtes Inventar unverändert: **1048** vorläufige Einträge, **967 lesbar**, **42 prüfen**, **39 offen** (= **81** Unsicherheiten).
- **16** Fächer vorläufig abgehakt, **20** weitere Fächer noch gezielt nachzuprüfen, **14** bereits nachgeprüft mit offener Identifikationsfrage. Fach 3-3 separat mit Positions-/Zählabgleich.
- **Nächstes Fach erst nach erneutem „Weiter“: 3-5**, nur die vier unsicheren IDs **B00329, B00330, B00332 und B00333**.
