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


## 2026-11-06 – Fachweise Unsicherheitenprüfung 2-7

- FOTO0012 Teile 01-03 gezielt für B00185, B00188 und B00198 eingesehen.
- B00185 = Brigitte Giraud, *Die Liebe ist doch sehr überschätzt*; B00188 = Petra Hammesfahr, *Das Geheimnis der Puppe* (Bild Bestseller-Bibliothek Band 6); B00198 = Roland Girtler, *Die feinen Leute: Von der vornehmen Art, durchs Leben zu gehen*.
- Nach Bild-/Bibliografieabgleich alle drei auf lesbar; 29/29 im Fach formell lesbar. Keine Buch-IDs, Positionen oder Bilddateien verändert.
- Gesamt 1048 Einträge, 959 lesbar, 49 prüfen, 40 offen; 15 Fächer vorläufig abgehakt; 25 weitere noch gezielt zu prüfen.
- Details: docs/fachpruefung_2-7_20261106.md. Als nächstes Fach 2-8.


## 2026-11-06 – Fach 2-8 gezielt nachgeprüft

- Aus FOTO0013 Teilen 03 und 04 ausschließlich B00226 (Position 14) geprüft. Autorin Eva Rossmann im Bild sichtbar, Titel mangels lesbarer Rückenaufschrift nicht sicher bestimmbar.
- Einzelfoto des Buchrückens oder Titelblatts angefordert; Status prüfen bleibt unverändert, keine unbelegten Titel ergänzt.
- Fach 2-8: 17 Einträge, 16 lesbar und 1 prüfen. Gesamt 1048, davon 959 lesbar, 49 prüfen, 40 offen.
- Gezielte Fachprüfung abgeschlossen, nicht abgehakt; 24 Fächer noch ungeprüft, 12 nachgeprüft mit offenem Fotobedarf. Details: docs/fachpruefung_2-8_20261106.md. Nächstes Fach: 3-1.


## 2026-11-06 – Zielprüfung Fach 3-1

- Acht unsichere Einträge B00232, B00235, B00240, B00241, B00247, B00249, B00257, B00258 mit allen vier Originalpixel-Ausschnitten von FOTO0014 untersucht.
- Fünf bestätigt/korrigiert: Eric Malpass *Wenn süß das Mondlicht auf den Hügeln schläft* sowie vier Bände André Kaminski (*Flimmergeschichten*, *Kiebitz*, *Die Gärten des Mulay Abdallah*, *Schalom allerseits*).
- B00235 B00240 B00258 unlesbar bzw. mit unklaren Bandgrenzen; Fotobedarf präzise benannt. Fach 3-1 nachgeprüft aber nicht abgehakt.
- 1048 unveränderte Buch-IDs: 964 lesbar, 44 prüfen, 40 offen; 15 Fächer vorläufig abgehakt; 23 noch gezielt nachzuprüfen.
- Details docs/fachpruefung_3-1_20261106.md. Nächstes Fach 3-2.


## 2026-11-06 – Gezielte Nachprüfung Fach 3-2

- FOTO0015 Teil 03 und 04 aus Git betrachtet; nur B00277 erneut bewertet.
- Buchrücken benennt Ben und Daniela Segenreich und *Fast ganz normal* (Amalthea). Vollständigen Titel *Fast ganz normal – Unser Leben in Israel* mit Original-Verlagskatalog verifiziert.
- B00277 auf lesbar gesetzt. Fach 3-2: 21/21 Bücher lesbar, vorläufig abgehakt. Gesamt unverändert 1048 vorläufige Exemplare; 965 lesbar, 43 prüfen, 40 offen.
- 16 Fächer vorläufig abgehakt, 22 weitere gezielt zu prüfen. Keine Fotos oder Standortdaten verändert. Einzelbericht docs/fachpruefung_3-2_20261106.md. Nächstes Fach 3-3.


