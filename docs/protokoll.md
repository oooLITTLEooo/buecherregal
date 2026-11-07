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


## 2026-11-06 – Fach 4-5 gezielt geprüft

- FOTO0026: vier Originalpixel-Ausschnitte gesichtet, ausschließlich B00474, B00475 und B00486 neu bewertet.
- B00474 = Mary Higgins Clark, *Und morgen in das kühle Grab*, bestätigt; B00475 = Corinna Milborn / Markus Breitenecker, *Change the Game: Wie wir uns das Netz von Facebook und Google zurückerobern*, bisherige Autorenschreibweise korrigiert; B00486 = Semezdin Mehmedinović, *Sarajevo Blues*, bestätigt.
- Fach 4-5 nun 19/19 Einträge lesbar, vorläufig abgehakt. Keine Fotos oder Buch-IDs oder Positionen verändert.
- Gesamt 1048 Einträge: 975 lesbar, 34 prüfen, 39 offen. 18 Fächer abgehakt, 14 gezielt zu prüfen. Bericht docs/fachpruefung_4-5_20261106.md; nächstes Fach 4-6.


## 2026-11-06 – Gezielte Nachprüfung Fach 4-6

- Git-Original FOTO0027 (Originalpixel Teil 01, zur Orientierung Teil 02) nur für B00492 überprüft.
- B00492 liegt zwischen Sabine Thiesler *Hexenkind* und Paul Auster *Nacht des Orakels*. Ein schmaler dunkler Bereich ist sichtbar, aber weder eigenständige Buchgrenze noch Autor/Titel sicher nachweisbar.
- Status bleibt `offen`; Frontalfoto und physische Nachzählung mit ggf. Titelblatt erforderlich. Fach 4-6 bleibt bei 22 vorläufigen Einträgen (21 lesbar, 1 offen), nicht abgehakt.
- Gesamt unverändert 1048 Einträge: 975 lesbar, 34 prüfen, 39 offen. Jetzt 13 weitere Fächer gezielt zu prüfen. Bericht: docs/fachpruefung_4-6_20261106.md. Nächstes Fach 4-7.


## 2026-11-06 – Fach 4-7 nachgeprüft

- Sechs unsichere Buch-IDs in allen vier Originalpixelteilen von FOTO0028 erneut betrachtet. B00526 zu Martin Borré / Thomas Reintjes, *Warum Frauen schneller frieren*, B00528 zu Friederun Pleterski, *Ein Haus in Dalmatien*, B00535 zu Eugen Roth, *Ernst und heiter*, bibliografisch ergänzt und auf lesbar gesetzt.
- B00516, B00518 und B00540 bleiben wegen nicht sicherer Titellesung bzw. Buchabgrenzung unsicher, jeweils konkrete Fotoanweisung hinterlegt.
- Fach 4-7 mit 30 Einträgen jetzt 27 lesbar, 1 prüfen, 2 offen; nicht abgehakt. Gesamt 1048 Einträge (978 lesbar, 31 prüfen, 39 offen); noch 12 gezielte Fachprüfungen.
- Einzelbericht docs/fachpruefung_4-7_20261106.md, nächstes Fach 4-8.


## 2026-11-06 – Fach 4-8 gezielt nachgeprüft

- FOTO0029: vier native Git-Originalpixel-Ausschnitte betrachtet, nur B00545 und B00558 neu bewertet.
- B00545 als Richard Picker, *Das Ende vom Lied? Positionen eines Lebens zwischen Hitlerjugend, Psychotherapie und Kirche*, mit Czernin Verlagskatalog bestaetigt. B00558 als Arthur Schnitzler, *Lesebuch*, anhand des gruenen Buchrueckens und bibliografischem Werknachweis geklaert; Herausgeber/Auflage dieser konkreten Ausgabe nicht behauptet.
- Fach 4-8 mit 16/16 vorlaeufigen Eintraegen lesbar und vorlaeufig abgehakt. Originalfotos, Buchnummern und Positionen unveraendert.
- Gesamt 1048 Eintraege: 980 lesbar, 29 pruefen, 39 offen. 19 Faecher abgehakt, 11 noch gezielt zu pruefen. Siehe docs/fachpruefung_4-8_20261106.md. Naechstes Fach 5-1.


