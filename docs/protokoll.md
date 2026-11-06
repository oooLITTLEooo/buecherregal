# Arbeitsprotokoll – Neuaufnahme

## 2026-11-06 – Verbindlicher Neustart für den neuen Chat

- GitHub-Repository `oooLITTLEooo/buecherregal` bleibt **public**, bewusst gewählt.
- Die eigentliche Bildbestandsanalyse soll **ausschließlich aus dem zum Start des neuen Chats tatsächlich vorhandenen Git-Dateibestand** erfolgen.
- Der Nutzer führt den Foto-Upload selbst durch und wird ihn vor dem Start des neuen Chats abschließen.
- Vorherige, aus der Unterhaltung abgeleitete Buchlisten, Fotozuordnungen, Regalfachzahlen und vorläufige Erkennungen werden **nicht übernommen**.
- Die CSV-Dateien für Fotos, Regalfachstatus und Bücher wurden daher als **leere Vorlagen** zurückgesetzt.
- Alte Projektstände bleiben in der Git-Historie, sind aber für die neue Erfassung **nicht maßgeblich**.
- Verbindlicher Arbeitsauftrag: `docs/NEUER_CHAT_BESTANDSANALYSE.md`.
- Der neue Chat soll (1) Git-Repositorium und Fotos prüfen, (2) tatsächliche Dubletten dokumentiert entfernen, (3) Fotos nach den realen Fächern sortieren und umbenennen, (4) fehlende oder ungenügende Ansichten identifizieren und (5) erst danach alle Bücher anhand der Git-Originalbilder inventarisieren.
- Keine Fotolöschungen, Bildumbenennungen oder Buchanalysen in diesem Dokumentationsschritt vorgenommen.

## 2026-11-06 – Stufe 1: Git-Ablage der hochgeladenen Originalfotos

- Datenquelle: `main` zum Beginn der Arbeiten, Commit `29baf1dcc23781e5163c242c8991251a5c2ee417`.
- Rekursiver Git-Baum: 68 Einträge; 52 JPEG-Bilder direkt im Root gefunden. Die bisherigen Originale im Root waren noch unklassifiziert.
- Alle 52 Root-Bilder werden verlustfrei per bestehender Git-Blob-SHA nach `bilder/originale/` verschoben; Dateinamen und Bytes bleiben identisch.
- `bilder/umbenannt/` wird als getrennte Ablage der später **nach Bildinhalt** bestimmten Regalpositionskopien vorbereitet. Zunächst **keine Positionsnamen**, da der Bildinhalt noch nicht geprüft ist.
- `daten/fotos.csv`: 52 initiale Foto-IDs, ursprüngliche Git-Pfade, neue Pfade, Größen und Git-Blob-SHAs. SHA-256, Auflösung, EXIF, visueller Vergleich, Gesamtübersichtszuordnung und Buchinventar sind **noch offen**; Git-Blob-SHA ist nicht die SHA-256-Prüfsumme.
- In diesem Schritt keine Fotos nach scheinbar ähnlichen Dateinamen entfernt. 0 byteidentische Git-Blob-SHA-Dopplungen innerhalb der Root-Fotos festgestellt.
- Abweichung von der bisherigen Übergabe präzisiert: Originaldateinamen erhalten, positionsbezogene Benennung ausschließlich über Kopien in `bilder/umbenannt/`.

## 2026-11-06 – CSV-Reparatur vor Bildanalyse

- Der erste GitHub-Actions-Lauf schlug wegen eines unescaped Semikolons im Feld notizen der initialen daten/fotos.csv fehl. Das Semikolon verschob die erwartete Git-SHA-Spalte.
- GitHub Actions hat direkt mit git hash-object und git ls-files --stage die Unveraendertheit des ersten JPEG bestaetigt.
- Die CSV wurde anhand des aktuellen Git-Baums mit exakt 13 Feldern je Zeile neu aufgebaut, alle 52 Foto-IDs beibehalten, Originalpfade/Blob-SHAs verifiziert. Keine Originalfotos veraendert.
- Erneuter technischer Analyselauf nach Reparatur angestossen.

## 2026-11-06 – Erfolgreiche technische und visuelle Fotoprüfung

