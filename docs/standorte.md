# Nummerierung und Erfassungsregeln

## Fächer

Ein Standort besteht aus `Spalte-Fach`.

- `1-1`: erste Spalte von links, oberstes Fach.
- `1-2`: erste Spalte von links, zweites Fach von oben.
- `1-5`: erste Spalte von links, fünftes Fach von oben.
- `2-1`: zweite Spalte von links, oberstes Fach.

Die tatsächliche Anzahl der Spalten und Fächer wird erst nach Sichtung des Übersichtsfotos festgelegt.

## Buchpositionen

Pro Fach wird von links nach rechts in der tatsächlichen Reihenfolge gezählt: `1`, `2`, `3` usw. Die Positionen bezeichnen zunächst den **Ist-Zustand**, nicht eine bereits geplante Sortierung.

## Inventar

Ein Datensatz je Buch bzw. physischem Exemplar. Pflichtfelder nach Identifikation: `buch_id`, `autor_nachname`, `titel`, `standort`, `position_im_fach`.

Nicht eindeutig identifizierbare Angaben werden als `unsicher` oder `unbekannt` gekennzeichnet. Keine Titel/Autoren erfinden. Doppelte Exemplare erhalten unterschiedliche IDs.

## Sortierziel

Alphabetisch A–Z nach Nachname des Autors, bei gleichem Nachnamen nach Vorname und danach nach Titel. Reihenfolge der Regalfächer: erste Spalte von oben nach unten; anschließend zweite Spalte von oben nach unten; usw.

## Bildablage

Unbearbeitete Nutzerfotos werden unter `bilder/originale/` archiviert; generierte Visualisierungen separat unter `bilder/generiert/`. Jede Aufnahme wird in `daten/fotos.csv` referenziert. **Kein Upload persönlicher Bilder, solange das Repository öffentlich ist.**
