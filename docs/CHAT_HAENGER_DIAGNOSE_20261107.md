# Wiederholte Bücher-Chat-Unterbrechungen – technische Bestandsprüfung (07.11.2026)

## Feststellbare Tatsachen

- `oooLITTLEooo/buecherregal` (`main`) enthielt bei der Prüfung **260** zusätzliche `.base64.txt`-Bilddateien mit insgesamt **178.317.140 Bytes** (rund **178,3 MB**), darunter 204 native Vollauflösungs-Ausschnitte. Dazu liegen 52 Original-JPEGs und 52 zugeordnete Positionskopien (einschließlich Gesamtbild) im Git.
- Die frühere Fortsetzungsdokumentation hält zeitweise nicht abrufbare FOTO0042-Ausschnitte fest; dies belegt **keine** Beschädigung des Originalfotos.
- Die genaue Ursache für Hänger in ChatGPT kann aus einem Git-Repository **nicht festgestellt** werden. App-seitige Absturz- oder Verbindungslogs liegen hier nicht vor. Lange Abläufe mit großen Base64-Texteingaben und vielen Bildern sind eine plausible **Hypothese**, nicht bewiesen.
- `README.md` hält fest, dass das Repository ausdrücklich als `public` gewünscht ist. Diese Einstellung wurde nicht verändert.
- Beim Fortsetzen am 07.11.2026 war ein Git-Objekt-Commit über die branch-ref-Aktualisierung technisch nicht publizierbar; die reguläre GitHub-Datei-API wurde für die tatsächlichen Dateiänderungen verwendet. Die branch-ref-Fehlermeldung ist **nicht** als Chat-Absturzursache zu interpretieren.

## Reduzierter Workflow

1. Vor jedem Fach den aktuellen `main`-Stand und nur die betroffenen CSV-Zeilen lesen.
2. Genau **ein Fach pro Benutzeraufforderung** bearbeiten, nur offene/prüfpflichtige Bücher.
3. Statt großer Bilddatenmengen ausschließlich einzelne vorhandene Ausschnitte aus dem Git laden.
4. Unsichtbare/verdeckt stehende Bände nicht erraten, stattdessen genau benötigtes Foto und eventuelle Zählunsicherheit protokollieren.
5. Änderungen im Git speichern und anschließend die aktuellen Zahlen, IDs und Dateien nachprüfen. Danach stoppen.

## Fortsetzungsstand

- Vor der Bearbeitung Fach 5-2: 1048 Datensätze, 983 lesbar, 27 prüfen, 38 offen.
- Nach Fach 5-2: 1048 Datensätze, 984 lesbar, 26 prüfen, 38 offen.
- B00599 durch FOTO0031 Teil 04 bestätigt; B00585 bleibt offen. **Nächstes Fach 5-3**.
