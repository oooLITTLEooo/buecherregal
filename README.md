# Bücherregal – Inventar und Sortierung

Dieses **private** Repository ist die zentrale Projektablage für die Erfassung und spätere alphabetische Sortierung eines Bücherregals. Die Sichtbarkeit wurde am 2026-11-06 auf GitHub als `private` bestätigt.

## Projektziele

- Regalfächer anhand eines Übersichtsfotos systematisch identifizieren und nummerieren.
- Alle Bücher anhand von Detailfotos erfassen: Autor, Titel und ursprünglicher Standort.
- Den ursprünglichen Platz jedes Buchs dokumentieren, damit es wiedergefunden werden kann.
- Später eine alphabetische Sortierung nach dem **Nachnamen des Autors** planen.
- Nutzerfotos sowie gegebenenfalls erzeugte Bilder im Repository versionieren.

## Ordnungssystem

Die Fächer werden **spaltenweise** nummeriert: links oben beginnend in der ersten Spalte nach unten, danach die zweite Spalte wieder oben beginnend nach unten, usw. `1-4` bedeutet: erste Spalte, viertes Fach von oben.

Zusätzlich erfasst `position_im_fach` die Position des Buchs im jeweiligen Fach, gezählt von links nach rechts. Die tatsächlichen Fächer und Spalten werden anhand des Übersichtsfotos und der Detailfotos festgelegt.

## Verzeichnisübersicht

- `daten/buecher.csv` – Buchinventar mit ursprünglichen Standorten
- `daten/fotos.csv` – Zuordnung der Aufnahmen zu den Regalfächern und Uploadstatus
- `docs/standorte.md` – Nummerierung und Erfassungsregeln
- `docs/uebersicht.md` – visuelle Ersteinschätzung des Gesamtfotos
- `docs/protokoll.md` – Projektverlauf
- `bilder/originale/` – Nutzerfotos, sprechende Dateinamen, unveränderter Bildinhalt
- `bilder/generiert/` – erzeugte Bilder/Grafiken

## Benennung der Fotos

- Gesamtübersicht: `Regal_Gesamt.jpg`
- Einzelnes Fach: `Regal_1-4.jpg` (erste Spalte, viertes Fach von oben)
- Mehrere Fotos eines Faches: `Regal_1-4_02.jpg` etc.

Dateiendung passend zum echten Bildformat beibehalten. Originale können unverändert umbenannt werden. Siehe `bilder/README.md`.

## Aktueller Stand

- Repository-Sichtbarkeit: **private**.
- Dokumentation und leere Inventardateien angelegt.
- Übersichtsfoto (`F0001`) und achtzehn Detailfotos (`F0002` bis `F0019`) im Chat empfangen.
- Achtzehn belegte Fächer erfasst: `1-5` bis `1-8`, `2-1` bis `2-8` sowie `3-1` bis `3-6`.
- In `daten/buecher.csv` 362 vorläufige Buchpositionen im ersten Erfassungsdurchgang, davon 68 noch offen/zu prüfen.
- Fortschritt und fehlende Fotos in `daten/fachstatus.csv` dokumentiert. **Nächstes Foto: `3-7`, danach `3-8`.**
- **Die 19 Original-JPEG-Dateien sind noch nicht in GitHub hochgeladen**, aber als ZIP mit korrekten Git-Dateinamen gesichert. Der in `daten/fotos.csv` gespeicherte Dateiname ist vorerst der beabsichtigte Git-Name.
- Alphabetische Umordnung erst auf Anweisung des Nutzers.

## Datenschutz und Arbeitsweise

- Alle Projektänderungen werden in Git dokumentiert.
- Eine Upload-Zusage gilt erst, wenn die Bilddatei tatsächlich ins Git-Repository übertragen und verifiziert wurde.
