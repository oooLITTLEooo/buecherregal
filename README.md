# Bücherregal – Inventar und Sortierung

Dieses **private** Repository ist die zentrale Projektablage für die Erfassung und spätere alphabetische Sortierung eines Bücherregals. Die Sichtbarkeit wurde am 2026-11-06 direkt auf GitHub als `private` bestätigt.

## Projektziele

- Regalfächer anhand eines Übersichtsfotos systematisch identifizieren und nummerieren.
- Alle Bücher anhand von Detailfotos erfassen: Autor, Titel und ursprünglicher Standort.
- Den ursprünglichen Platz jedes Buchs dokumentieren, damit es wiedergefunden werden kann.
- Später eine alphabetische Sortierung nach dem **Nachnamen des Autors** planen.
- Vom Nutzer bereitgestellte Originalfotos sowie gegebenenfalls später erzeugte Bilder im Repository versionieren.

## Ordnungssystem

Die Fächer werden **spaltenweise** nummeriert: links oben beginnend in der ersten Spalte nach unten, danach die zweite Spalte wieder oben beginnend nach unten, usw. `1-5` bedeutet: erste Spalte, fünftes Fach von oben.

Zusätzlich erfasst `position_im_fach` die Position des Buchs im jeweiligen Fach, gezählt von links nach rechts. Die tatsächlichen Fächer und Spalten werden erst anhand des Übersichtsfotos festgelegt.

## Verzeichnisübersicht

- `daten/buecher.csv` – Buchinventar mit ursprünglichen Standorten
- `daten/fotos.csv` – Zuordnung der Aufnahmen zu den Regalfächern
- `docs/standorte.md` – Nummerierung und Erfassungsregeln
- `docs/protokoll.md` – Projektverlauf und getroffene Entscheidungen
- `bilder/originale/` – unveränderte Originalfotos
- `bilder/generiert/` – später erzeugte Bilder und Grafiken

## Aktueller Stand

- Repository-Sichtbarkeit: **private** (geprüft am 2026-11-06).
- Dokumentationsstruktur und leere Inventardateien angelegt.
- Regalfotos und Buchinventar noch nicht erfasst.
- Nächster Schritt: Übersichtsfoto entgegennehmen, danach Detailfotos der Regalfächer. Erst nach Anweisung des Nutzers die Ergebnisse und Sortierung ausgeben.

## Datenschutz und Arbeitsweise

- Alle Projektänderungen werden direkt in Git dokumentiert.
- Bilddateien werden nach Möglichkeit im Originalformat gespeichert und über `daten/fotos.csv` referenziert.
- Eine Upload-Zusage gilt erst, wenn die jeweilige Datei tatsächlich ins Git-Repository übertragen und verifiziert wurde.