## 2026-11-06 – Gezielte Nachprüfung Fach 5-1

- Git-Original FOTO0030, alle vier Originalpixel-Ausschnitte gezielt für B00560, B00563, B00575 und B00579 eingesehen.
- B00560 als Marlo Morgan *Traumfänger* (Goldmann 43740; früher fälschlich Mario); B00575 als Donna Leon *Endstation Venedig* (detebe 22936); B00579 als Norman Levine *Django, Karfunkelstein & Rosen* (vorher *Django Kaffein & Rosen* falsch) durch Originalpixel und bibliografischen Abgleich gelöst.
- B00563 weiter offen: Buchbereich zwischen Håkan Nesser *Barins Dreieck* und Claudie Gallay *Die Brandungswelle*, Mörike-Eintrag noch nicht mit sicherem Titel belegbar; Einzelfoto des Titels/der Buchgrenze erforderlich.
- Fach 5-1 gezielt geprüft, nicht abgehakt: 22 Einträge, 21 lesbar, 1 offen. Gesamt 1048 IDs (983 lesbar, 27 prüfen, 38 offen), noch 10 gezielte Fachprüfungen. Einzelbericht docs/fachpruefung_5-1_20261106.md, nächstes Fach 5-2.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-2

- Nur B00585 und B00599 an den vorhandenen Git-Originalpixelteilen FOTO0031 Teil 01, 02 und 04 erneut geprüft.
- B00599 als Martha Grimes, *Fremde Federn / Inspektor Jury besucht alte Damen*, anhand der zwei eindeutig lesbaren Titel auf demselben Goldmann-Rücken bestätigt; jetzt lesbar.
- B00585 bleibt offen: ein überstehender Umschlag verdeckt den Bereich zwischen Jonas Jonasson *Mörder Anders* und Minette Walters *Wellenbrecher*. Frontalfoto ohne Umschlag und physische Fachzählung erforderlich.
- Fach 5-2: 19 vorläufig erfasste Bücher, 18 lesbar, 0 prüfen, 1 offen; nicht abgehakt. Gesamt 1048 Bucheinträge (984 lesbar, 26 prüfen, 38 offen = 64 unsicher). 19 Fächer vorläufig abgehakt, 9 weitere Fächer gezielt zu prüfen. Bericht `docs/fachpruefung_5-2_20261107.md`, nächstes Fach 5-3.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-3

- Nur B00600, B00604, B00614, B00615 und B00619 anhand der vier nativen Git-Ausschnitte von FOTO0032 behandelt; keine Originalfotos verändert.
- B00614 Julian Schutting, *Liebesgedichte* (dtv 6346) und B00619 Alexander Solschenizyn, *Zwischenfall* (dtv 857), durch Originalrücken und Bibliografie bestätigt → lesbar.
- B00615: bisherige Titellesung *Manchmal möchte ich eine Insel sein* korrigiert zu **Christine Nöstlinger – Manchmal möchte ich ein Single sein**, durch Originalpixel und offizielle Werkliste nachgewiesen → lesbar.
- B00600 Agatha Christie, Titel trotz Rückenzahl 822 nicht belegt → offen. B00604 ebenfalls offen: neben dunklem schlecht lesbaren Rücken steht noch ein erkennbarer gelber Rücken **Bertolt Brecht – Der gute Mensch von Sezuan** zwischen Ann Granger und Fabio Geda. Möglicher zusätzlicher Band/Positionsfehler, vor Ort zählen, keine neue ID oder Verschiebung geraten.
- Fach 5-3: 22 vorläufige Einträge (20 lesbar, 0 prüfen, 2 offen), nicht abgehakt. Gesamt 1048 (987 lesbar, 23 prüfen, 38 offen = 61 unsicher). 19 Fächer vorläufig abgehakt, 8 weitere gezielt zu prüfen. Bericht `docs/fachpruefung_5-3_20261107.md`, nächstes Fach **5-4**.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-4

