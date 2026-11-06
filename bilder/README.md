# Originalfotos und Bildverwaltung

Dieses GitHub-Repository ist ausdrücklich **öffentlich**. Alle dort abgelegten Fotos sind entsprechend öffentlich einsehbar.

## Grundlage

Für die neue Bestandsanalyse zählen **nur die Bilddateien, die beim Start des neuen Chats tatsächlich im aktuellen Git-Repository liegen**. Bildlisten oder Dateien aus früheren Chats werden nicht importiert oder als Quelle verwendet.

Der Nutzer lädt die Fotos eigenständig und in voller Auflösung hoch. Erst nach Uploadabschluss werden alle Bilder **rekursiv im Repository** gesucht; der Zielordner darf noch abweichen.

## Zielablage und Namensschema

- `bilder/originale/Regal_Gesamt.jpg` – Übersichtsbild
- `bilder/originale/Regal_1-5.jpg` – erste Spalte, fünftes Fach von oben
- `bilder/originale/Regal_1-5_02.jpg` – zusätzliche nützliche Ansicht desselben Fachs
- `bilder/generiert/` – später erzeugte Abbildungen (nicht mit Originalen vermischen)

Die Namen sind **Beispiele**, keine Aussage über tatsächlich vorhandene Regalfächer. Dateierweiterungen an das echte Format anpassen.

## Qualitätsregeln

- Original-Bildbytes erhalten; nicht unnötig komprimieren, skalieren oder neu kodieren.
- Doppelte Fotos anhand von SHA-256 und visueller Ähnlichkeit beurteilen, nur wirklich überflüssige Aufnahmen entfernen.
- Alle Zuordnungen aus den realen Bildinhalten ableiten; Namen und Dateireihenfolge allein genügen nicht.
- Nach dem Sortieren Pfad, Prüfsumme, Auflösung, Fachzuordnung und Ergebnis in `daten/fotos.csv` eintragen.
- Nach jedem Git-Commit und Push den Ergebnisstand erneut prüfen.

Vollständiger Auftrag: [docs/NEUER_CHAT_BESTANDSANALYSE.md](../docs/NEUER_CHAT_BESTANDSANALYSE.md).
