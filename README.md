# Bücherregal – Inventar und Sortierung

**Öffentliches GitHub-Repository (Public) auf ausdrücklichen Wunsch des Eigentümers**, damit Interessierte Einsicht in die Sammlung und Projektfortschritte erhalten. GitHub als **Single Source of Truth**. Zuvor war es zeitweise privat; die Umstellung auf Public wurde vom Nutzer am 2026-11-06 als **beabsichtigt** bestätigt.

## Projektziel

Ein vollständiges, nachvollziehbares Buchinventar mit ursprünglicher Regalposition erstellen und anschließend alphabetisch nach Autorennachnamen sortieren.

Nummerierung: links beginnen, in Spalte 1 von oben nach unten, danach in Spalte 2 wieder von oben nach unten, usw. `1-5` bedeutet Spalte 1, Fach 5. Innerhalb des Fachs die Bücher von links nach rechts zählen.

## Daten und Bilder

- `daten/buecher.csv`: Autor, Titel, ursprünglicher Standort, Position und Prüfstatus
- `daten/fotos.csv`: Zuordnung originaler Fotos, SHA-256 und Git-Uploadstatus
- `daten/fachstatus.csv`: fotografierte und noch fehlende Regalfächer
- `bilder/originale/`: alle vom Nutzer übermittelten, **unveränderten** JPEGs mit Regalnamen
- `bilder/generiert/`: später generierte Bilder
- `docs/uebersicht.md`: Gesamtbild und Fortschritt
- `docs/standorte.md`: Nummerierungs- und Sortierregeln
- `docs/protokoll.md`: Änderungen und Entscheidungen
- `scripts/import-fotos.sh`: SHA-256-geprüfter Bildimport in den Git-Clone samt Commit und Push

### Bilddateinamen

- Gesamtansicht: `Regal_Gesamt.jpg`
- Regalfach: `Regal_3-7.jpg` (Spalte 3, Fach 7)
- Weitere Ansicht: `Regal_3-7_02.jpg`

Alle Originaldateien werden nur **umbenannt**, nicht inhaltlich verändert.

## Aktueller Stand (2026-11-06)

- GitHub-Sichtbarkeit: **public**, ausdrücklich gewünscht.
- **25 Fotos** im Chat übermittelt: 1 Gesamtansicht + 24 Fachfotos (bis einschließlich Fach `4-4`).
- Die Fotos wurden anhand der Aufnahmen benannt und in einem verifizierten ZIP gesammelt.
- **0 von 25 Original-JPEGs im Git-Repository**; alle in `daten/fotos.csv` als `upload_status=ausstehend` markiert. Der Upload steht aus, weil die verfügbare GitHub-Verbindung keinen direkten Dateitransfer lokaler Binärbilder ermöglicht.
- Die vorläufige Buchinventarliste enthält **362** Positionen aus den früher bearbeiteten Fächern, davon **68** als offen/zu prüfen. Die sechs zuletzt erhaltenen Fächer werden gemäß neuem Workflow erst **nach erfolgreicher Bildarchivierung in Git** detailliert ausgewertet.
- **Nächste noch fehlende Aufnahme:** voraussichtlich `4-5` (danach `4-6`, `4-7`, `4-8`), anhand der Gesamtübersicht weiter überprüfen.

## Neuer verbindlicher Arbeitsablauf

1. Bilder empfangen, Standorte zuordnen und Dubletten erkennen.
2. Alle unveränderten Originale **zuerst im GitHub-Repository ablegen**, Upload mittels SHA-256 und Pfad verifizieren.
3. Erst danach jedes Fach exakt analysieren, unlesbare Titel markieren, jedes Buch inventarisieren.
4. Änderungen mit Git dokumentieren: **sync → script/import → sync → analyse**.
5. Nach vollständiger Aufnahme Sortierplan nach Autorennachname erstellen.

### Ersteinmaliger Import der ersten 25 Fotos

Original-ZIP `buecherregal_fotos_bis_4-4_2026-11-06.zip` aus der Chat-Antwort herunterladen. Im geklonten Repository mit Git-Schreibzugriff ausführen:

```bash
git clone https://github.com/oooLITTLEooo/buecherregal.git
cd buecherregal
bash scripts/import-fotos.sh /vollstaendiger/pfad/buecherregal_fotos_bis_4-4_2026-11-06.zip
```

Das Skript verifiziert jede Original-JPEG-Datei gegen `daten/fotos.csv`, setzt den Uploadstatus und führt Commit + Push aus. Danach:
```bash
git ls-files bilder/originale/ | grep -c '\.jpg$'
git status --short
```

**Hinweis:** GitHub ist öffentlich, auch die dort später hochgeladenen Original-Regalfotos können von anderen angesehen werden.
