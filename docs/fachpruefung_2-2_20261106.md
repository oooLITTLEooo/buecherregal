# Gezielte Nachprüfung Fach 2-2 – 06.11.2026

## Gegenstand

- In diesem Durchgang wurde **ausschließlich Fach 2-2** betrachtet und **nur der bisher offene Buchdatensatz `B00094`** auf Fachposition 15 untersucht.
- Unveränderte Git-Fotoquelle `bilder/originale/PXL_20261105_151105038.jpg`, Kennung `FOTO0007`, Auflösung laut `daten/fotos.csv` 8160 × 4590 Pixel.
- Gezielter Sichtabgleich mit den hochauflösenden Ausschnitten `daten/bildanalyse/fullres/FOTO0007_teil_02.jpg.base64.txt` und `FOTO0007_teil_03.jpg.base64.txt`.
- Originalfoto und bereits vorhandene Ausschnitte sind unverändert geblieben. Keine erneute Detailprüfung der übrigen 26 zuvor als lesbar erfassten Bucheinträge.

## Ergebnis B00094

| Merkmal | Beobachtung |
| --- | --- |
| Buch-ID | `B00094` |
| Fachposition | `2-2 / 15` |
| Nachweis | `FOTO0007` Teil 2 |
| Umfeld | Zwischen Barbara Frischmuth, *Kopftänzer* (Position 14), und Henrik Ibsen, *Nora (Ein Puppenheim)* (Position 16) |
| Bildbefund | Sehr schmaler dunkelgrauer Rücken, auf dem keine vollständige Titel-/Autorenangabe sicher entziffert werden kann |
| Identifikationsstatus | **`offen` bleibt unverändert** |
| Benötigtes Zusatzfoto | Den schmalen Band einzeln herausnehmen, **Rücken und Vorderseite oder Titelblatt** frontal und scharf fotografieren |

Der genaue Titel und der Autor werden **nicht** aus Nachbarbüchern oder unklaren Schriftfragmenten erschlossen. Die Anzahl von 27 vorläufigen Bänden und die Position 15 bleiben als bisherige Inventarannahme erhalten.

## Dokumentation im Git

1. `daten/buecher.csv`: Nur die Bemerkung zu B00094 auf die konkrete Fotostelle und den fehlenden Nachweis aktualisiert, **keine** Änderung an Titel, Autor, ID, Position oder Status.
2. `daten/bildanalyse/feinpruefung_unsicher.csv`: Nur B00094 erläutert; der Wert `bleibt_unsicher_nach_hochaufloesungspruefung` bleibt bestehen.
3. `daten/fachstatus.csv`: Die gezielte Prüfung und das nötige zusätzliche Detailfoto dokumentiert.
4. `daten/pruefplan_faecher.csv`: Fach 2-2 von `gezielte_pruefung` auf `neues_detailfoto_bei_bedarf` gestellt, **nicht abgehakt**.
5. `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: Übersicht mit der neuen Warteschlange synchronisiert.

## Stand

- Fach 2-2: **27** vorläufige Buchdatensätze, davon **26 lesbar**, **1 offen**, **0 prüfen**.
- Gesamt: **1048** vorläufige Datensätze; **949 lesbar**, **59 prüfen**, **40 offen** (99 ungeklärt).
- **12** der 51 fotografierten Fächer sind vorläufig abgehakt; **39** besitzen mindestens einen offenen Eintrag. Davon **30** noch gezielt zu untersuchen und **9** bereits erneut angesehen, die weitere Bildinformationen brauchen.

**Nächster Durchgang erst nach neuem „Weiter“:** Fach **2-3**; dort nur **B00107, B00117, B00123 und B00125**.
