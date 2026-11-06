# Bücherregal – Projektstatus und Einstieg

Repository: **[oooLITTLEooo/buecherregal](https://github.com/oooLITTLEooo/buecherregal)**  
Sichtbarkeit: **public** (ausdrücklicher Wunsch des Eigentümers)  
GitHub ist **Single Source of Truth**. Arbeitsvorgabe: **Git sync → Änderungen/Skript → Git sync → Analyse**.

## Wichtig: Nächster Arbeitsabschnitt in einem NEUEN CHAT

**[Vollständige Übergabe und verbindlicher Prüfauftrag: docs/NEUER_CHAT_BESTANDSANALYSE.md](docs/NEUER_CHAT_BESTANDSANALYSE.md)**

Der nächste Chat soll erst das Repository und sämtliche tatsächlich abgelegten Fotos prüfen, dann Dubletten bereinigen, Fotos anhand der Regalfächer ordnen und umbenennen, fehlende Fächer ermitteln und **erst danach** alle Bücher anhand der Git-Fotos gründlich identifizieren.

**In diesem Chat erfolgt keine Löschung oder Umbenennung von Git-Bildern und keine neue vollständige Buchanalyse.**

## Status – geprüft am 2026-11-06

| Thema | Ist-Stand |
|---|---|
| Fotos im Gespräch | 43 (1 Gesamtansicht + 42 Regalfotos) |
| Vorläufig fotografierte Regalfächer | 1-5 bis 1-8; 2-1 bis 2-8; 3-1 bis 3-8; 4-1 bis 4-8; 5-1 bis 5-8; 6-1 bis 6-6 |
| Noch abzugleichen | 6-7, 6-8 und alle weiteren vorhandenen Fächer/Spalten |
| Bilder nachweislich in `main` | **0** (im gesamten rekursiven GitHub-`main`-Baum am Prüftag keine Bilddatei) |
| Vom Nutzer gemeldeter Upload | Alle Fotos in voller Auflösung; tatsächlichen Speicherort im neuen Chat erneut überprüfen |
| Vorläufige Buchpositionen | 362 |
| Noch offene/prüfbedürftige Buchpositionen | 68 |
| Offene Nutzer-Erinnerungen | `3.5 noch`, `2.5 noch`, `1.5 noch offen` |

**Wichtig:** Der Nutzer hat einen Foto-Upload bestätigt. Die direkte GitHub-Prüfung ergab zu diesem Zeitpunkt jedoch nur die Datei `bilder/originale/.gitkeep`. Kein Upload wurde als erfolgt behauptet; `upload_status=ausstehend` in `daten/fotos.csv` bleibt richtig, bis die Originaldateien in Git verifiziert sind. Es gibt nur den Branch `main`. Wenn die Fotos anderswo hochgeladen wurden, muss deren Ablage zuerst gefunden werden.

Die **43 unveränderten Chat-JPEG-Dateien** sind außerdem in `buecherregal_fotos_bis_6-6_2026-11-06.zip` als Chat-Artefakt gesichert, inklusive Prüfsummenmanifest; **nicht** als GitHub-Datei. Für einen autorisierten Import aus einem lokalen Git-Clone steht `scripts/import-fotos.sh` bereit.

## Regalnummerierung

- `1-5`: erste Spalte von links, fünftes Fach von oben
- `2-1`: zweite Spalte, oberstes Fach
- `6-6`: sechste Spalte, sechstes Fach von oben
- Einzelbücher innerhalb eines Fachs von **links nach rechts** zählen
- Die Anordnung bleibt zunächst **Ist-Stand**, keine vorzeitige alphabetische Umordnung

## Projektdaten

- `daten/fotos.csv`: Foto-IDs, Regalzuordnung, Dateinamen, SHA-256, Uploadstatus
- `daten/fachstatus.csv`: Fach für Fach: leer, fotografiert oder noch abzugleichen
- `daten/buecher.csv`: vorläufiges Buchinventar mit ursprünglichen Buchpositionen
- `daten/offene_punkte.csv`: Nutzer-Erinnerungen
- `bilder/originale/`: Soll-Ablage unveränderter Originalfotos
- `bilder/generiert/`: Ablage später erzeugter Grafiken
- `docs/uebersicht.md`: Regalübersicht
- `docs/standorte.md`: Nummerierung und Sortierkonvention
- `docs/protokoll.md`: Chronik und Statusprüfungen
- `docs/NEUER_CHAT_BESTANDSANALYSE.md`: **vollständiger Arbeitsauftrag für den nächsten Chat**
- `scripts/import-fotos.sh`: geprüfter lokaler Git-Import aus einer ZIP-Sicherung

## Ziel

Nach Verifizierung der Fotos jedes **physische** Buch mit Autor, Titel, Fachposition und Links zum Originalfoto inventarisieren. Unsicherheiten dokumentieren statt erraten. Danach alphabetisch nach **Nachname des Autors (A–Z)** sortieren: spaltenweise von links nach rechts, innerhalb jeder Spalte von oben nach unten.

## Erinnerungen – bis zur Klärung am Ende der Antworten nennen

- **3.5 noch**
- **2.5 noch**
- **1.5 noch offen**

Fächer 3-5, 2-5 und 1-5 wurden bereits fotografiert. Der Wortlaut beschreibt offene Nutzeraufgaben; nicht automatisch von „fehlenden Fotos“ ausgehen.
