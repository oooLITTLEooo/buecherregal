# Fachprüfung 7-4 – 06.11.2026

## Prüfgrundlage

- Ausschließlich **Regalfach 7-4** bearbeitet.
- Originalfoto: `bilder/originale/PXL_20261105_151640010.jpg`, Foto-ID `FOTO0049` (laut Foto-Inventar 8160 × 4590 Pixel).
- Vier hochauflösende Ausschnitte `daten/bildanalyse/fullres/FOTO0049_teil_01.jpg.base64.txt` bis `FOTO0049_teil_04.jpg.base64.txt` wurden direkt bildlich betrachtet. Sie bilden die Fachreihe von links nach rechts ab.
- `daten/buecher.csv` bei Prüfstart: **18 physische Bücher**, `B00970` bis `B00987`, Positionen 1–18, sämtlich bereits `lesbar`.

## Sichtkontrolle sämtlicher Buchrücken

| Position | Buch-ID | Autor | Auf dem Foto bestätigter Titel | Bildteil |
| ---: | --- | --- | --- | ---: |
| 1 | B00970 | Martha Grimes | Was am See geschah | 1 |
| 2 | B00971 | Joy Fielding | Tanz, Püppchen, tanz | 1 |
| 3 | B00972 | Ewald Arenz | Alte Sorten | 1 |
| 4 | B00973 | Martin Suter | Allmen und die Dahlien | 1 |
| 5 | B00974 | René Freund | Das Vierzehn-Tage-Date | 1 |
| 6 | B00975 | Agatha Christie | Nikotin | 2 |
| 7 | B00976 | Roger Willemsen | Der Knacks | 2 |
| 8 | B00977 | Ruth Rendell | See der Dunkelheit | 2 |
| 9 | B00978 | Willa Cather | Meine Antonia | 2 |
| 10 | B00979 | Judith Fanto | Viktor | 2 |
| 11 | B00980 | Andrea Camilleri | Der Dieb der süßen Dinge | 2 |
| 12 | B00981 | Martin Suter | Montecristo | 3 |
| 13 | B00982 | Martin Walker | Eskapaden | 3 |
| 14 | B00983 | Thomas Raab | Walter muss weg | 3 |
| 15 | B00984 | Elif Shafak | Der Geruch des Paradieses | 3 |
| 16 | B00985 | Tana French | Grabesgrün | 3 |
| 17 | B00986 | John Grisham | Der Regenmacher | 4 |
| 18 | B00987 | Ken Follett | Die Brücken der Freiheit | 4 |

**Prüfergebnis:** Alle 18 sichtbaren Buchrücken stimmen mit den bisherigen Autoren-, Titel- und Positionsangaben überein. Es wurde keine neue Fehlablesung, nachweislich fehlende Buch-ID oder doppelte Zählung festgestellt. Aus nicht sichtbaren Buchseiten lässt sich naturgemäß keine weitere Information ableiten.

## Früher unsichere Fälle

Die bereits in einem früheren Durchgang korrigierten Fälle sind auf dem Foto erneut eindeutig lesbar:
- `B00971`, Pos. 2: Joy Fielding – *Tanz, Püppchen, tanz* (Teil 1).
- `B00982`, Pos. 13: Martin Walker – *Eskapaden* (Teil 3).
- `B00985`, Pos. 16: Tana French – *Grabesgrün* (Teil 3).

Ihre vorhandenen Prüfdatensätze in `daten/bildanalyse/feinpruefung_unsicher.csv` bleiben unverändert, ebenso die zugehörigen Inventareinträge.

## Git-Änderungen und Ergebnis

- `daten/buecher.csv` **nicht verändert**: alle 18 Datensätze waren bereits korrekt.
- `daten/bildanalyse/feinpruefung_unsicher.csv` **nicht verändert**: alle drei früheren Prüffälle waren bereits gelöst.
- `daten/fachstatus.csv`: veralteten Hinweis `Einzelbucherfassung ausstehend` durch den abgeschlossenen Fachprüfstand ersetzt.
- Originalfoto und positionsbenannte Kopie unverändert; keine physische oder alphabetische Umsortierung.
- **Fach 7-4: 18/18 lesbar, 0 prüfen, 0 offen.**
- **Gesamtstand:** weiterhin **1048** vorläufige Bücher, **947 lesbar**, **60 prüfen**, **41 offen** (101 ungeklärt).

**Nächste Fachprüfung erst nach erneutem „Weiter“: Regalfach 7-5.**
