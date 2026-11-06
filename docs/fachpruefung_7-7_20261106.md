# Fachprüfung 7-7 – 06.11.2026

## Grundlage und Umfang

- In diesem Durchgang wurde **ausschließlich Fach 7-7** untersucht.
- Original im Git: `bilder/originale/PXL_20261105_151658812.jpg` (Foto-ID `FOTO0052`, 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Alle vier vorhandenen hochauflösenden Ausschnitte unter `daten/bildanalyse/fullres/FOTO0052_teil_01.jpg.base64.txt` bis `FOTO0052_teil_04.jpg.base64.txt` wurden tatsächlich visuell geprüft.
- Vor und nach der Prüfung: **16 vorläufige physische Bucheinträge** `B01033` bis `B01048` mit Positionen 1–16 von links nach rechts.

## Abgleich der Bücher

| Pos. | Buch-ID | Autor | Titel | Bildbeleg |
| ---: | --- | --- | --- | --- |
| 1 | B01033 | John Irving | Gottes Werk und Teufels Beitrag | Teil 1 |
| 2 | B01034 | Marcel Reich-Ranicki | Mein Leben | Teil 1 |
| 3 | **B01035** | Erich Fried | **Titel nicht sicher erkennbar** | Teil 1, siehe offene Stelle |
| 4 | B01036 | Erich Fried | Vorübungen für Wunder | Teil 1 |
| 5 | B01037 | Charlotte Link | Wilde Lupinen | Teil 2 |
| 6 | B01038 | Michael Ende | Die unendliche Geschichte | Teil 2 |
| 7 | B01039 | Thomas Raab | Der Metzger sieht rot | Teil 2 |
| 8 | B01040 | Elisabeth Reichart | Die Voest-Kinder | Teil 2 |
| 9 | B01041 | Thomas Raab | Der Metzger bricht das Eis | Teil 2 |
| 10 | B01042 | Thomas Raab | Der Metzger muss nachsitzen | Teil 3 |
| 11 | B01043 | Andreas Englisch | Franziskus: Zeichen der Hoffnung | Teil 3 |
| 12 | B01044 | Anne B. Ragde | Tod im Fjord / Mord in Spitzbergen | Teil 3, ein physischer Sammelband |
| 13 | B01045 | Erika Pluhar | Am Ende des Gartens | Teil 3 |
| 14 | B01046 | Jörg Maurer | Die große Hitze | Teil 4 |
| 15 | B01047 | Charlotte Link | Sturmzeit | Teil 4 |
| 16 | B01048 | Charlotte Link | Die letzte Spur | Teil 4 |

**15** Autor-/Titel-Einträge stimmen mit den sichtbaren Buchrücken überein. Frühere Nachprüfungen für B01036, B01039, B01044 und B01046 sind bereits als `korrigiert_und_lesbar` in der Prüfliste dokumentiert; deren Buchfelder mussten nicht erneut geändert werden.

## Noch ungeklärt

- **B01035, vorläufige Position 3, `offen`:** auf `FOTO0052` Teil 1 ein eigener, etwas zurückstehender dunkler Band zwischen Marcel Reich-Ranickis *Mein Leben* (Position 2) und Erich Frieds *Vorübungen für Wunder* (Position 4). Der Name **Erich Fried** ist sichtbar, aber der eigenständige Titel nicht zuverlässig lesbar.
- **Benötigt:** den betreffenden Band einzeln herausziehen, Rücken und Vorderseite bzw. Titelblatt scharf fotografieren. Bis dahin Autor und vorläufige Position beibehalten, Titel nicht raten.
- Ein **Friedrich-Gulda-Hörbuch mit „2 CD“** ist auf Bildteil 2 sichtbar. Es ist kein gedrucktes Buchexemplar und wird gemäß Inventurregel **nicht** als zusätzliche Buch-ID gezählt.

## Git-Veränderungen

- `daten/buecher.csv`: nur bei B01035 die Bemerkung mit genauer Bildreferenz und Zusatzfoto-Anforderung ersetzt; Status, Buch-ID, Fotoquelle, Titel- und Autorenfelder und Position nicht verändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: nur beim offenen Prüffall B01035 den Nachweis präzisiert; Entscheidung `bleibt_unsicher_nach_hochaufloesungspruefung` bleibt erhalten.
- `daten/fachstatus.csv`: den veralteten Hinweis `Einzelbucherfassung ausstehend` durch den geprüften Stand ersetzt.
- Alle Originalfotos, Bildausschnitte und positionsbenannten Bildkopien bleiben unverändert. Keine alphabetische Umsortierung und kein anderes Fach bearbeitet.

## Ergebnis Fach 7-7

- **16** vorläufige Bucheinträge.
- **15** `lesbar`, **0** `pruefen`, **1** `offen`.
- **1048** vorläufige Bucheinträge im ganzen Regal, davon **947 lesbar**, **60 pruefen**, **41 offen** (101 noch ungeklärt).

## Offene Fächer im ganzen Regal – Zählung nach Datenbestand

Das Regal ist als **8 × 8 = 64** Positionen dokumentiert. `daten/fotos.csv` enthält **51 verschiedene Detailfotos zu 51 Fächern**. Alle 51 haben bereits eine **vorläufige Inventarisierung**, die beim ersten Durchgang anhand der originalen Pixelbereiche erfolgte. Die spezielle **erneute Einzelfach-Nachprüfung in den neueren Chats** erstreckt sich nun über **11 Fächer**, nämlich 6-5 bis 6-8 und 7-1 bis 7-7; **40** früher inventarisierte Fächer (1-5 bis 6-4) müssten noch einmal nach diesem zusätzlichen Kontrollstandard geprüft werden, falls ein vollständiger zweiter Durchgang gewünscht ist.

Zu den übrigen **13 Fächern ohne Detailaufnahme** verzeichnet `daten/fachstatus.csv`:
- **1-1, 1-2, 1-3:** laut Gesamtbild leer.
- **1-4:** Lampe, kein Buchfach zu fotografieren.
- **7-8:** verdeckt; Buchbestand noch unklar, weitere Aufnahme sinnvoll.
- **8-1, 8-2:** Bücher erkennbar, **Detailaufnahmen erforderlich**.
- **8-3 bis 8-8:** laut Gesamtbild leer oder unklar; Belegung vor Ort bestätigen.

Damit ist 7-7 das **letzte bereits mit einem Einzelfoto versehene Fach in der bisherigen Reihenfolge**. Ohne zusätzliche Aufnahmen lässt sich 7-8 und die rechte Regalspalte nicht vollständig inventarisieren.

**Fortsetzung erst nach neuem „Weiter“:** mit dem Nutzer festlegen, ob zuerst die ausstehenden drei gezielten Fotos (7-8, 8-1, 8-2) erstellt werden oder die 40 bereits inventarisierten Fächer einzeln ein zweites Mal nachgeprüft werden. In jedem Fall genau **ein Fach pro Arbeitsdurchgang**.
