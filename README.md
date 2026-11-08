# Bücherregal – Bestandsaufnahme und alphabetische Sortierung

**Repository:** https://github.com/oooLITTLEooo/buecherregal  
**Sichtbarkeit:** öffentlich (`public`), ausdrücklich gewünscht  
**Single Source of Truth:** ausschließlich der **jeweils aktuelle tatsächliche GitHub-Dateibestand**

## Aktuelle Umräumliste – 08.11.2026

Die alphabetische Umräumplanung wurde ausdrücklich beauftragt. **1.022 erkannte Bücher** sind mit bisherigen und geplanten Standorten aufgeführt. Die **11 offenen Einträge** bleiben separat; **15 historische `kein_buch`-Einträge** werden nicht mitgezählt. Das Ist-Inventar bleibt bis zum tatsächlichen Umräumen unverändert.

- [Vollständige Umräumliste nach Autoren-Nachnamen](daten/umsortierung/umraeumliste.md)
- [CSV der Umräumliste](daten/umsortierung/umraeumliste.csv)
- [Geplante Belegung je Regalfach](daten/umsortierung/regalbelegung.md)
- [Breitenschätzung und Planungsmethode](docs/umsortierung_2026-11-08.md)
- [Elf offene Bücher zum manuellen Ergänzen](daten/nachkontrolle/offene-buecher-zum-ergaenzen.md)

Der Plan belegt **55 Fächer von 1-1 bis 7-7** in spaltenweiser Reihenfolge. Pro belegtem Fach ist Platz für mindestens ungefähr 2–3 weitere Bücher auf Grundlage grob geschätzter durchschnittlicher Rückenbreiten vorgesehen. Alle alten Standortnummern und Positionen sind erhalten.

## Neustart der Bestandsanalyse

Der Foto-Upload wurde am 06.11.2026 als abgeschlossen gemeldet; der Bestand wird ausschließlich am aktuellen Git-Stand geprüft. Die frühere Erfassung ist **nicht maßgeblich**. Keine Fotoanzahlen, Regalfachzuordnungen, Erinnerungen, Buchinventare oder Bilddateien aus vorherigen Chat-Nachrichten übernehmen.

**Verbindlicher Einstieg und vollständiger Arbeitsauftrag:**  
[docs/NEUER_CHAT_BESTANDSANALYSE.md](docs/NEUER_CHAT_BESTANDSANALYSE.md)

## Geplante Reihenfolge

1. Repository und den tatsächlich vorhandenen Foto-Dateibestand vollständig prüfen.
2. Identische und visuell doppelte Fotos vergleichen und nach dokumentierter Prüfung überflüssige Dubletten bereinigen.
3. Originalfotos mit unverändertem Namen nach `bilder/originale/` verschieben; nach geprüfter Fachzuordnung unveränderte **Kopien** unter `bilder/umbenannt/` nach Regalposition benennen.
4. Tatsächliche Regalstruktur und Vollständigkeit anhand des Gesamtbildes überprüfen; konkrete fehlende Fotos benennen.
5. **Erst dann** die Originalfotos in voller Auflösung auf einzelne Bücher analysieren und Autor, Titel, Fach und Position erfassen.
6. Alles versioniert in Git dokumentieren und anschließend überprüfen.

**Git-Arbeitsregel:** `sync → Skript/Änderung → sync → Analyse`.

## Standortkonvention

`Spalte-Fach`: von **links nach rechts** durch die Spalten, innerhalb jeder Spalte von **oben nach unten**. Beispiel: `1-5` bedeutet erste Spalte, fünftes Fach von oben. Die tatsächlich vorhandene Fach- und Spaltenzahl wird **erst aus den Fotos im Git** ermittelt.

Ziel der späteren physischen Umsortierung: **A–Z nach Autoren-Nachnamen**, entlang dieser Fachreihenfolge. Eine Umsortierung wird erst auf ausdrückliche neue Anweisung geplant.

## Projektstruktur

- `bilder/originale/` – unveränderte Originalfotos mit ursprünglichem Dateinamen
- `bilder/umbenannt/` – später nach tatsächlicher Regalposition benannte Kopien (unveränderte Bildbytes)
- `bilder/generiert/` – später ggf. erzeugte Diagramme und Fotoskizzen
- `daten/fotos.csv` – aus dem aktuellen Git-Bestand neu zu erstellendes Foto-Inventar
- `daten/fachstatus.csv` – tatsächliche Regalfächer und Foto-Abdeckung
- `daten/buecher.csv` – nach der Bildprüfung frisch erfasste Buchexemplare
- `docs/standorte.md` – Nummerierung und Erfassungsregeln
- `docs/uebersicht.md` – Regalstruktur und Vollständigkeit (noch zu ermitteln)
- `docs/protokoll.md` – Arbeitsprotokoll ab Neustart
- `docs/NEUER_CHAT_BESTANDSANALYSE.md` – Arbeitsauftrag an den nächsten Chat

Die CSV-Tabellen wurden für diesen Neustart auf ihre Kopfzeilen zurückgesetzt. Die frühere Projektentwicklung bleibt in der Git-Historie erhalten, ist aber **keine Quelle für die neue Bestandsanalyse**.