- GitHub Actions hat alle 52 Originalfotos erfolgreich geöffnet und SHA-256, Git-Blob-SHA, JPEG-Abmessungen, EXIF und dHash in daten/fotos.csv eingetragen. 0 Lesefehler.
- Vier Kontaktbögen und 52 Foto-Vorschauen aus den Git-Originalen generiert und in Git dokumentiert.
- FOTO0001 ist Gesamtübersicht: acht Spalten, acht Fach-Ebenen. FOTO0002–FOTO0052 folgen in den aufgenommenen Fachreihen.
- Alle 52 positionsbezogen benannten Kopien als bestehende Git-Blobs ohne erneute Kodierung angelegt; 52 von 52 Kopie-Hashes nach Git-Push geprüft.
- DHash-Kandidat FOTO0021/FOTO0033 visuell als verschiedene Bücher und verschiedene Fächer erkannt; beide erhalten.
- Mapping in daten/fotos.csv und Fachstatus für alle 64 Fachpositionen in daten/fachstatus.csv aktualisiert.
- Fehlende mögliche Buchdetails: 8-1, 8-2; 7-8 wegen Verdeckung zu prüfen. Keine physische oder geplante alphabetische Umsortierung.

## 2026-11-06 – Beginn der physischen Buchexemplar-Erfassung

- In den Bildvorschauen FOTO0002 bis FOTO0005 wurden 59 vorläufige einzelne Buchrücken in Reihenfolge erfasst.
- 18 Angaben sind unsicher oder offen und brauchen den Feinabgleich der Originalauflösung.
- Keine unsichtbaren Exemplare erfunden; jedes erfasste Buch enthält die Originalfoto-Referenz.
- Die restlichen Detailbilder und die fehlenden Fachaufnahmen sind weiter offen, siehe docs/inventur_fortschritt.md.

## 2026-11-06 – Korrektur frueherer Vorschaufehler aus Originalaufloesung

- Native Ausschnitte von FOTO0002 bis FOTO0005 visuell neu geprueft.
- 22 zuvor fehlerhafte oder unvollstaendige Angaben im Inventar der Faecher 1-5 bis 1-8 korrigiert. 2 unklare Positionen verbleiben.
- Bestehende Buch-IDs, Fachpositionen und Originalfoto-Referenzen erhalten. Git-Historie bewahrt alle alten Lesungen.

## 2026-11-06 – Erfassung 2-5 bis 2-8

- Native Originalausschnitte FOTO0010–FOTO0013 visuell geprüft. 80 neue Datensätze, 11 unsicher, Gesamtstand 229.
- Keine Originalfotos geändert oder alphabetische Umsortierung begonnen.

## 2026-11-06 – Erfassung Fächer 3-1 bis 3-4

- Originalpixel-Ausschnitte von FOTO0014 bis FOTO0017 geprüft, 94 weitere vorläufige Datensätze, 15 unsicher, Gesamtstand 323.
- Zwei Fehllesungen in 2-7 korrigiert; Originale und physische Buchreihenfolge nicht verändert.

## 2026-11-06 – Fächer 3-5 bis 3-8

- Git synchronisiert; Originaldateien FOTO0018–FOTO0021 geprüft; 16 hochauflösende Ausschnitte verwendet.
- 77 Buchexemplare mit Standort, physischer Links-rechts-Position, Bildquelle und Lesestatus hinzugefügt.
- 8 Einträge offen/pruefen, keine erdachten Autor- oder Titelangaben.
- Nächste Originalfotos für Fächer 4-1 bis 4-4 zur Vollauflösungsprüfung vorgemerkt. Keine alphabetische Umsortierung.

## 2026-11-06 – vierte Spalte, Fächer 4-1 bis 4-4

- Git-Sync und Prüfung der 16 nativen Originalausschnitte von FOTO0022 bis FOTO0025 durchgeführt.
- 71 neue Exemplare einzeln nach physischer Links-rechts-Position dokumentiert; 8 mit offenen/pruefen-Feldern.
- Originale unverändert, keine Umordnung. Nächste vier Detailfotos in der Git-Actions-Prüfliste vorgesehen.


## 2026-11-06 – Abschluss Spalte 4, Faecher 4-5 bis 4-8

