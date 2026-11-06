# Übergabe an neuen Chat – Bestandsanalyse Bücherregal

**Stand:** 2026-11-06  
**GitHub:** https://github.com/oooLITTLEooo/buecherregal  
**Standardbranch:** `main`  
**Sichtbarkeit:** `public` – vom Nutzer ausdrücklich gewünscht.  
**Arbeitsregel:** GitHub ist die Single Source of Truth; **immer Git: sync → Skript/Änderung → sync → Analyse**.

## Auftrag für den NEUEN Chat

Der Nutzer wünscht folgende Reihenfolge:

1. **Repository vollständig analysieren**: Branches, Verzeichnisbaum, tatsächliche Originalfotos, README, CSV-Inventare, Foto-Manifest, Protokoll und Git-Historie.
2. **Doppelte Fotos identifizieren und bereinigen**: erst identische Dateien über SHA-256, danach visuell fast identische Aufnahmen durch Bildvergleich. Bei Zweifeln nicht automatisch löschen; aussagekräftigste Aufnahme bewahren. Jede Löschung vorher dokumentieren und sicherstellen, dass keine einzigartige Buchinformation verloren geht. Git-Historie/Backup als Rückweg erhalten.
3. **Fotos ordnen und umbenennen**: `Regal_Gesamt.jpg` sowie `Regal_<Spalte>-<Fach>.jpg`; bei mehreren sinnvollen Ansichten z. B. `Regal_3-5_02.jpg`. Dateien in `bilder/originale/`; `git mv` bzw. GitHub-Commits benutzen. Umbenennung nur anhand gesicherter Fachzuordnung, nicht bloß nach Kameranummer. `daten/fotos.csv` und Fotoverweise in `daten/buecher.csv` konsistent nachführen.
4. **Abgleich auf Vollständigkeit**: Foto-Standorte gegen `daten/fachstatus.csv` und Gesamtübersicht prüfen. Leere Fächer als leer markieren, nicht als fehlende Fotos. Pro tatsächlich belegtem Fach mindestens eine ausreichend lesbare Aufnahme. Konkrete fehlende Fächer mit Nummer melden; Kameranummernlücken sind für sich allein kein Beweis fehlender Regalfotos.
5. **Erst danach vollständige Analyse aller in Git gespeicherten Fotos**: jeden Buchrücken möglichst genau identifizieren (Autor, Titel, ggf. Band und Edition). Physische Exemplare einzeln erfassen, auch echte doppelte Bücher. Reihenfolge von **links nach rechts** innerhalb des Faches dokumentieren. Unleserliche Angaben als `offen`/`pruefen` kennzeichnen statt zu raten. Nicht davon ausgehen, dass die 362 bereits erfassten Einträge korrekt oder vollständig sind; anhand der Originale verifizieren.
6. Ergebnisse und Prüfprotokolle **ins Git committen**. Erst nach kompletter Bestandsanalyse einen separaten alphabetischen Sortierplan vorbereiten. **Keine physische Umsortierung ohne neue Nutzeranweisung.**

## Aktueller geprüfter GitHub-Befund

Am **2026-11-06** wurden das Repository und seine Branches sowie der rekursive Dateibaum über die GitHub-Verbindung geprüft:

- Es existierte **nur der Branch `main`**.
- `bilder/originale/` enthielt nur `.gitkeep`. Im gesamten rekursiv abgefragten `main`-Baum waren **keine JPG/JPEG/PNG/WEBP/HEIC-Bilddateien**.
- Der Nutzer berichtet, **alle Fotos in voller Auflösung hochgeladen zu haben**. Das konnte im überprüften Branch/Repository zu diesem Zeitpunkt **noch nicht bestätigt** werden. Bei Beginn im neuen Chat **erneut prüfen**, ob inzwischen Bilder hinzugekommen sind oder sie an anderer Stelle abgelegt wurden. Nicht widerspruchslos als in Git vorhanden behandeln.
- Die GitHub-Textdateien sind vorhanden, insbesondere `daten/buecher.csv`, `daten/fotos.csv`, `daten/fachstatus.csv`, `daten/offene_punkte.csv`.
- **43 Chat-Aufnahmen** wurden verzeichnet: **1 Übersichtsfoto + 42 Fachfotos**.
- Die Original-JPEG-Daten der 43 Chat-Aufnahmen wurden für einen möglichen Import **ohne Rekodierung** im Chat-Archiv `buecherregal_fotos_bis_6-6_2026-11-06.zip` gesichert (43 Dateien, pro Bild SHA-256 im enthaltenen `FOTO_MANIFEST.csv`). Das Archiv liegt als Chat-Artefakt vor, **nicht als bestätigte Datei im GitHub-Repository**.
- Die 43 `daten/fotos.csv`-Einträge tragen korrekterweise `upload_status=ausstehend`. Status erst nach Abgleich mit echten Git-Dateien aktualisieren.

