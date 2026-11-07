# Gezielte Nachprüfung Fach 5-7 – 07.11.2026

## Verbindliche Git-Bildquelle und Prüfungsumfang

- Git-Original: `bilder/originale/PXL_20261105_151527033.jpg` = `FOTO0036` (8160 × 4590 Pixel laut `daten/fotos.csv`); zugeordnete Kopie `bilder/umbenannt/Regal_5-7.jpg`.
- Einzeln gelesen: die im Git vorhandenen Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0036_teil_03.jpg.base64.txt` und `FOTO0036_teil_04.jpg.base64.txt`. Diese decken die Positionen 13 und 18 ab.
- **Nur B00701 und B00706** neu bewertet; die übrigen 16 Bucheinträge des Fachs nicht erneut inventarisiert. Keine Foto-, Fach-, Buch-ID-, Fotoverweis- oder Positionsänderungen.

## Entscheidungen

| Buch-ID | Vorläufige Position | Befund | Entscheidung |
| --- | ---: | --- | --- |
| **B00701** | 13 | FOTO0036 Teil 03 zeigt einen weißen C.H.Beck-Rücken mit **Sehnsucht** und das auffällige Bild einer römischen Gebäudefassade. Vergleich mit der bebilderten gebundenen Ausgabe von **Sabine Gruber – Stillbach oder Die Sehnsucht** ergibt eine Übereinstimmung des charakteristischen Einbandmotivs, Titels und Verlags. Der übrige Rückenaufdruck ist teilweise verdeckt/abgenutzt. | **lesbar** – Autorin **Sabine Gruber**, vollständiger Titel **Stillbach oder Die Sehnsucht** |
| **B00706** | 18 | FOTO0036 Teil 04: letzter breiter, hellblau/türkiser Hardcover-Rücken unmittelbar rechts von Håkan Nesser *Eine ganz andere Geschichte*. Die goldene Prägung ist zu stark verblasst, um Autor oder Werktitel sicher zu unterscheiden. Kein Titelgeraten. | **offen**, wie zuvor |

## Bibliografischer und visueller Abgleich zu B00701

- [Sabine Gruber, offizielle Werkseite](https://www.sabinegruber.at/werke/stillbach-oder-die-sehnsucht) – *Stillbach oder Die Sehnsucht*, C.H.Beck, München, 2011.
- [C.H.Beck-Verlagskatalog](https://www.chbeck.de/buecher/literatur/literatur-bei-chbeck/) – die Autorin und der Roman stehen gemeinsam im offiziellen Literaturverzeichnis.
- [Knihobot – fotografiertes Hardcover mit Gebäude-/Schneemotiv](https://knihobot.cz/g/3123742) – Einbandmotiv und Gestaltung sind mit dem fotografierten Git-Exemplar vergleichbar.
- [C.H.Beck-Verzeichnis der Ausgabe 2011](https://cms.chbeck.de/buecher/gesamtverzeichnis/?query=Stillbach) – Hardcover-Nachweis. Das genaue ISBN-/Auflagenmerkmal des **vorhandenen** Exemplars ist am Git-Foto nicht direkt bestätigt und wird daher nicht als zwingende Exemplarangabe übernommen.

Der externe Einbandvergleich dient ausschließlich dem Werk-/Autorenabgleich. Die tatsächliche Regalposition stammt ausschließlich aus dem Git-Foto und der bisherigen Inventur.

## Notwendiges Nachfoto

Für **B00706** das letzte große blaue Buch **rechts neben Håkan Nesser *Eine ganz andere Geschichte*** einzeln herausziehen und bei schrägem, reflexionsarmem Licht fotografieren. **Titelblatt** und möglichst Impressum zusätzlich aufnehmen; verblasste Schrift nicht frei ergänzen.

## Git-Nachführung und Bilanz

- `daten/buecher.csv`: B00701 auf `lesbar` gesetzt, Autorin/Titel präzisiert; bei B00706 nur Nachfotobedarf und sichtbaren Befund dokumentiert, Status `offen` unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: B00701 als `korrigiert_und_lesbar`, B00706 weiterhin `bleibt_unsicher_nach_hochaufloesungspruefung`; beide Entscheidungen belegt.
- `daten/pruefplan_faecher.csv`: Fach 5-7 = **18** vorläufige Datensätze, **17 lesbar, 0 prüfen, 1 offen**. Status `neues_detailfoto_bei_bedarf`, zweite Prüfung `ja`, offene ID B00706.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: entsprechend synchronisiert.
- **Gesamter vorläufiger Bestand: 1048** Einträge, davon **995 lesbar, 16 prüfen, 37 offen** (53 unsicher).
- **20** Fächer vorläufig abgehakt; **4** Fächer noch in der ersten gezielten Prüfrunde; **26** nachgeprüfte Fächer mit Restunsicherheiten, zusätzlich Sonderprüfung Fach 3-3 bezüglich möglicher Positions-/Zählabweichung.
- Fach 5-7 bleibt **nicht abgehakt**. **Nächstes Fach erst bei „Weiter“: 5-8**, nur B00711, B00718 und B00719.
