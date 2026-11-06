# Gezielte Nachprüfung Fach 4-7 – 06.11.2026

## Quelle und Umfang

- Git-Original `bilder/originale/PXL_20261105_151450088.jpg` (FOTO0028; 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Vier im Git gespeicherte Originalpixel-Ausschnitte: `daten/bildanalyse/fullres/FOTO0028_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt`.
- Ausschließlich sechs bisher unsichere IDs B00516, B00518, B00526, B00528, B00535 und B00540 erneut beurteilt. Die anderen 24 als lesbar markierten Buchdatensätze nicht erneut systematisch untersucht.

## Einzelentscheidungen

| ID | Position | Nachweis und Entscheidung | Status |
| --- | ---: | --- | --- |
| B00516 | 4 | Dunkler Buchbereich zwischen Konstantin Wecker *Der Klang der ungespielten Töne* und *Jeder Augenblick ist ewig* in FOTO0028 Teil 01. Kein eindeutiger vollständiger Titel, die physische Bandgrenze ist ebenfalls zu prüfen. Vorläufiger Autor Konstantin Wecker aus Erstinventar übernommen, nicht unabhängig bestätigt. | **offen** |
| B00518 | 6 | Der aus dem Erstinventar stammende Titel *Das heimliche Fest* ist im Teil 01 nicht sicher lesbar oder eindeutig dem vorhandenen Buchrücken zuzuordnen. Autor ebenfalls ungeklärt. | **pruefen** |
| B00526 | 14 | FOTO0028 Teil 02: *Warum Frauen schneller frieren* zwischen Erich Kästner *Lyrische Hausapotheke* und Håkan Nesser *Der Tote vom Strand*. Buch von **Martin Borré und Thomas Reintjes**, kompletter Titel *Warum Frauen schneller frieren: Alltagsphänomene wissenschaftlich erklärt*, bibliografisch bestätigt. | **lesbar** |
| B00528 | 16 | FOTO0028 Teil 02: *Ein Haus in Dalmatien* nach Nesser und vor J. D. Salinger. Autorin **Friederun Pleterski** durch den Verlag nachgewiesen. | **lesbar** |
| B00535 | 23 | FOTO0028 Teil 03: schmaler dtv-Rücken Nr. 10 mit *Roth – Ernst und heiter* nach *Beyond Survival* vor Safier *Muh!*. Bibliografisch eindeutig **Eugen Roth – Ernst und heiter**. | **lesbar** |
| B00540 | 28 | FOTO0028 Teile 03/04: schmaler, teilweise verdeckter Buchbereich zwischen Markaris *Faule Kredite* und Éric-Emmanuel Schmitt *Das Evangelium nach Pilatus*. Weder eine eindeutige physische Bandgrenze noch Autor und Titel gesichert. | **offen** |

### Bibliografische Quellen

- B00526: [3sat / Presseportal](https://www.presseportal.de/en/pm/6348/710235), [Hochschule Bonn-Rhein-Sieg](https://www.h-brs.de/de/pressemitteilung/gibt-es-kotzende-pferde-vor-der-apotheke).
- B00528: [Drava Verlag – Ein Haus in Dalmatien](https://drava.at/buecher/ein-haus-in-dalmatien-978-3-85435-820-6/).
- B00535: [BookBrainz – Eugen Roth, Ernst und heiter](https://bookbrainz.org/edition/42c1b6e1-a670-4ac2-8851-12f5b0ab36c7) und [Sammlung dtv-Umschlaggestaltung](https://aiap.it/2000-2020/cdpg/index%EF%B9%96IDsubarea%3D169%26IDsez%3D232%26order%3Dtitolo%26page%3D2%26order%3Danno%2Bdesc%26order%3Dtitolo%26order%3Drand%28%29.html).

Es wird keine nicht am fotografierten Exemplar gesicherte ISBN oder konkrete Auflage behauptet.

## Benötigte Nachfotos

- B00516: Dunklen Band zwischen den Wecker-Büchern *Der Klang der ungespielten Töne* und *Jeder Augenblick ist ewig* frontal fotografieren, bei Bedarf Bücher auseinanderziehen und separat zählen.
- B00518: Schmalen Rücken zwischen *Jeder Augenblick ist ewig* und *Sage nein!* frontal und mit Titelblatt aufnehmen, um *Das heimliche Fest* und den Autor zu bestätigen oder zu berichtigen.
- B00540: Rücken zwischen Markaris *Faule Kredite* und Schmitt *Das Evangelium nach Pilatus* freilegen, einzeln aufnehmen und physische Bandzahl kontrollieren.

## Git-Änderungen / Bilanz

- `daten/buecher.csv`: genau sechs problematische Buchzeilen angepasst. B00526, B00528 und B00535 von prüfen auf lesbar mit Autor-Nachweis. B00516, B00518 und B00540 unveränderte Identifikationsstatus mit konkretisierten Bemerkungen.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: sechs Nachprüfentscheidungen und direkte Fotoreferenzen nachgeführt.
- `daten/pruefplan_faecher.csv`: Fach 4-7 als nachgeprüft, drei verbleibende Problem-IDs, `neues_detailfoto_bei_bedarf`; nicht vorläufig abgehakt.
- `daten/fachstatus.csv`, Gesamtprüfplan und chronologische Fortschrittsprotokolle aktualisiert.
- Keine Originalbilder, Buch-IDs, anderen Buchzeilen oder Positionsnummern verändert.
- Fach 4-7: **30** vorläufige Einträge, **27 lesbar, 1 prüfen, 2 offen**.
- Gesamt **1048** vorläufige Einträge: **978 lesbar, 31 prüfen, 39 offen**; 70 verbleibende Identifikationsunsicherheiten.
- **18** Fächer vorläufig abgehakt, **12** noch gezielt zu prüfen, **20** nachgeprüft mit Restunsicherheiten, plus Fach 3-3 mit Zähl-/Positionskontrolle.
- Nächstes Fach **erst nach Weiter**: **4-8**, ausschließlich B00545 und B00558.