- Git-Originaldateien FOTO0026 bis FOTO0029 nur lesend ueber native Bildausschnitte geprueft.
- 87 separate sichtbare Buchruecken vorlaeufig aufgenommen. 14 unsichere Angaben sind als pruefen oder offen markiert.
- Die Originalfotos blieben unveraendert. Git-Sync vor dem Schreiben, Quellenpfade kontrolliert, neue Vollauflosungs-Queue fuer FOTO0030..FOTO0033 eingetragen. Keine alphabetische Sortierung.


## 2026-11-06 – Fächer 5-1 bis 5-4

- 85 vorläufige Exemplar-Datensätze aus den Originalbildern FOTO0030 bis FOTO0033 nach nativer Pixelprüfung angehängt.
- Offene Teiltexte (u.a. dünne Taschenbücher und Mehrfachbände) bleiben markiert, ohne aus früheren Chats zu ergänzen.
- Vorheriger Git-Stand geprüft, keine Originalfotos verändert. Nächster Prüfauftrag FOTO0034–FOTO0037 per Git-Workflow; keine alphabetische Umsortierung.


## 2026-11-06 – Fächer 5-5 bis 5-8

- 83 sichtbare Exemplare aus den 16 nativen Prüfausschnitten zu FOTO0034..FOTO0037 erfasst; 17 offene Titel/Buchangaben markiert.
- Datensatz mit Dieter Noll / Die Abenteuer des Werner Holt von falsch getrennten Namensfeldern berichtigt.
- Kein Originalbild verändert. Git vorher synchronisiert, Folgeprüfung FOTO0038–FOTO0041 im Git-Workflow eingetragen. Keine alphabetische Umsortierung.


## 2026-11-06 – Spalte 6, erste Hälfte

- Fotos FOTO0038–FOTO0041 im Git vollaufloesend geprueft; 87 neue physische Buchdatensaetze. 11 unsicher/offen.
- Originalfoto-Pfade und Standort 6-1 bis 6-4 dokumentiert; keine Originalbilder geaendert, keine alphabetische Umordnung.
- Folge-Queue auf FOTO0042–FOTO0045 gesetzt.


## 2026-11-06 – Fächer 6-5 bis 6-8

- Native Ausschnitte aus den Originalen FOTO0042–FOTO0045 visuell geprüft, auch die Serie von schmalen Agatha-Christie-Bänden; keine Bilddaten im Original geändert.
- 100 vorläufige Exemplare in Links-rechts-Position geschrieben; 10 unklar/offen.
- Git-Sync mit Foto-Pfaden, keine Buchumsortierung. Nächster Crop-Lauf für FOTO0046–FOTO0049 vorgemerkt.

## 2026-11-06 – Siebte Regalspalte 7-1 bis 7-4

- Aktuellen Git-Stand samt vorhandener 913 Eintraege und Fotomapping vor dem Schreiben abgeglichen.
- FOTO0046–FOTO0049 jeweils aus vier nativen Pixel-Ausschnitten gelesen. 74 vorlaeufige Exemplare zu daten/buecher.csv ergaenzt.
- Unlesbare oder nicht zweifelsfrei abzugrenzende Buchruecken bleiben offen/pruefen und sind mit Foto-/Fachposition rueckverfolgbar.
- Alle Originalfotos und bereits vorhandene Buecher-Datensaetze unveraendert; keine physische Sortierung oder Bildloeschung.
- Folgeauftrag in daten/bildanalyse/crop_queue.txt: FOTO0050 bis FOTO0052.

## 2026-11-06 – Siebte Spalte 7-5 bis 7-7, Foto-Inventur abgeschlossen

- Aktuellen Git-HEAD und bestehende 987 Bucheintraege vor Schreiben abgeglichen.
- Git-Folgeworkflow stellte 12 native Vollaufloesungs-Ausschnitte fuer FOTO0050–FOTO0052 bereit. 61 Datensaetze mit stabilen fortlaufenden IDs erfasst.
- Unsichere Titel, verborgene Ruecken sowie doppelbetitelte Sammelbaende als pruefen/offen dokumentiert. Nichtbuch-Material (Notizblaetter, Gulda-CD-Hoerbuch in 7-7) nicht als Buch aufgenommen.
- Originalbilder unveraendert. Alle 51 verfuegbaren Detailfotos durchgegangen. Offene fotografische Luecken 8-1, 8-2 und Pruefung 7-8; finale fachweise Plausibilitaetspruefung steht aus.

