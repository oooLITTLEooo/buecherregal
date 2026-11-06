# Bücherregal – Bestandsaufnahme und alphabetische Sortierung

**Repository:** https://github.com/oooLITTLEooo/buecherregal  
**Sichtbarkeit:** öffentlich (`public`), ausdrücklich gewünscht  
**Single Source of Truth:** ausschließlich der **jeweils aktuelle tatsächliche GitHub-Dateibestand**

## Neustart der Bestandsanalyse

Der Foto-Upload durch den Nutzer läuft noch und soll **vor Beginn des neuen Chats** abgeschlossen sein. Die frühere Erfassung ist **nicht maßgeblich**. Keine Fotoanzahlen, Regalfachzuordnungen, Erinnerungen, Buchinventare oder Bilddateien aus vorherigen Chat-Nachrichten übernehmen.

**Verbindlicher Einstieg und vollständiger Arbeitsauftrag:**  
[docs/NEUER_CHAT_BESTANDSANALYSE.md](docs/NEUER_CHAT_BESTANDSANALYSE.md)

## Geplante Reihenfolge

1. Repository und den tatsächlich vorhandenen Foto-Dateibestand vollständig prüfen.
2. Identische und visuell doppelte Fotos vergleichen und nach dokumentierter Prüfung überflüssige Dubletten bereinigen.
3. Originalfotos nach Regalfächern ordnen und eindeutig umbenennen.
4. Tatsächliche Regalstruktur und Vollständigkeit anhand des Gesamtbildes überprüfen; konkrete fehlende Fotos benennen.
5. **Erst dann** die Originalfotos in voller Auflösung auf einzelne Bücher analysieren und Autor, Titel, Fach und Position erfassen.
6. Alles versioniert in Git dokumentieren und anschließend überprüfen.

**Git-Arbeitsregel:** `sync → Skript/Änderung → sync → Analyse`.

## Standortkonvention

`Spalte-Fach`: von **links nach rechts** durch die Spalten, innerhalb jeder Spalte von **oben nach unten**. Beispiel: `1-5` bedeutet erste Spalte, fünftes Fach von oben. Die tatsächlich vorhandene Fach- und Spaltenzahl wird **erst aus den Fotos im Git** ermittelt.

Ziel der späteren physischen Umsortierung: **A–Z nach Autoren-Nachnamen**, entlang dieser Fachreihenfolge. Eine Umsortierung wird erst auf ausdrückliche neue Anweisung geplant.

## Projektstruktur

- `bilder/originale/` – Ablage der im Repository vorliegenden Originalfotos
- `bilder/generiert/` – später ggf. erzeugte Diagramme und Fotoskizzen
- `daten/fotos.csv` – aus dem aktuellen Git-Bestand neu zu erstellendes Foto-Inventar
- `daten/fachstatus.csv` – tatsächliche Regalfächer und Foto-Abdeckung
- `daten/buecher.csv` – nach der Bildprüfung frisch erfasste Buchexemplare
- `docs/standorte.md` – Nummerierung und Erfassungsregeln
- `docs/uebersicht.md` – Regalstruktur und Vollständigkeit (noch zu ermitteln)
- `docs/protokoll.md` – Arbeitsprotokoll ab Neustart
- `docs/NEUER_CHAT_BESTANDSANALYSE.md` – Arbeitsauftrag an den nächsten Chat

Die CSV-Tabellen wurden für diesen Neustart auf ihre Kopfzeilen zurückgesetzt. Die frühere Projektentwicklung bleibt in der Git-Historie erhalten, ist aber **keine Quelle für die neue Bestandsanalyse**.
