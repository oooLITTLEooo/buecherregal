# Übergabe für neuen Chat: Bestandsanalyse Bücherregal

## Projekt und verbindlicher Datenbestand

- **GitHub-Repository:** https://github.com/oooLITTLEooo/buecherregal
- **Sichtbarkeit:** `public` ist ausdrücklich gewünscht.
- **Single Source of Truth:** ausschließlich die **zum Start des neuen Chats tatsächlich im Git-Repository vorhandenen Dateien**, insbesondere die Originalfotos. Der Upload wird laut Nutzer **vor Beginn des neuen Chats abgeschlossen** sein.
- **Keine Übernahme von Fotos, Bucherkennungen, Bildnummern, Regalzuordnungen, Inventarständen oder sonstigen Annahmen aus früheren Chat-Nachrichten.** Den Bestand ohne Vorannahmen aus Git neu ermitteln.
- Frühere, nicht anhand des aktuellen Git-Fotobestands überprüfte Daten gelten **nicht** als Inventarnachweis. Aus dem aktuellen Git-Bestand eine neue, überprüfbare Bestandsaufnahme erstellen.

## Arbeitsauftrag – in genau dieser Reihenfolge

### 1. Git-Repository und tatsächlich vorhandene Fotos prüfen

1. Repository-Status, Standardbranch, gegebenenfalls andere Branches, Git-Historie und Verzeichnisstruktur prüfen; **Git-Sync** vor Arbeitsbeginn.
2. **Alle Bilddateien im Repository rekursiv** finden, unabhängig davon, wie sie aktuell heißen und in welchen Unterordnern sie liegen. Unterstützte Formate und mögliche Abweichungen ermitteln; nicht nur `bilder/originale/` durchsuchen.
3. Eine vorläufige Fotoliste aus **tatsächlich existierenden Dateien** erstellen: ursprünglicher Git-Pfad, Format, Dateigröße, Auflösung, SHA-256, ggf. EXIF, Erfassungs-/Prüfstatus.
4. Verfügbarkeit und Lesbarkeit der hochgeladenen Bilder in voller Auflösung verifizieren. Wenn der Upload wider Erwarten nicht vollständig oder der Speicherort unbekannt ist, die konkreten Lücken dokumentieren; **keine imaginären Bilder ergänzen**.
5. Das Gesamtübersichtsfoto ermitteln und den wirklichen Regalaufbau daraus ableiten. Es gibt keine vorausgesetzte Zahl von Spalten oder Fächern.

### 2. Doppelte Fotos erkennen und bereinigen

1. **Byte-identische Dubletten** per SHA-256 finden.
2. **Visuell ähnliche und mehrfach aufgenommene Fächer** mittels Bildvergleich (z. B. perceptual hash) prüfen. Ähnliche Bilder können zusätzliche lesbare Buchrücken zeigen und müssen deshalb nicht überflüssig sein.
3. Prüfprotokoll mit allen Kandidaten, Bildpfaden, Prüfsummen und Entscheidung anlegen.
4. Nur **nachweislich überflüssige Dubletten** aus dem aktiven Bestand entfernen; möglichst aussagekräftiges Original behalten. Unklare Fälle erhalten und kennzeichnen. Veränderungen nachvollziehbar committen; die Git-Historie als Wiederherstellungsmöglichkeit bewahren.

### 3. Fotos sortieren und eindeutig umbenennen

1. Regalfächer aus der Übersicht **spaltenweise** nummerieren: links beginnend, innerhalb jeder Spalte von oben nach unten. Beispiel: `1-5` = erste Spalte, fünftes Fach von oben.
2. Jede Aufnahme anhand ihres tatsächlichen Bildinhalts einem Fach zuordnen; ursprüngliche Dateinamen sind **kein** sicherer Beleg für die Fachposition.
3. Einheitliche Namen **nur für die Kopien unter `bilder/umbenannt/`**: `Regal_Gesamt.jpg`, `Regal_1-5.jpg`, bei nützlicher zweiter Ansicht `Regal_1-5_02.jpg` usw. Die **Originalbilddaten und Originaldateinamen** in `bilder/originale/` unverändert lassen; keine unnötige Neuspeicherung, Konvertierung, Skalierung oder Kompression.
4. Verbindliche Präzisierung vom 06.11.2026: Originalfotos zunächst **ohne Umbenennung** aus dem Root nach `bilder/originale/` verlagern; nach gesicherter Bild-zu-Fach-Zuordnung jeweils eine byteidentische Kopie mit Positionsnamen in `bilder/umbenannt/` anlegen. Unbekannte Positionen nicht raten. Bestehende Dateien niemals überschreiben. Vorher-Nachher-Mapping in `daten/fotos.csv` dokumentieren und nach dem Push verifizieren.