## 2026-11-06 – Gezielte Nachprüfung 3-3 und Feststellung eines möglichen Zählfehlers

- FOTO0016 Teil 02-04: B00292 als Carl Gustav Jung, *Erinnerungen, Träume, Gedanken* (aufgezeichnet und herausgegeben von Aniela Jaffé), B00300 als Jakob Wassermann, *Etzel Andergast* (Moewig), identifiziert.
- Zwischen Eva Rossmann *Alles rot* und Jung ist vermutlich John Irving *Deutschlandreise* als weiterer schmaler Buchrücken sichtbar. In 3-3 möglicherweise 22 statt 21 tatsächliche Bände. Deshalb keine vorläufige Fachfreigabe trotz gelesener Titel.
- Status Fach 3-3: `positionsabgleich_noetig`; Nachfoto und spätere korrigierte Positionsliste erforderlich. Keine Bild-, Buch-ID- oder Positionsänderung.
- Aktuell 1048 erfasste Bücher (967 lesbar, 42 prüfen, 39 offen), evtl. mindestens ein weiteres Exemplar. Noch 21 gezielte Fachprüfungen; Bericht docs/fachpruefung_3-3_20261106.md. Nächstes Fach 3-4.


## 2026-11-06 – Gezielte Nachprüfung Fach 3-4

- Original FOTO0017 und die Git-Originalpixelteile 03/04 nur für B00318 (Position 17) untersucht. Zwischen John Irving *Eine Mittelgewichts-Ehe* und *Zirkuskind* kann das Vorliegen eines eigenständigen weiteren Bandes nicht sicher belegt werden.
- Kein Titel geraten und kein Datensatz gelöscht. B00318 bleibt offen, das Fach benötigt ein frontales Nachfoto und eine physische Nachzählung an Position 17.
- Fach 3-4: weiterhin 22 vorläufige Einträge (21 lesbar, 1 offen), gezielte Nachprüfung erfolgt, nicht abgehakt. Gesamt unverändert 1048 Einträge: 967 lesbar, 42 prüfen, 39 offen.
- Jetzt 20 Fächer mit noch ausstehender gezielter Kontrolle, 14 erneut geprüft mit Restunsicherheit; Bericht docs/fachpruefung_3-4_20261106.md. Als nächstes Fach 3-5.


## 2026-11-06 – Gezielte Nachprüfung Fach 3-5

- FOTO0018 alle 4 Originalpixel-Ausschnitte aus Git betrachtet, vier vorher unsichere IDs im Teil 02 geprüft.
- B00329 richtig als Karl-Markus Gauß und Martin Pollack (Herausgeber), *Das reiche Land der armen Leute: Literarische Wanderungen durch Galizien*; B00330 Joy Fielding, *Träume süß, mein Mädchen* (vorher „Träume sind“ falsch); B00332 Konstantin Wecker, *Dann denkt mit dem Herzen*; B00333 Erle Stanley Gardner, *Mord auf der Luxusjacht*.
- Fach 3-5 jetzt 16/16 formal lesbar, vorläufig abgehakt, Originalfotos und alle Positionen unverändert.
- Stand 1048 inventarisierte Einträge, 971 lesbar, 38 prüfen, 39 offen. 17 Fächer abgehakt, 19 gezielt nachzuprüfen. Belege docs/fachpruefung_3-5_20261106.md. Nächstes Fach: 3-6.


## 2026-11-06 – Gezielte Nachprüfung Fach 3-6

- Git-Original FOTO0019: Teil 01 für B00340, Teile 03-04 für B00360 geprüft.
- B00360 als **Antonio Manuel Garrido – Das Pergament des Himmels** über Bildzuordnung und Aufbau-Verlagskatalog ergänzt, auf lesbar gestellt.
- B00340: Veit Heinichen am schwarzen Rücken sichtbar, bisheriger Titelanfang *Kalte Tage des …* aber nicht sicher lesbar und bibliografisch nicht bestätigt. Bleibt prüfen, frontales Rückendetail/Titelblatt nötig; keinen Werktitel erfunden.
- Fach 3-6 vorläufig 25 Bucheinträge (24 lesbar, 1 prüfen), gezielte Prüfung abgeschlossen, nicht abgehakt. Gesamt 1048 Einträge, 972 lesbar, 37 prüfen, 39 offen; 18 noch gezielt zu prüfende Fächer. Bericht docs/fachpruefung_3-6_20261106.md. Nächstes Fach 3-7.


