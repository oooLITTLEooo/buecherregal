# Bildablage – Stand 2026-11-06

## Verbindliche Ordner

- `bilder/originale/`: Die vom Nutzer hochgeladenen JPEG-Dateien, **unverändert**, mit ursprünglichen Dateinamen.
- `bilder/umbenannt/`: Jeweils eine **byteidentische Kopie** aus `bilder/originale/`, nach Prüfung der tatsächlichen Regalposition benannt, z. B. `Regal_Gesamt.jpg`, `Regal_1-5.jpg` oder `Regal_1-5_02.jpg`.
- `bilder/generiert/`: Später erzeugte Skizzen/Grafiken; niemals als Originalbeleg verwenden.

Die Originale nicht umbenennen oder neu kodieren. Ein Foto darf erst in `bilder/umbenannt/` abgelegt werden, wenn die Regalposition aus dem Bildinhalt gesichert wurde. Keine `PXL`-Zeitstempel zur Positionsbestimmung verwenden.

## Nachweis

`daten/fotos.csv` enthält pro Foto die stabile ID, den ursprünglichen Git-Pfad, den aktuellen Git-Pfad und die Git-Blob-SHA. Die Spalten `sha256`, Bildauflösung, EXIF, pHash sowie Regalzuordnung werden erst nach Prüfung der vollständigen Bildbytes befüllt. Quelle ist ausschließlich der tatsächliche Git-Stand.

Eine angeblich doppelte Aufnahme nur nach Verifikation entfernen. Git-Historie als Wiederherstellungsmöglichkeit erhalten.

Siehe `docs/NEUER_CHAT_BESTANDSANALYSE.md`.