### 4. Vollständigkeitsabgleich

1. Die anhand der Gesamtübersicht **tatsächlich vorhandenen** Regalspalten und Fächer bestimmen.
2. Bild für Bild abgleichen: Welche Fächer sind eindeutig dokumentiert, welche nur teilweise und welche fehlen? Mehrfachbilder nicht als zusätzliche Fächer zählen.
3. Leere Fächer und Fächer ohne Bücher separat kennzeichnen, nicht als fehlendes Buchfoto behandeln.
4. Konkrete fehlende oder schlecht lesbare Fächer **mit Standortnummer** in `daten/fachstatus.csv` aufführen. Bei Unklarheiten exakt sagen, welches Foto ergänzend gebraucht wird.
5. Keine pauschalen Annahmen über Fachanzahl, ursprüngliche Reihenfolge oder bisherigen Erfassungsfortschritt übernehmen.

### 5. Vollständige Buchbestandsanalyse aus Git-Fotos

**Erst wenn die Bildablage bereinigt, nummeriert und auf Vollständigkeit geprüft ist:**

1. Jedes Fach in voller Originalauflösung ansehen, bei Bedarf Bildbereiche vergrößern.
2. Für **jedes physische Buchexemplar** Autor (Nachname, Vorname), exakten Titel, Original-Standort und Position **von links nach rechts** erfassen. Echte doppelte Bücher sind getrennte Exemplare.
3. Verdeckte, unscharfe oder unlesbare Buchrücken nicht raten: `offen`/`pruefen` samt genauer Fundstelle markieren. Bei Bedarf ergänzendes Detailfoto eines konkret benannten Faches anfordern.
4. Quellbeleg zu jedem Datensatz in `daten/buecher.csv` bzw. mittels stabiler Foto-ID und Git-Pfad dokumentieren. Bücher aus angrenzenden Fächern, die am Rand eines Bildes zu sehen sind, nicht doppelt erfassen.
5. Abschlusskontrolle pro Fach: Anzahl und Reihenfolge der Bücher gegen die Bilddatei prüfen; summarische Statistik zu Beständen, Unsicherheiten, fehlenden Ansichten und echten Dubletten erstellen.

### 6. Git-Dokumentation und Ergebnis

- Alle Scripts, Inventare, Fotozuordnungen, Prüfprotokolle und Entscheidungen im Repository versionieren.
- Arbeitsregel: **Git sync → Skript/Änderung → Git sync → Analyse und Ergebnisprüfung**; `main` nicht unnötig mit temporären Dateien verschmutzen.
- Vorhandene Datenfelder und CSV-Strukturen bei Bedarf anpassen, sofern konsistent und dokumentiert. **Keine alten Inventare blind übernehmen.**
- Abschließend einen geprüften **Ist-Bestand** und eine Liste eventuell noch fehlender/unklarer Fotos bereitstellen.
- **Noch keine physische oder geplante alphabetische Umsortierung durchführen.** Das spätere Ziel lautet alphabetisch nach **Nachnamen der Autoren A–Z**, spaltenweise von links nach rechts und innerhalb jeder Spalte von oben nach unten. Die Umsortierung erfolgt nur auf ausdrückliche weitere Anweisung.

## Kurzprompt zum Start im neuen Chat

> Starte die vollständige Bestandsanalyse von `oooLITTLEooo/buecherregal` gemäß `docs/NEUER_CHAT_BESTANDSANALYSE.md`. Mein Foto-Upload ist jetzt abgeschlossen. Verwende ausschließlich Dateien, die tatsächlich im GitHub-Repository liegen. Prüfe zuerst den vollständigen Bildbestand, entferne verifizierte Fotodubletten, ordne und benenne die Originalbilder nach den richtigen Regalfächern, ermittle fehlende Fotos und analysiere erst danach alle Bücher mit Autor, Titel und exakter ursprünglicher Position. Dokumentiere und synchronisiere alle Schritte über Git.