## Bislang abgebildete Fächer (vorläufig)

- `1-1` bis `1-3`: laut Übersicht leer; `1-4`: Lampe / kein erkennbarer Bücherbestand.
- `1-5` bis `1-8`: Detailaufnahmen vorhanden.
- `2-1` bis `2-8`: Detailaufnahmen vorhanden.
- `3-1` bis `3-8`: Detailaufnahmen vorhanden.
- `4-1` bis `4-8`: Detailaufnahmen vorhanden.
- `5-1` bis `5-8`: Detailaufnahmen vorhanden.
- `6-1` bis `6-6`: Detailaufnahmen vorhanden.
- **Abgleich noch offen:** `6-7`, `6-8` und die übrigen Spalten (auf dem Übersichtsbild schätzungsweise insgesamt acht vertikale Spalten). Die endgültige Zahl und Belegung der Fachpositionen sind erst nach Fotoabgleich festzulegen.

## Inventarqualität bisher

- `daten/buecher.csv`: 362 **vorläufige** Buchpositionen aus 18 früher analysierten Fächern.
- Davon 68 als `offen` oder `pruefen` gekennzeichnet.
- Die nach dem vereinbarten Wechsel auf **„Bilder zuerst in Git“** erhaltenen Fächer sind noch **nicht** vollständig buchweise erfasst.
- Im Folgechat alle 362 vorhandenen Zeilen gegen die Originalfotos validieren; danach die fehlenden Fächer vervollständigen. Einträge nicht unbesehen als endgültige Fakten übernehmen.

## Offene Nutzer-Erinnerungen – unbedingt erhalten

Diese Wortlaute stammen vom Nutzer und dürfen **nicht** als Behauptung eines fehlenden Fotos missverstanden werden:

- **`3.5 noch`** → in `daten/offene_punkte.csv`, offen; Fach 3-5 ist bereits fotografiert.
- **`2.5 noch`** → in `daten/offene_punkte.csv`, offen; Fach 2-5 ist bereits fotografiert.
- **`1.5 noch offen`** → in `daten/offene_punkte.csv`, offen; Fach 1-5 ist bereits fotografiert.

Bis zur Klärung diese Erinnerungen **am Ende der Antworten wiedergeben**.

## Qualitäts- und Sicherheitsregeln

- Nie Originalbilder ohne expliziten Grund bearbeiten, verkleinern oder durch andere Dateibytes ersetzen.
- Vor **Löschungen** Dublettenprotokoll mit mindestens Pfad, Dateigröße, SHA-256, verglichenem Inhalt und Entscheidung erstellen; im Zweifel nicht löschen.
- Ähnliche Aufnahmen können unterschiedliche Buchrücken sichtbar machen und daher **keine** überflüssigen Dubletten sein.
- Wenn noch keine Fotos im Repository sind, **nicht mit der vollständigen Buchanalyse beginnen**; erst die Bildarchivierung/Verfügbarkeit beheben und verifizieren.
- Das Repository ist öffentlich, die Tatsache ist **gewollt**; nicht wieder eigenmächtig auf privat stellen.
- Nach jeder Git-Änderung die resultierenden Dateien verifizieren, nicht bloß Erfolg vermuten.
- Der Nutzer möchte die eigentliche Bestandsanalyse ausdrücklich **in einem neuen Chat** starten.

## Datenformat/Bezeichner

- Standort `X-Y`: Spalte X von links, Fach Y von oben; `3-5` = Spalte 3, fünftes Fach von oben.
- Foto-IDs `F0001`…`F0043` in `daten/fotos.csv`; Fotoposition `3-5` sollte in `standort` stehen.
- Buch-IDs `B0001`…`B0362` und Referenz-Foto-ID in `daten/buecher.csv`; keine IDs für unterschiedliche Exemplare wiederverwenden.
- Beim Fotografieren aufgenommene Anteile des oberen/unteren Nachbarfachs **nicht** als separate Bücher des aktuellen Fachs erfassen.
- Nachnamen für spätere alphabetische Ordnung (A–Z) vorsehen, zunächst aber ursprüngliche Standorte unverändert erfassen.