## 2026-11-06 – Gezielte Nachprüfung Fach 3-7

- Original FOTO0020, vier Git-Originalpixel-Ausschnitte geprüft, einzig unklaren Datensatz B00373 erneut betrachtet.
- Name Brigitte Schwaiger auf schmalem orange/rosa Buchrücken zwischen Håkan Nesser und Sten Nadolny sichtbar, Titel in den vorhandenen Ausschnitten nicht zweifelsfrei lesbar. Kein Titel aus Bibliografie geraten.
- Original-JPEG über GitHub-API wegen Binär-/Größenbeschränkung nicht vollständig nachgeladen; einzelnes Rücken-/Titelblattfoto erforderlich.
- B00373 bleibt offen. Fach 3-7 weiterhin 18 vorläufige Einträge, 17 lesbar und 1 offen, gezielte Prüfung durchgeführt, nicht abgehakt.
- Gesamt weiterhin 1048 Einträge: 972 lesbar, 37 prüfen, 39 offen. Jetzt 17 gezielte Fachprüfungen ausstehend. Bericht docs/fachpruefung_3-7_20261106.md, nächstes Fach 4-2.


## 2026-11-06 – Gezielte Nachprüfung Fach 4-2

- Original FOTO0023, alle vier Originalpixelteile aus Git betrachtet; nur B00418 (Pos 1) und B00433 (Pos 16) bewertet.
- B00418: Autor Folke Tegetthoff erkennbar, Titel des ersten dunkelgrün-blauen Bandes nicht lesbar. Nicht mit danebenstehenden *Kräutermärchen* (B00419) gleichgesetzt.
- B00433: dunkler schmaler Rücken zwischen Friedrich Torberg *Süßkind von Trimberg* und Sabine Thiesler *Die Totengräberin* sichtbar; Autor und Titel unbekannt.
- Für beide Fälle Einzelaufnahme/Titelblatt benötigt, keine neuen Titel geraten, Status unverändert. Fach 4-2 mit 21 Einträgen (19 lesbar, 1 prüfen, 1 offen) gezielt kontrolliert, nicht abgehakt. Gesamt 1048 (972 lesbar, 37 prüfen, 39 offen); 16 weitere Fachprüfungen. Bericht docs/fachpruefung_4-2_20261106.md. Nächstes Fach 4-3.


## 2026-11-06 – Gezielte Nachprüfung Fach 4-3

- Git-FOTO0024, Originalpixelteile 02/03/04 nur für B00448 und B00454 ausgewertet.
- B00448: Ann Granger auf schmalem dunklem Buchrücken nach Wolf Haas *Auferstehung der Toten* lesbar; Titel nicht bestimmbar. B00454: schmaler dunkler Bereich zwischen Petros Markaris *Zurück auf Start* und Elizabeth George *Mein ist die Rache*, weder Titel noch eigenständige physische Buchgrenze zuverlässig erkennbar.
- Status unverändert (1 prüfen, 1 offen), für beide Fälle konkrete Frontal-/Titelblattfotos dokumentiert. Fach 4-3 vorläufig 18 Einträge (16 lesbar), gezielt nachgeprüft aber nicht abgehakt.
- Gesamt unverändert 1048 Einträge (972 lesbar, 37 prüfen, 39 offen). Jetzt 15 noch gezielte Fachprüfungen. Bericht docs/fachpruefung_4-3_20261106.md, nächstes Fach 4-5.
