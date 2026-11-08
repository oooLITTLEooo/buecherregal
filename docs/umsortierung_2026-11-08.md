# Alphabetische Umräumplanung – 08.11.2026

## Auftrag und Ergebnisdateien

Alle 1.022 Inventarzeilen mit Status `lesbar` nach Autoren-Nachnamen ordnen. Alte Regalnummern, Positionen und IDs bleiben unverändert im Ist-Inventar. Die elf offenen Bücher werden später geklärt, die 15 `kein_buch`-Zeilen zählen nicht zum Bestand.

- [Vollständige Umräumliste](../daten/umsortierung/umraeumliste.md)
- [CSV mit sieben Spalten](../daten/umsortierung/umraeumliste.csv): ID, Autor, Titel, Regal, Position, Nach Regal, Nach Position
- [Belegung aller 64 Fächer](../daten/umsortierung/regalbelegung.md)
- [Breitenannahmen](../daten/umsortierung/breitenschaetzung.json)
- [Ergebnisprüfung](../daten/umsortierung/pruefung.json)

## Reihenfolge

Zielreihenfolge 1-1, 1-2, …, 1-8, 2-1, …, 8-8. Innerhalb eines Faches von links nach rechts, Zielpositionen ab 1. Nachname, dann Vorname, dann Titel, zuletzt ID. Bei mehreren Autoren zählt der erste genannte Name. Namensvorsätze `von`, `du` und `le` werden beim Sortieren übergangen. Umlaute wie Grundbuchstaben, ß wie ss und andere diakritische Zeichen vereinfacht. Anzeigenamen bleiben in ihrer vorhandenen Schreibweise erhalten. Ein erkanntes Lesebuch ohne Autorenangabe, B01017 *Winter am Kamin: Das große Lesebuch*, wird am Schluss zugewiesen. Bestehende Autoren- und Titelangaben werden nicht bibliografisch umgeschrieben.

## Grobe Breitenplanung

Die vorhandene Gesamtaufnahme und vergrößerte Ausschnitte daraus wurden für die Platzschätzung betrachtet. Für jedes der 51 Herkunftsfächer wurde der von Büchern belegte Anteil der Fachbreite grob geschätzt; sichtbare Lücken und andere Gegenstände zählen nicht als Buchbreite. Verdeckte Bereiche sind besonders grob. Geschätzte Anteile stehen nachvollziehbar in der JSON-Datei. Eine mit `lesbar` gekennzeichnete Inventarzeile steht nicht für eine gemessene Einzelbuchbreite.

Als Größenmodell gelten die mittleren Spalten 2–7 mit relativer Breite 1,00, die laut vorhandener Regalübersicht schmaleren Randspalten 1 und 8 mit vorsichtig angesetzter Breite 0,85. Das sind Planungsannahmen, keine gemessenen Abmessungen. Alle Fachebenen einer Spalte erhalten dieselbe Breitenannahme.

Mittlere Rückenbreite pro Herkunftsfach = relative Fachbreite × geschätzter Buchfüllanteil ÷ Inventarzeilen ohne `kein_buch` in diesem Fach. Jedes erkannte Buch übernimmt diese mittlere Herkunftsbreite. Dadurch werden beispielsweise die vielen schmalen Christie-Bände anders gewichtet als breite Bände aus locker gefüllten Fächern. Unterschiede einzelner Bücher innerhalb desselben Herkunftsfachs sind nicht vermessen und können vor Ort Abweichungen verursachen.

In der alphabetischen Reihenfolge wird das nächste Buch nur dann ins Fach aufgenommen, wenn danach noch mindestens **2,5 durchschnittliche Rückenbreiten der dort eingeplanten Bücher** frei bleiben. Eine Restlücke unterhalb der Breite des nächsten Buches kann die Reserve größer machen. Das letzte belegte Fach kann deutlich mehr Platz frei lassen. Der Wunsch nach Platz für ungefähr 2–3 Bücher wird als Mindestreserve umgesetzt, nicht als feste Anzahl Bücher pro Fach.

Die Lampe in 1-4 und andere Gegenstände in belegten Zielfächern müssen beim Umräumen weichen. Die Zielwerte sind eine Arbeitshilfe zum Einräumen; Fachgrenzen bei abweichender tatsächlicher Buchbreite entsprechend verschieben. Das ursprüngliche Inventar wird erst nach einer bestätigten physischen Umsortierung als neuer Ist-Stand geändert.

## Umsetzung und Prüfung

1. Aktuellen Git-Inventarstand sowie Foto- und Fachzuordnung lesen, Gesamtfoto betrachten.
2. Breitenannahmen und Generator separat im Git speichern.
3. Umräumliste und Fachbelegung erzeugen, vollständige Abdeckung aller erkannten IDs, Sortierung, ursprüngliche Positionen, eindeutige Zielplätze und Mindestreserve prüfen.
4. Ergebnisdateien im Git speichern und erneut lesen/vergleichen.

Reproduktion aus dem Repository-Hauptverzeichnis: `python3 scripts/plane_umsortierung.py`. Der Generator prüft den SHA-256-Wert des Ausgangsinventars und verweigert unverändert übernommene Breitenannahmen bei geändertem Inventarstand. Für einen späteren neuen Stand Quelle und Annahmen zuerst prüfen und aktualisieren. Grundlage dieser Planung: Commit `1b1f485ed70bbd6705ca0705034ef2684ad74352`.