- Nur B00627, B00631 und B00642 anhand der Git-Bilddaten FOTO0033 und bibliografischer Quellen geprüft. Teile 02 bis 04 zeigten die relevanten Rücken; keine anderen Buch-IDs oder Originalfotos verändert.
- B00627: Dieter Noll, *Die Abenteuer des Werner Holt*, auf dem roten Buchrücken lesbar. B00631: *Nie wieder Hummer* auf schwarzem Rücken, Autor **Hanns Marzini** anhand Buchkatalog geklärt. B00642: *Figuren*, **Melitta Breznik**, Sammlung Luchterhand, Titel und Nachname auf dem Rücken, voller Vorname aus Katalog.
- Alle drei auf `lesbar` umgestellt; keine ISBN, Auflagen oder Erscheinungsjahre für das vorhandene Exemplar behauptet. Fach **5-4**: 22/22 vorläufig lesbar, vorläufig abgehakt.
- Gesamt 1048 Datensätze (990 lesbar, 20 prüfen, 38 offen = 58 unsicher). 20 Fächer vorläufig abgehakt, 7 weitere gezielte Fachprüfungen. Dokumentation `docs/fachpruefung_5-4_20261107.md`. **Nächstes Fach erst auf „Weiter“: 5-5**, ausschließlich B00645 und B00647.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-5

- Nur B00645 (Position 2) und B00647 (Position 4) anhand der Git-Originalpixel von FOTO0034 Teil 01 geprüft, Teil 02 ergänzend betrachtet. Die anderen 19 Bucheinträge nicht erneut inventarisiert.
- B00645: dunkler reflektierender Buchrücken zwischen Saul Bellow *Der Regenkönig* und Thomas Bernhard *Ein Kind* bleibt unlesbar; frontales Foto/Titelblatt nötig.
- B00647: teilweise verdeckter schmaler Rücken zwischen Thomas Bernhard *Ein Kind* und John Irving *Die imaginäre Freundin* bleibt unlesbar; freigestelltes Detailfoto/Titelblatt nötig. Die sichtbare Diogenes-Nummer **23308** gehört laut Diogenes dem bereits erfassten Irving-Band B00648 und darf nicht für B00647 übernommen werden.
- Fach 5-5: **21** vorläufige Bucheinträge, **19 lesbar, 0 prüfen, 2 offen**; nicht abgehakt, nur neue Detailfotos zielführend. Gesamt unverändert **1048 Bucheinträge, 990 lesbar, 20 prüfen, 38 offen** (= 58 unsicher); 20 Fächer vorläufig abgehakt, 6 noch gezielt zu prüfen. Bericht `docs/fachpruefung_5-5_20261107.md`; nächstes Fach **5-6**.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-6

- Ausschließlich B00668, B00671, B00673, B00680, B00686 und B00688 anhand der vier einzeln geladenen nativen Git-Ausschnitte FOTO0035 geprüft; die übrigen Bücher und alle Originalfotos unverändert.
- B00668 **Hans Weigel – Die Leiden der jungen Wörter** (Hans-Weigel-Bibliografie); B00671 **Edith Kneifl (Hrsg.) – Tatort Kaffeehaus** (Falter-Verlagskatalog; vorher „Tarot“ falsch); B00673 **Daniel Keel / Daniel Kampa (Hrsg.) – Erlesene Verbrechen: Kriminalgeschichten** (detebe 23574); B00680 **Eva Zeller – Lampenfieber** (dtv 1238) identifiziert und auf `lesbar` gesetzt.
- B00686: „OSKAR WERNER“ auf großem weißem Rücken, genaue Autoren-/Titelzuordnung nicht sicher; B00688: „Frank Hoffmann“ auf spiegelndem blauen Band, eigentlicher Titel nicht entzifferbar. Beide bleiben `offen`; jeweils Titelblatt und blendfreies Rückenfoto nötig.
- Fach 5-6: **24 vorläufige Bucheinträge, 22 lesbar, 0 prüfen, 2 offen**, nicht abgehakt. Insgesamt **1048 Datensätze, 994 lesbar, 16 prüfen, 38 offen** (= 54 unsicher). **20** Fächer vorläufig abgehakt; **5** weitere gezielte Fachprüfungen. Einzelbericht `docs/fachpruefung_5-6_20261107.md`; **nächstes Fach 5-7**.

## 2026-11-07 – Gezielte Nachprüfung Fach 5-7

