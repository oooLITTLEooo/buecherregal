# Arbeitsprotokoll – Neuaufnahme

## 2026-11-06 – Verbindlicher Neustart für den neuen Chat

- GitHub-Repository `oooLITTLEooo/buecherregal` bleibt **public**, bewusst gewählt.
- Die eigentliche Bildbestandsanalyse soll **ausschließlich aus dem zum Start des neuen Chats tatsächlich vorhandenen Git-Dateibestand** erfolgen.
- Der Nutzer führt den Foto-Upload selbst durch und wird ihn vor dem Start des neuen Chats abschließen.
- Vorherige, aus der Unterhaltung abgeleitete Buchlisten, Fotozuordnungen, Regalfachzahlen und vorläufige Erkennungen werden **nicht übernommen**.
- Die CSV-Dateien für Fotos, Regalfachstatus und Bücher wurden daher als **leere Vorlagen** zurückgesetzt.
- Alte Projektstände bleiben in der Git-Historie, sind aber für die neue Erfassung **nicht maßgeblich**.
- Verbindlicher Arbeitsauftrag: `docs/NEUER_CHAT_BESTANDSANALYSE.md`.
- Der neue Chat soll (1) Git-Repositorium und Fotos prüfen, (2) tatsächliche Dubletten dokumentiert entfernen, (3) Fotos nach den realen Fächern sortieren und umbenennen, (4) fehlende oder ungenügende Ansichten identifizieren und (5) erst danach alle Bücher anhand der Git-Originalbilder inventarisieren.
- Keine Fotolöschungen, Bildumbenennungen oder Buchanalysen in diesem Dokumentationsschritt vorgenommen.

## 2026-11-06 – Stufe 1: Git-Ablage der hochgeladenen Originalfotos

- Datenquelle: `main` zum Beginn der Arbeiten, Commit `29baf1dcc23781e5163c242c8991251a5c2ee417`.
- Rekursiver Git-Baum: 68 Einträge; 52 JPEG-Bilder direkt im Root gefunden. Die bisherigen Originale im Root waren noch unklassifiziert.
- Alle 52 Root-Bilder werden verlustfrei per bestehender Git-Blob-SHA nach `bilder/originale/` verschoben; Dateinamen und Bytes bleiben identisch.
- `bilder/umbenannt/` wird als getrennte Ablage der später **nach Bildinhalt** bestimmten Regalpositionskopien vorbereitet. Zunächst **keine Positionsnamen**, da der Bildinhalt noch nicht geprüft ist.
- `daten/fotos.csv`: 52 initiale Foto-IDs, ursprüngliche Git-Pfade, neue Pfade, Größen und Git-Blob-SHAs. SHA-256, Auflösung, EXIF, visueller Vergleich, Gesamtübersichtszuordnung und Buchinventar sind **noch offen**; Git-Blob-SHA ist nicht die SHA-256-Prüfsumme.
- In diesem Schritt keine Fotos nach scheinbar ähnlichen Dateinamen entfernt. 0 byteidentische Git-Blob-SHA-Dopplungen innerhalb der Root-Fotos festgestellt.
- Abweichung von der bisherigen Übergabe präzisiert: Originaldateinamen erhalten, positionsbezogene Benennung ausschließlich über Kopien in `bilder/umbenannt/`.

## 2026-11-06 – CSV-Reparatur vor Bildanalyse

- Der erste GitHub-Actions-Lauf schlug wegen eines unescaped Semikolons im Feld notizen der initialen daten/fotos.csv fehl. Das Semikolon verschob die erwartete Git-SHA-Spalte.
- GitHub Actions hat direkt mit git hash-object und git ls-files --stage die Unveraendertheit des ersten JPEG bestaetigt.
- Die CSV wurde anhand des aktuellen Git-Baums mit exakt 13 Feldern je Zeile neu aufgebaut, alle 52 Foto-IDs beibehalten, Originalpfade/Blob-SHAs verifiziert. Keine Originalfotos veraendert.
- Erneuter technischer Analyselauf nach Reparatur angestossen.

## 2026-11-06 – Erfolgreiche technische und visuelle Fotoprüfung

- GitHub Actions hat alle 52 Originalfotos erfolgreich geöffnet und SHA-256, Git-Blob-SHA, JPEG-Abmessungen, EXIF und dHash in daten/fotos.csv eingetragen. 0 Lesefehler.
- Vier Kontaktbögen und 52 Foto-Vorschauen aus den Git-Originalen generiert und in Git dokumentiert.
- FOTO0001 ist Gesamtübersicht: acht Spalten, acht Fach-Ebenen. FOTO0002–FOTO0052 folgen in den aufgenommenen Fachreihen.
- Alle 52 positionsbezogen benannten Kopien als bestehende Git-Blobs ohne erneute Kodierung angelegt; 52 von 52 Kopie-Hashes nach Git-Push geprüft.
- DHash-Kandidat FOTO0021/FOTO0033 visuell als verschiedene Bücher und verschiedene Fächer erkannt; beide erhalten.
- Mapping in daten/fotos.csv und Fachstatus für alle 64 Fachpositionen in daten/fachstatus.csv aktualisiert.
- Fehlende mögliche Buchdetails: 8-1, 8-2; 7-8 wegen Verdeckung zu prüfen. Keine physische oder geplante alphabetische Umsortierung.

## 2026-11-06 – Beginn der physischen Buchexemplar-Erfassung

- In den Bildvorschauen FOTO0002 bis FOTO0005 wurden 59 vorläufige einzelne Buchrücken in Reihenfolge erfasst.
- 18 Angaben sind unsicher oder offen und brauchen den Feinabgleich der Originalauflösung.
- Keine unsichtbaren Exemplare erfunden; jedes erfasste Buch enthält die Originalfoto-Referenz.
- Die restlichen Detailbilder und die fehlenden Fachaufnahmen sind weiter offen, siehe docs/inventur_fortschritt.md.

## 2026-11-06 – Korrektur frueherer Vorschaufehler aus Originalaufloesung

- Native Ausschnitte von FOTO0002 bis FOTO0005 visuell neu geprueft.
- 22 zuvor fehlerhafte oder unvollstaendige Angaben im Inventar der Faecher 1-5 bis 1-8 korrigiert. 2 unklare Positionen verbleiben.
- Bestehende Buch-IDs, Fachpositionen und Originalfoto-Referenzen erhalten. Git-Historie bewahrt alle alten Lesungen.

## 2026-11-06 – Erfassung 2-5 bis 2-8

- Native Originalausschnitte FOTO0010–FOTO0013 visuell geprüft. 80 neue Datensätze, 11 unsicher, Gesamtstand 229.
- Keine Originalfotos geändert oder alphabetische Umsortierung begonnen.
