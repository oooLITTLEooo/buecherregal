# Fortsetzung Bücherregal nach Chat-Unterbrechungen – 06.11.2026

## Verbindliche Datenquelle und Git-Stand

- Repository: `oooLITTLEooo/buecherregal`, Branch `main`.
- Ausgangs-HEAD bei der Bestandsprüfung: `7917628ea5d054c72a954a9d51dab5fe9954ded6` (Commit-Zeitpunkt 2026-11-06 18:02:19 UTC).
- Ausschließlich der aktuelle Git-Dateibestand ist für Bücher und Originalbilder maßgeblich.
- Diese Datei ist eine Zustandsnotiz **ohne Änderungen an Fotos, Bucheinträgen, IDs oder Positionen**. Vor Fortsetzung erneut den Git-HEAD prüfen.

## Verifizierter Ist-Stand

- 52 Original-JPEGs in `bilder/originale/`, dazu 52 byteidentische, nach Position benannte Kopien unter `bilder/umbenannt/` einschließlich der Gesamtansicht. Die Kopie- und Original-Git-Blob-SHAs stimmen bei allen 52 Zuordnungen aus `daten/fotos.csv` überein.
- 0 byteidentische Fotodubletten innerhalb der 52 Originale; ein früherer dHash-Ähnlichkeitskandidat (FOTO0021/FOTO0033) erwies sich als **kein** Duplikat.
- Originalauflösung laut `daten/fotos.csv`: 8160 × 4590 Pixel, alle 52 technisch lesbar.
- Regal: 8 Spalten à 8 Ebenen, zusammen 64 Fachpositionen. Detailaufnahmen für 51 Fachpositionen vorhanden.
- 8-1 und 8-2: sichtbare Bücher, aber keine Detailfotos. 7-8: verdeckt, zusätzliche Sichtprüfung erforderlich. 8-3 bis 8-8 aus Gesamtbild als leer/unklar notiert, vor Ort bestätigen.
- `daten/buecher.csv`: 1048 einzelne **vorläufige** Buchdatensätze, alle Buch-IDs eindeutig; 941 `lesbar`, 65 `pruefen`, 42 `offen`. Alle 51 fotografierten Fächer wurden mindestens einmal erfasst.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: ursprüngliche Prüfbasis 159 IDs. Davon 52 als `korrigiert_und_lesbar` abgeschlossen, 104 weiterhin nach Hochauflösungsprüfung unsicher, 3 nur mit unzureichenden Bilddaten geprüft; somit 107 offen/prüfpflichtig.
- Die fortlaufenden Buchpositionen innerhalb der Fächer und der tatsächliche Exemplarumfang sind noch nicht endgültig verifiziert. Keine alphabetische Umsortierung begonnen.

## Bilddaten und technische Risikostellen

- 204 native, aus 51 Detailfotos erzeugte Ausschnitte sind als `.jpg.base64.txt` unter `daten/bildanalyse/fullres/` versioniert. Zusammen ca. 170 MB textkodierte Ausschnitte; mit Vorschau- und Kontaktbogen-Dateien insgesamt 260 `.base64.txt`-Dateien mit ca. 178 MB.
- Das logische Dateivolumen des Git-Baums beträgt ca. 879 MB (inklusive Original-/Positionskopien; Git kann gleiche Bildbytes intern deduplizieren).
- Im zweiten Hochauflösungs-Prüfblock ließen sich die Teile 3 und 4 von `FOTO0042` (Fach 6-5) nicht als Bild dekodieren/ausliefern. Das Originalbild ist im Git vorhanden. Drei verbliebene Prüffälle sind davon betroffen. Kein Beleg dafür, dass das Original beschädigt ist.
- Der letzte GitHub-Actions-Lauf `Foto-Vollaufloesungs-Ausschnitte` (#12) wurde erfolgreich abgeschlossen. Aus dem Repo lässt sich **kein App-Absturzgrund** ableiten.
- Dass die Chat-App beim Arbeiten mit vielen hochauflösenden Ausschnitten oder sehr großen Base64-Textdateien hängen bleibt, ist **eine plausible, nicht belegte Hypothese**. App-Fehler-/Absturzlogs sind hier nicht verfügbar.

## Sinnvolle direkte Fortsetzung – kleine, überprüfbare Batches

1. Vor jeder Änderung Git-HEAD und Inventar-/Foto-Zuordnung prüfen; nur tatsächlich im Git vorhandene Fotos verwenden.
2. Zuerst die drei Prüffälle im Fach 6-5 aus `FOTO0042` (insbesondere Teile 3/4) erneut bearbeiten. Statt der alten rekodierten Base64-Texte möglichst direkte/verlustfreie **kleine Bildausschnitte** aus dem Original erzeugen und als echte Bilddateien bereitstellen, ohne das Original zu ändern.
3. Anschließend die 104 nach einmaliger Hochauflösungsprüfung noch unsicheren Fälle fächerweise in überschaubaren Gruppen bearbeiten; Schwerpunkte nach Anzahl verbleibender Unklarheiten: 3-1 (8), 4-7 (6), 5-6 (6), 5-3 (5).
4. Wenn ein Rücken auch nach gezieltem Ausschnitt verdeckt bleibt: als `offen`/`pruefen` belassen und benötigtes Zusatzfoto präzise notieren. Keine Titel raten.
5. Nach jeder abgeschlossenen kleinen Gruppe Buch-ID, Fach, Position, Fotoreferenz und Status erhalten; `daten/buecher.csv`, `daten/bildanalyse/feinpruefung_unsicher.csv` und Protokoll synchronisieren, erneut auf Konsistenz prüfen.
6. Noch aufzunehmende Fotos: 8-1, 8-2 und eine Überblicks-/Detailansicht von 7-8; spätere Prüfung 8-3 bis 8-8. Bis dahin keine abschließende Bestandszahl und keine alphabetische Umsortierung.

## Verweise

- `docs/NEUER_CHAT_BESTANDSANALYSE.md` – verbindliche Gesamtarbeitsregeln
- `docs/inventur_fortschritt.md` – Inventurhistorie
- `docs/feinpruefung_unsicher_20261106.md` – Einzelfallnachweise
- `daten/bildanalyse/feinpruefung_unsicher.csv` – Status der 159 Prüffälle
- `daten/fotos.csv`, `daten/fachstatus.csv`, `daten/buecher.csv` – aktuelle Primärdaten