## 2026-11-06 – Zweite Detailprüfung unsicherer Fotoablesungen (Teil 1)

- Alle 159 bisher als offen/pruefen markierten IDs als Prüfbasis fixiert.
- Native Foto-Bildausschnitte für die Fächer 1-7 bis 1-8, 2-1 bis 2-8, 3-1 und 7-1 bis 7-7 betrachtet und 27 eindeutige Autor-/Titelangaben direkt in daten/buecher.csv korrigiert bzw. bestaetigt.
- Das Inventar bleibt bei 1048 Zeilen; IDs, Positionen, Originalquellpfade unveraendert.
- Geprüfte Änderungen und noch ausstehende Einträge in docs/feinpruefung_unsicher_20261106.md und daten/bildanalyse/feinpruefung_unsicher.csv.
- Weitere Sichtprüfung der übrigen Fächer (insbesondere Spalten 3-6) noch ausstehend; offene Titel bleiben ausdrücklich ungesichert.

## 2026-11-06 – Feinprüfung restlicher Git-Originalpixel und 25 weitere Berichtigungen

- Weitere native 1:1-Pixel-Ausschnitte aus den vorhandenen 8160x4590-JPEGs eingesehen; bei zwei Teilbildern von FOTO0042 schlug die Bildauslieferung fehl. Dies ist im Prüfprotokoll explizit dokumentiert.
- Weitere 25 prüfpflichtige Einträge sicher nachkontrolliert (kumulativ 52). Darunter falsche Autoren bei Eva Bakos, Nicholas Sparks sowie Doris Knecht korrigiert.
- Für die übrigen 107 ursprünglich fraglichen Einträge kein Scheinabschluss: Details weiterhin `offen`/`pruefen`, einschließlich bibliographisch nur teilweise bekannter Einträge und unklarer Buchzählung.
- Es wurden keine Originalfotos überschrieben, keine Büchernummern neu vergeben und kein vorhandenes Exemplar entfernt.



## 2026-11-06 – Gezielt Fach 2-4 nachgeprüft

- FOTO0009 originalpixelbasiert in Teilbildern 1, 2 und 4 für B00131 und B00149 gesichtet.
- B00149 als Peter Høeg, *Von der Liebe und ihren Bedingungen in der Nacht des 19. März 1929*, anhand rororo 22314 am Rücken mit Bibliotheksabgleich bestätigt und bibliografisch korrigiert.
- B00131 bleibt mangels eindeutig lesbarem Rücken und gesicherter Bandgrenze offen, Einzelaufnahme angefordert.
- Gesamt 1048 Einträge: 953 lesbar, 55 prüfen, 40 offen. Nächster Prüfschritt Fach 2-5. Siehe docs/fachpruefung_2-4_20261106.md.


## 2026-11-06 – Fach 2-5 gezielt nachgeprüft

- FOTO0010 Teile 02 und 03: B00155 als Helen Fielding, Bridget Jones, sowie B00161 als Mary Higgins Clark, Dass du ewig denkst an mich, auf den Originalpixeln identifiziert.
- 17 von 17 vorläufigen Buchdatensätzen im Fach lesbar. Keine Originalfotos verändert oder Positionen verschoben.
- Gesamt: 1048 Einträge, 955 lesbar, 53 prüfen, 40 offen. 13 Fächer vorläufig abgehakt, 27 gezielt nachzuprüfen.
- Siehe docs/fachpruefung_2-5_20261106.md. Nächstes Fach: 2-6.


## 2026-11-06 – Gezielte Nachprüfung Fach 2-6

- FOTO0011 Teile 01 und 02 zum einzigen unsicheren Eintrag B00170 gelesen. Auf schwarzem Rücken Götz Schrage, 1000x verliebt und Milena erkennbar; offiziellen Katalogtitel beim Verlag als *Tausendmal verliebt* abgeglichen.
- 17 von 17 Büchern im Fach nun formal lesbar, vorläufig abgehakt; keine Bilder, Standorte oder IDs verändert.
- Stand 1048 Einträge, 956 lesbar, 52 prüfen, 40 offen. 14 Fächer abgehakt, 26 weitere gezielt zu prüfen.
- Bericht: docs/fachpruefung_2-6_20261106.md. Nächstes Fach: 2-7.
