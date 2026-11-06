# Bücherregal – Inventar und Sortierung

Dieses Repository ist die zentrale Projektablage für die Erfassung und spätere alphabetische Sortierung eines Bücherregals.

> **Datenschutz:** Bis das Repository auf **private** gestellt und die Sichtbarkeit erneut geprüft wurde, werden hier keine Originalfotos, Buchdaten oder sonstigen persönlichen Inhalte abgelegt.

## Projektziele

- Regalfächer anhand eines Übersichtsfotos systematisch identifizieren und nummerieren.
- Alle Bücher anhand von Detailfotos erfassen: Autor, Titel und ursprünglicher Standort.
- Standort jedes Buchs so dokumentieren, dass es wiedergefunden werden kann.
- Später eine alphabetische Sortierung nach dem **Nachnamen des Autors** planen.
- Originalfotos und ggf. später erzeugte Bilder im selben Repository versionieren.

## Ordnungssystem

Die Fächer werden **spaltenweise** nummeriert: links oben beginnend in der ersten Spalte nach unten, danach die zweite Spalte wieder oben beginnend nach unten, usw. `1-5` bedeutet: erste Spalte, fünftes Fach von oben.

Zusätzlich erfasst `position_im_fach` die Position des Buchs im jeweiligen Fach, gezählt von links nach rechts.

## Verzeichnisübersicht

- `daten/buecher.csv` – Buchinventar mit ursprünglichen Standorten
- `daten/fotos.csv` – Zuordnung der Aufnahmen zu den Regalfächern
- `docs/standorte.md` – Nummerierung und Erfassungsregeln
- `docs/protokoll.md` – Projektverlauf und getroffene Entscheidungen
- `bilder/originale/` – unveränderte Originalfotos (erst nach Umstellung auf private)
- `bilder/generiert/` – später erzeugte Bilder/Grafiken (erst nach Umstellung auf private)

## Aktueller Stand

- Repository initialisiert.
- Regalfotos und Buchinventar noch nicht erfasst.
- **Offener Schritt:** Repository-Sichtbarkeit von public auf private ändern und prüfen.
- Erst danach Bilder und Inhalte hochladen.