- Ausschließlich B00701 (Position 13) und B00706 (Position 18) anhand der einzelnen nativen Git-Bildteile FOTO0036 Teile 03/04 kontrolliert. Die anderen 16 Bucheinträge des Fachs sowie alle Originalfotos unverändert belassen.
- **B00701:** *Sabine Gruber – Stillbach oder Die Sehnsucht* durch lesbares „Sehnsucht“, C.H.Beck-Verlagsaufdruck sowie den eindeutigen Bildmotivvergleich des römischen Gebäudes mit der gebundenen Ausgabe und bibliografischen Nachweis bei C.H.Beck/Autorin identifiziert → nun `lesbar`. Keine konkrete Auflage des Exemplars behauptet.
- **B00706:** letzter breiter, blau/türkiser Band rechts von Håkan Nesser *Eine ganz andere Geschichte*; verblasste goldene Schrift kann nicht zuverlässig entziffert werden → bleibt `offen`; gezieltes Rückennahfoto plus Titelblatt/Impressum erforderlich.
- Fach 5-7: **18** vorläufige Einträge, **17 lesbar, 0 prüfen, 1 offen**, nicht abgehakt. Gesamt **1048 Einträge: 995 lesbar, 16 prüfen, 37 offen** (= 53 unsicher). **20** Fächer vorläufig abgehakt, **4** weitere Fächer erstmals gezielt zu prüfen. Bericht `docs/fachpruefung_5-7_20261107.md`; **nächstes Fach 5-8** (nur B00711, B00718, B00719).

## 2026-11-07 – Gezielte Nachprüfung Fach 5-8

- Ausschließlich **B00711, B00718 und B00719** an vier einzeln eingelesenen nativen Bildteilen von FOTO0037 geprüft. Original-JPEGs sowie alle anderen Bucheinträge, IDs, Fach- und Positionsangaben unverändert belassen.
- **B00718** James A. Michener, *Die Kinder von Torremolinos*, auf dem cremefarbenen Rücken im Teil 03 sicher lesbar und bibliografisch durch Goldmann-Katalog bestätigt → nun `lesbar`.
- **B00719** *Alice Miller – Du sollst nicht merken*, grüner Suhrkamp-Rücken `st 952` in Teil 03; der zuvor eingetragene Vorname **Arthur** war falsch und wurde anhand des Suhrkamp-Verlagskatalogs korrigiert → nun `lesbar`. Benachbarter *Arthur Miller – Hexenjagd* ist ein eigenes Exemplar; keine Positionsverschiebung.
- **B00711** Colleen McCullough am hellen Rücken zwischen Thomas Mann *Die Erzählungen* und Donna Leon *Das goldene Ei* erkennbar, Titel verdeckt → bleibt `offen`. Frontalfoto des freigestellten Rückens sowie Titelblatt benötigt, kein Titel geraten.
- Fach 5-8: **20 vorläufige Einträge, 19 lesbar, 0 prüfen, 1 offen**, nicht abgehakt. Gesamt **1048 Datensätze (997 lesbar, 14 prüfen, 37 offen = 51 unsicher)**. **20** Fächer vorläufig abgehakt, **3** weitere gezielt zu prüfen. Bericht `docs/fachpruefung_5-8_20261107.md`; **nächstes Fach 6-1**, nur B00727 und B00748.

## 2026-11-07 – Gezielte Nachprüfung Fach 6-1

- Ausschließlich **B00727 (Position 1)** und **B00748 (Position 22)** anhand der einzeln geladenen nativen Git-FOTO0038-Bildteile 01 bzw. 04 untersucht. Die weiteren 21 Bucheinträge des Fachs sowie sämtliche Originalfotos und Positionen unverändert belassen.
- **B00727:** am äußersten linken Fachrand schmaler dunkler Rücken, von **Leo Lukas – Das Leo Lukas Lesebuch** weitgehend verdeckt. Eigenständige Bandgrenze, Autor und Titel nicht sicher bestimmbar. **B00748:** schmaler dunkler Rücken mit roter btb-artiger Markierung zwischen **Axel Munthe – Das Buch von San Michele** und **Håkan Nesser – Sein letzter Fall**; Autor und Titel nicht lesbar. Beide bleiben `offen`, keine Schätzungen.
- Für beide Positionen **frontal fotografierter freigestellter Rücken**, **Titelblatt** und Kontrolle der physischen Buchgrenzen nötig; Nachbarbände als Positionsanker festhalten.
- Fach 6-1: **23 vorläufige Einträge, 21 lesbar, 0 prüfen, 2 offen**, nicht abgehakt. Gesamt weiterhin **1.048 Einträge, 997 lesbar, 14 prüfen, 37 offen** (= 51 unsicher). **20** Fächer vorläufig abgehakt, **2** weitere in der laufenden Fachprüfrunde zu bearbeiten. Einzelbericht `docs/fachpruefung_6-1_20261107.md`; **nächstes Fach 6-2**, ausschließlich **B00767**.

