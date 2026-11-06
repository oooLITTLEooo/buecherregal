# Bilder und Dateinamen

Repository-Sichtbarkeit am 2026-11-06 als **public** bestätigt und vom Nutzer ausdrücklich als beabsichtigt bezeichnet. Originalfotos werden nach erfolgreichem Import öffentlich einsehbar sein.

## Namenskonvention

- Übersichtsfoto: `Regal_Gesamt.jpg`
- Einzelnes Fach: `Regal_1-4.jpg` = **erste Spalte von links, viertes Fach von oben**
- Weitere Aufnahme desselben Fachs: `Regal_1-4_02.jpg`, `Regal_1-4_03.jpg`, usw.
- Wenn mehrere nebeneinanderliegende Fächer sichtbar sind, erst nach eindeutiger Zuordnung benennen; bei Unsicherheit eine vorläufige Bild-ID verwenden und nicht falsch einsortieren.
- Bildendung muss dem tatsächlichen Originalformat entsprechen (`.jpg`, `.png`, `.webp`, …); keine Formatkonvertierung nur zum Umbenennen.

`bilder/originale/` enthält unveränderte Nutzerbilder (gleiche Dateibytes, nur sinnvoller Dateiname). `bilder/generiert/` enthält neu erzeugte Visualisierungen.

Alle Dateien werden in `daten/fotos.csv` dokumentiert. Das dortige Feld `upload_status` unterscheidet `ausstehend` von `im_git`. Nur nach erfolgreichem Upload und Prüfung des Ablageorts als `im_git` kennzeichnen.

## Wichtig

Vorläufige Fotobezeichnungen sind kein Beweis, dass eine Bilddatei tatsächlich im Repository liegt. Insgesamt 43 Originalfotos liegen im Chat und in einem SHA-256-geprüften Original-ZIP (`buecherregal_fotos_bis_6-6_2026-11-06.zip`) vor. Der Nutzer meldet einen Upload aller Fotos in voller Auflösung. Der rekursiv geprüfte GitHub-Dateibaum von `main` enthielt am 2026-11-06 jedoch keine JPEGs/PNGs, nur `.gitkeep` unter `bilder/originale/`. Daher ist der tatsächliche Speicherort noch zu überprüfen. Bis zum Nachweis gilt `upload_status=ausstehend`. Der vorgesehene lokale Git-Import erfolgt gegebenenfalls mit `scripts/import-fotos.sh` anhand der SHA-256-Prüfsummen. Der Import erfolgt mit `scripts/import-fotos.sh` anhand der SHA-256-Prüfsummen.

## Neuer Chat

Die vollständige Bildbestandsprüfung, Dublettenbereinigung und Umbenennung werden **nicht hier** durchgeführt, sondern nach der Übergabe in `docs/NEUER_CHAT_BESTANDSANALYSE.md` im neuen Chat. Vor dem Löschen oder Umbenennen Bildbestand, Provenienz und Sicherung nachweisen.
