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
