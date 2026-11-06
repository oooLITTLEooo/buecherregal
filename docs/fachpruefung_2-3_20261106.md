# Gezielte Nachprüfung Fach 2-3 – 06.11.2026

## Umfang

- Ausschließlich Fach **2-3** und die vier in `daten/pruefplan_faecher.csv` markierten Fälle `B00107`, `B00117`, `B00123`, `B00125` geprüft.
- Original im Git: `bilder/originale/PXL_20261105_151109630.jpg`, Foto-ID `FOTO0008`, 8160 × 4590 Pixel laut `daten/fotos.csv`.
- Vier zugehörige native Bildausschnitte `daten/bildanalyse/fullres/FOTO0008_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` visuell geprüft. Es wurden nur die vier vorher unsicheren Bücher gezielt bewertet; andere bereits `lesbar` markierte Bücher nicht erneut systematisch inventarisiert.

## Ergebnisse der vier Prüffälle

| ID | Pos. | Zustand vorher | Ergebnis und Beleg | Status nachher |
| --- | ---: | --- | --- | --- |
| `B00107` | 1 | Daniel Glattauer, *Ewig Dein*, `pruefen` | `FOTO0008`, Teil 1: Auf dem zurückstehenden blauen Rücken sind Daniel Glattauer und die Titelaufschrift erkennbar. Angaben bestätigt, keine Titeländerung | **lesbar** |
| `B00117` | 11 | William Golding, *Das Feuer der Finsternis*, `pruefen` | `FOTO0008`, Teil 2: Rückenbeschriftung bestätigt Autor und Titel, zwischen Joachim Gauck und Ken Follett | **lesbar** |
| `B00123` | 17 | unbekannt, `offen` | `FOTO0008`, Teile 3/4: Ein schmaler dunkler, zurückstehender Buchbereich zwischen Ken Follett *Eisfieber* und Ann Granger *Mord wirft lange Schatten* ist erkennbar, Autor, Titel und genaue Bandgrenze bleiben unsicher | **offen** |
| `B00125` | 19 | F. Scott Fitzgerald, *Vater heiratet eine ...*, `pruefen` | `FOTO0008`, Teil 4: Der graue Rücken zeigt *Vater heiratet eine Mormonin*. Der tatsächliche Autor ist **John D. Fitzgerald**, siehe bibliografischen Abgleich | **lesbar** |

### B00125: bibliografische Korrektur

Die bisherige Zuordnung zu **F. Scott Fitzgerald** war falsch. Im Foto ist der Name `Fitzgerald` und der Titel `Vater heiratet eine Mormonin` zu lesen. Bibliografische Belege für den vollständigen Autor **John D. Fitzgerald** und den deutschen Titel:

- LovelyBooks: https://www.lovelybooks.de/autor/John-D.-Fitzgerald/Vater-heiratet-eine-Mormonin-1347061750-w/
- ZVAB: https://www.zvab.com/9783499113505/Vater-heiratet-Mormonin-3499113503/plp
- John-D.-Fitzgerald-Bibliografie: https://de.wikipedia.org/wiki/John_D._Fitzgerald_%28Schriftsteller%29

Die Ausgabe und ISBN des fotografierten Exemplars wurden nicht nachgewiesen; keine unbelegten Angaben ergänzt.

### Gesonderte Auffälligkeit bei B00126 (nicht geändert)

Unmittelbar rechts von B00125 steht der zuvor bereits als lesbar markierte Band **B00126, *Der Fluch der Fitzgeralds***. Die oben genannte John-D.-Fitzgerald-Bibliografie ordnet **auch dieses Werk John D. Fitzgerald zu**, während `daten/buecher.csv` dafür weiterhin `F. Scott Fitzgerald` führt. **Dieser fünfte Eintrag wurde gemäß Nutzeranweisung, ausschließlich die vier unsicheren IDs zu bearbeiten, nicht verändert.** Die Autorenabweichung ist als *separat zu korrigierende Datenauffälligkeit* vermerkt; eine zukünftige kurze Einzelkorrektur ist sinnvoll.

## Für B00123 benötigte Aufnahme

Den schmalen dunklen Band direkt **zwischen Ken Follett *Eisfieber* (Pos. 16) und Ann Granger *Mord wirft lange Schatten* (Pos. 18)** einzeln herausnehmen und **Buchrücken, Vorderseite oder Titelblatt** frontal und scharf fotografieren. Ggf. vor Ort bestätigen, dass die erfasste Buchgrenze physisch tatsächlich vorhanden ist. Keine Titel geraten.

## Änderungen im Git

- `daten/buecher.csv`: Nur B00107 und B00117 auf `lesbar` gestellt; B00125 Autor und Titel korrigiert und als `lesbar` markiert; bei B00123 ausschließlich Bemerkung konkretisiert, weiterhin `offen`. **Alle übrigen Buchdatensätze, einschließlich B00126, unverändert.**
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Die vier Statusnachweise samt konkreten Fotobelegen aktualisiert.
- `daten/fachstatus.csv`: den aktuellen Fachstatus mit Fotobedarf nachgeführt.
- `daten/pruefplan_faecher.csv`: Fach 2-3 zu `neues_detailfoto_bei_bedarf` verschoben, nur `B00123` weiterhin unsicher.
- `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: zusammenfassende Arbeitsliste angepasst.
- Originalfoto, Bildausschnitte und positionsbezogene Kopie blieben unverändert; keine physische oder alphabetische Umsortierung.

## Neuer Stand

- Fach **2-3**: 20 vorläufige Bucheinträge, **19 mit Status lesbar**, **1 offen (B00123)**, 0 prüfen. B00126 hat jedoch noch eine gesondert notierte Autorenauffälligkeit trotz `lesbar`-Status.
- Gesamtes Regal: unverändert **1048** vorläufige Einträge, nun **952 lesbar**, **56 prüfen**, **40 offen** = **96** unsichere.
- **12** fotografierte Fächer vorläufig abgehakt. Von **39** Fächern mit formell offenen Büchern stehen **29** gezielte Prüfungen noch aus, **10** Fächer haben bereits eine erneute Bildprüfung mit Bedarf für bessere Fotos.

**Nächstes Fach erst nach erneutem „Weiter“:** `2-4`, ausschließlich `B00131` und `B00149`.
