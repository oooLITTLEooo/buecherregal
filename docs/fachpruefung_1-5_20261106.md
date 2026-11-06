# Fachprüfung 1-5 – zweite Einzelfachkontrolle am 06.11.2026

## Umfang und Quellen

- **Nur Fach 1-5** geprüft. Das ist die zusätzliche zweite, streng fachweise Sichtkontrolle nach der bereits abgeschlossenen ersten Erfassung aller verfügbaren Originalfotos.
- Verwendet wurde ausschließlich der tatsächliche Git-Fotobestand: `FOTO0002`, Original `bilder/originale/PXL_20261105_151031219.jpg`, laut `daten/fotos.csv` **8160 × 4590 Pixel**.
- Alle vier hochauflösenden Pixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0002_teil_01.jpg.base64.txt` bis `FOTO0002_teil_04.jpg.base64.txt` wurden direkt als Bilder betrachtet und gegen `daten/buecher.csv` abgeglichen.
- 14 physische Bände mit Buch-IDs `B00001` bis `B00014`, Positionen 1–14 von links nach rechts. Keine zusätzlichen sichtbaren Bände oder Dubletten festgestellt.

## Einzelkontrolle der 14 Bücher

| Pos. | Buch-ID | Autor | Titel (nach Prüfung) | Bildausschnitt |
| ---: | --- | --- | --- | ---: |
| 1 | B00001 | Marc Elsberg | Blackout | 1 |
| 2 | B00002 | Jodi Picoult | Zeit der Gespenster | 1 |
| 3 | **B00003** | Erika Pluhar | **Als gehörte eins zum andern** | 1 |
| 4 | B00004 | Henning Mankell | Die rote Antilope | 1/2 |
| 5 | B00005 | Henning Mankell | Die Rückkehr des Tanzlehrers | 2 |
| 6 | B00006 | Henning Mankell | Der Feind im Schatten | 2 |
| 7 | B00007 | Thomas Mann | Tagebücher 1953–1955 | 2 |
| 8 | B00008 | Jodi Picoult | Das Herz ihrer Tochter | 2 |
| 9 | B00009 | Henning Mankell | Tea-Bag | 3 |
| 10 | B00010 | Rosamunde Pilcher | Wilder Thymian | 3 |
| 11 | B00011 | Thomas Mann | Joseph und seine Brüder | 3 |
| 12 | B00012 | Golo Mann | Deutsche Geschichte des 19. und 20. Jahrhunderts | 3 |
| 13 | B00013 | Henning Mankell | Mittsommermord | 4 |
| 14 | B00014 | Jodi Picoult | Zerbrechlich | 4 |

## Eine eindeutige Korrektur

- **B00003**, Position 3: zuvor `Als gehöre eins zum andern`; der tatsächliche Buchrücken auf **FOTO0002 Teil 1** zeigt `ALS GEHÖRTE EINS ZUM ANDERN`. In `daten/buecher.csv` deshalb auf **`Als gehörte eins zum andern`** geändert.
- Buch-ID, Autor, Fachposition, Lesbarkeitsstatus und Quelle blieben erhalten; die Bemerkung enthält jetzt den konkreten Bildnachweis.
- Die anderen 13 Einträge stimmten mit den lesbaren Buchrücken überein; die Bezeichnung `lesbar` wurde daher nicht neu vergeben. **Kein** Eintrag dieses Faches blieb unsicher.

## Git-Dokumentation, Datenintegrität, Grenzen

- `daten/buecher.csv`: ausschließlich Titel und Bemerkung von B00003 geändert, keine neuen/gelöschten Datensätze.
- `daten/fachstatus.csv`: veraltete Notiz `Einzelbucherfassung ausstehend` durch den Abschluss der zweiten Sichtprüfung ersetzt.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: nicht verändert, da dieses Fach keine offenen Prüffälle hatte.
- Originalfoto `FOTO0002`, alle kodierten Bildausschnitte sowie die positionsbenannte Foto-Kopie unverändert. Keine alphabetische oder physische Umsortierung.
- Prüfgrundlage sind die **sichtbaren Rücken**, nicht die nicht einsehbaren Innenseiten oder versteckten Bände.

**Ergebnis Fach 1-5:** 14/14 Bände lesbar, 0 `pruefen`, 0 `offen`; eine Schreib-/Lesekorrektur.

**Globaler Stand:** 1048 vorläufige Bucheinträge, 947 `lesbar`, 60 `pruefen`, 41 `offen`; weiterhin 101 ungeklärte Einträge. Die Gesamtzahl ist wegen fehlender Detailfotos und möglicher unsichtbarer Bände noch vorläufig.

**Fortsetzung erst auf neues „Weiter“:** Fach **1-6** – genau ein Fach pro Durchgang.