## 2026-11-07 – Gezielte Nachprüfung Fach 6-2

- Ausschließlich **B00767, Position 18**, anhand des einzeln geladenen Git-Originalpixel-Bildteils `FOTO0039_teil_04` untersucht. Die 19 bereits lesbaren Nachbarbücher und alle Originalfotos unverändert belassen.
- Auf dem blauen Rücken sind **Komarek/Kalmár**, *Schräge Vögel* und *Faszinierende Lebensentwürfe* erkennbar. Buchhandels-/Verlagsnachweis: **Alfred Komarek (Text)** und **János Kalmár (Fotografien)**, *Schräge Vögel: Faszinierende Lebensentwürfe*, Kremayr & Scheriau. Die unterschiedlichen Mitwirkendenrollen ausdrücklich dokumentiert; konkrete ISBN/Auflage des Exemplars nicht aus Katalogdaten übernommen.
- B00767 `pruefen` → `lesbar`; Fach **6-2 = 20 von 20 vorläufig lesbar**, vorläufig abgehakt. Gesamt **1048 Bucheinträge, 998 lesbar, 13 prüfen, 37 offen** (= 50 unsicher). **21** Fächer vorläufig abgehakt. Prüfbericht `docs/fachpruefung_6-2_20261107.md`.
- **Nur noch Fach 6-4 in der gezielten Nachprüfrunde**, ausschließlich **B00804** und **B00811**; noch keine weiteren Fächer geprüft. Physische Zähl-/Positionsfragen und Restunsicherheiten bleiben separat bestehen.

## 2026-11-07 – Gezielte Nachprüfung Fach 6-4 und Abschluss dieser Prüfrunde

- Ausschließlich **B00804 (Position 15)** und **B00811 (Position 22)** im Git-Original `FOTO0041` anhand der vorhandenen hochauflösenden Einzelbildteile (insbesondere Teile 03 und 04) geprüft. Keine anderen Buch-IDs in der Inventarliste verändert.
- **B00804:** Heinrich Böll und **Lew Kopelew** – *Warum haben wir aufeinander geschossen?*. „Koppel“ war eine Namensverlesung, der im Foto nur teilweise sichtbare Titel ist durch Bibliothekskatalog und Deutsche Biographie vervollständigt. Status `pruefen` → `lesbar`.
- **B00811:** Peter Handke – *Die linkshändige Frau*. Dunkelblauer Rücken **suhrkamp taschenbuch st 560** zwischen Böll *Der Zug war pünktlich* und Harris *Die Hannibal-Lecter-Romane* im Git-Foto. DLA Marbach Katalog und Vergleichsfoto einer st-560-Ausgabe bestätigen die Identifikation; die konkrete Auflage bleibt offen. Status `offen` → `lesbar`.
- Fach 6-4: **24/24 lesbar**, vorläufig abgehakt. **Gesamter Inventarstand 1.048 vorläufige Bucheinträge, 1.000 lesbar, 12 prüfen, 36 offen**, somit **48 unsichere**. **22 Fächer vorläufig abgehakt, 28 mit Restunsicherheiten**. **Kein Fach dieser gezielten Nachprüfrunde mehr unbearbeitet.** Zwei besondere Zähl-/Positionsfragen (3-3 und 5-3) und bereits dokumentierte fehlende Fachdetailfotos bleiben separat bestehen.
- Alle Originalfotos, Buch-IDs, Positionen und Fotoreferenzen unverändert. Vollständiger Nachweis `docs/fachpruefung_6-4_20261107.md`. Nächster Projektschritt **nur nach neuer Aufforderung**: Nachfotoliste der 48 noch unsicheren Datensätze und gesonderte physische Fachzählungen aus den vorhandenen Git-Befunden ableiten.

