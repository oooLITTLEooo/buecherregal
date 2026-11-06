# Arbeitsprotokoll

## 2026-11-06 – Projektstart

- Repository `oooLITTLEooo/buecherregal` als zentrale Ablage festgelegt.
- Gewünschte Nummerierung: links beginnend, pro Spalte von oben nach unten.
- Buchdatenmodell: Autor, Titel, Fachstandort und Position innerhalb des Fachs.
- Gewünscht: Ablage sämtlicher Original- und später generierter Bilder.
- Initial festgestellt: Repository-Sichtbarkeit **public**.
- Projektstruktur und leere Inventardateien angelegt; Bild- und Bucherfassung noch ausständig.

## 2026-11-06 – Sichtbarkeit bestätigt

- Nutzer hat Repository auf **private** gestellt.
- GitHub-Metadaten erneut abgefragt; Sichtbarkeit **private** bestätigt.
- Foto- und Inventarerfassung kann beginnen. Noch keine Regalfotos übermittelt oder archiviert.

## 2026-11-06 – Übersichtsfoto 1

- Übersichtsfoto `58245.jpg` (1536 × 864 Pixel) im Chat empfangen.
- In `daten/fotos.csv` als `F0001` verzeichnet.
- Acht senkrechte Regalspalten von links nach rechts sichtbar (vorläufige Sichtprüfung).
- Zahl der Fächer je Spalte wird anhand weiterer Fotos geprüft; noch keine definitive Nummerierung.
- Keine Einzeltitel aus der Übersicht geraten; weitere Detailfotos abwarten.
- **Archivierungsstatus:** Originaldatei ist im Chat vorhanden, GitHub-Bildupload steht noch aus; Bild daher nicht als in Git archiviert kennzeichnen.

## 2026-11-06 – Sechs weitere Detailfotos

- Sechs Fotos im Chat erhalten: Originalnamen `58246.jpg` bis `58251.jpg`.
- Anhand des Gesamtbilds zugeordnet: `Regal_1-5.jpg` bis `Regal_1-8.jpg`, danach `Regal_2-1.jpg`, `Regal_2-2.jpg`.
- Keine identischen oder offensichtlich mehrfach fotografierten Regalfächer in diesem Paket erkannt. Überschneidungen am oberen/unteren Bildrand sind kein Duplikat.
- SHA-256-Prüfsummen und einfache Bild-Hashes in `daten/fotos.csv` aufgenommen.
- `daten/buecher.csv`: erster Durchgang mit 106 vorläufigen Buchpositionen; dabei 18 als offen/zu prüfen markiert. Die Feinzuordnung einzelner verdeckter Bücher bleibt vorbehaltlich weiterer Ansichten.
- `daten/fachstatus.csv` angelegt: `1-1` bis `1-3` laut Übersichtsbild leer, `1-4` enthält Lampe, `1-5` bis `1-8` und `2-1` bis `2-2` fotografiert.
- **Nächstes Detailfoto:** `Regal_2-3.jpg`, danach `Regal_2-4.jpg` usw.
- **Wichtig:** Die Bilder liegen im Chat vor, aber die Original-JPEG-Binärdateien wurden noch nicht nach GitHub übertragen; die Fotoeinträge tragen korrekt `upload_status=ausstehend`. Die Dateinamen in Git sind derzeit Soll-Namen, keine vorhandenen Bilddateien.

## 2026-11-06 – Zweite Spalte vollständig fotografiert

- Sechs neue Originalfotos erhalten: `58253.jpg` bis `58258.jpg`, ohne identische Dubletten; Zuordnung `2-3` bis `2-8`.
- Foto-IDs `F0008` bis `F0013` mit Soll-Dateinamen `Regal_2-3.jpg` bis `Regal_2-8.jpg` in `daten/fotos.csv` aufgenommen; SHA-256 und konsistente perzeptuelle Hashes dokumentiert.
- `daten/fachstatus.csv` aktualisiert. In Spalte 2 sind alle acht Fächer fotografiert.
- `daten/buecher.csv`: 121 zusätzliche vorläufige Buchpositionen (20 + 22 + 17 + 17 + 28 + 17). Insgesamt derzeit 227 Positionen, davon 39 mit Status `offen` oder `pruefen`.
- Die Inventarzahlen sind ein erster Durchgang und können sich durch verdeckte oder mehrfach sichtbare Buchrücken noch ändern. Der ursprüngliche Standort bleibt unverändert dokumentiert.
- **Nächstes Detailfoto:** `Regal_3-1.jpg`, anschließend innerhalb von Spalte 3 von oben nach unten.
- **Originalfotos:** alle 13 JPEGs im Chat vorhanden und lokal mit korrekten Namen in `buecherregal_fotos_bis_2-8_2026-11-06.zip` zusammengestellt. **Upload der Binärdateien nach GitHub weiter ausstehend**, deshalb `upload_status=ausstehend`.

## 2026-11-06 – Dritte Spalte, Fächer 3-1 bis 3-6

- Sechs weitere Detailfotos entgegengenommen: `58261.jpg`, `58262.jpg`, `58264.jpg`, `58265.jpg`, `58266.jpg`, `58267.jpg`.
- Im privaten GitHub-Inventar registriert als `Regal_3-1.jpg` bis `Regal_3-6.jpg` (`F0014`–`F0019`); keine Foto-Dubletten zu den 13 älteren Aufnahmen festgestellt.
- Die Lücke der Kamera-Dateinummer `58263.jpg` bedeutet **keine Regalfachlücke**. Die Fächer 3-1 bis 3-6 sind inhaltlich fortlaufend.
- SHA-256-Prüfsummen aus den Original-JPEG-Bytes verifiziert; für alle 19 Aufnahmen perzeptuelle Hashwerte nach einheitlichem Verfahren neu berechnet.
- 135 weitere vorläufige Buchpositionen aus den sechs Fächern erfasst; nun insgesamt **362**, davon **68** mit `offen`/`pruefen`.
- Erfassungsstand für **Spalte 3**: Fächer 3-1 bis 3-6 fotografiert, 3-7 und 3-8 noch ausständig. Die noch ausständigen Fächer basieren auf dem bisherigen Acht-Fächer-Muster und sind bei Detailansichten zu prüfen.
- Alle 19 unveränderten JPEG-Dateien inklusive früherer Fotos zusätzlich im ZIP `buecherregal_fotos_bis_3-6_2026-11-06.zip` mit Git-Zielnamen gesichert; ZIP-Datei im Chat bereitgestellt.
- Bilddateien selbst weiterhin **nicht** im GitHub-Repository. Eintrag `upload_status=ausstehend` bleibt bis zum erfolgreichen Upload bestehen.

## 2026-11-06 – Git-Workflow korrigiert; Public ist beabsichtigt

- Nutzer erklärt, dass die Umstellung des Repositories auf **public absichtlich** erfolgte, damit andere die Sammlung einsehen können.
- Vorgabe geändert: **Originalfotos zuerst in Git hochladen und verifizieren, erst danach einzelne Buchrücken vertieft analysieren und Inventar vervollständigen**.
- Sechs weitere JPEGs erhalten: `58268.jpg` bis `58273.jpg`.
- Zuordnung anhand der Gesamtaufnahme und Fotoreihenfolge: `3-7`, `3-8`, `4-1`, `4-2`, `4-3`, `4-4`, Git-Namen `Regal_3-7.jpg` usw.
- Identische Fotos im neuen Paket nicht festgestellt; SHA-256-Prüfsummen in `daten/fotos.csv`.
- Alle 25 unveränderten Originale als ZIP `buecherregal_fotos_bis_4-4_2026-11-06.zip` mit Manifest gesammelt; alle 25 SHA-256-Werte geprüft und 25 individuelle Dateien bestätigt.
- **Noch nicht hochgeladen:** 25 Original-JPEGs. Vorhandene GitHub-Verbindung schreibt Inventardateien, aber kann die lokalen Binärdateien nicht direkt hochladen. Statt voreilig `im_git` zu setzen, verbleibt der Status auf `ausstehend`.
- Das bereits im Repository gespeicherte Skript `scripts/import-fotos.sh` ermöglicht den überprüften Import des ZIPs aus einem Git-Clone mit Push-Rechten.
- Der detaillierte Erfassungsdurchgang der sechs neu erhaltenen Fächer wartet gemäß neuem Ablauf auf die bestätigte Git-Bildablage. Vorläufiges Buchinventar weiterhin 362 Datensätze, davon 68 zu prüfen.

## 2026-11-06 – Neue Detailfotos 4-5 bis 5-2 und Zusatzvermerk

- Sechs Originalbilder `58274.jpg` bis `58279.jpg` im Chat erhalten.
- Standort: `4-5`, `4-6`, `4-7`, `4-8`, `5-1`, `5-2`, Dateinamen entsprechend `Regal_4-5.jpg` usw.
- Exakte Datei-SHA-256-Prüfsummen und perzeptuelle Hashwerte in `daten/fotos.csv` registriert (`F0026` bis `F0031`). Insgesamt 31 Aufnahmen, alle mit unterschiedlichen SHA-256-Werten. Keine nahezu identischen Bilder gefunden (keine pHash-Distanzen <= 9).
- Umbenannte, bytegetreu erhaltene Originale zusammen mit bisherigen Fotos in `buecherregal_fotos_bis_5-2_2026-11-06.zip` archiviert, inklusive `FOTO_MANIFEST.csv` und Importhinweisen. ZIP auf Integrität geprüft.
- Foto-Status: Spalte 4 vollständig; Spalte 5 Fächer 1 und 2 fotografiert; **als Nächstes 5-3**.
- Der Nutzer hat ausdrücklich notiert: **`3.5 noch`**. Dieser Wortlaut ist als Erinnerung unverändert zu erhalten und am Ende der Antwort wiederzugeben. Regal 3-5 ist in `daten/fachstatus.csv` schon als fotografiert erfasst; Bedeutung des neuen Hinweises noch offen.
- Gemäß vereinbartem Arbeitsablauf werden die zusätzlichen Bücher erst nach Bildarchivierung im Git vertieft inventarisiert.
- Bild-Binärdateien weiterhin nicht nach GitHub hochgeladen, obwohl Foto-Metadaten dort dokumentiert sind. Zum Upload ist der einmalige Lauf von `scripts/import-fotos.sh` mit dem neuen ZIP im Git-Clone vorgesehen.

## 2026-11-06 – Spalte 5 vollständig, weitere Erinnerung

- Sechs neue Detailfotos im Chat erhalten: `58280.jpg`–`58285.jpg`, den Fächern `5-3`–`5-8` zugeordnet und nach `Regal_5-3.jpg`–`Regal_5-8.jpg` benannt.
- `daten/fotos.csv` um Foto-IDs `F0032`–`F0037` ergänzt; SHA-256, Größe und pHash aus den Original-Dateibytes überprüft.
- Gesamt: **37 einzigartige Original-JPEG-Dateien**, 1 Übersicht und 36 Fachfotos. Zwischen allen 37 Bildern keine identischen SHA-256-Werte und keine pHash-Distanzen unter 10 (kleinste Distanz 12). Alle 37 Bilddateien wurden unverändert und korrekt benannt im ZIP `buecherregal_fotos_bis_5-8_2026-11-06.zip` gesichert; ZIP-Integrität und Inhalt geprüft.
- **Spalte 5 ist fotografisch vollständig.** Nächste Aufnahme `6-1`.
- Neue wortgetreue Nutzer-Erinnerung: **`2.5 noch`**. Der bereits bestehende Vermerk **`3.5 noch`** bleibt ebenfalls offen. Beide stehen in `daten/offene_punkte.csv`; sie werden als offene Aufgaben behandelt, nicht automatisch als fehlende Fotos.
- Die Binärfotos sind derzeit **noch nicht in GitHub hochgeladen**. Die gespeicherten Foto-Metadaten tragen `upload_status=ausstehend`; ein Git-Import des aktuellen ZIPs erfolgt über das vorhandene `scripts/import-fotos.sh`.
- Die vorhandene Buchinventarliste (362 vorläufige Positionen, 68 offen/zu prüfen) bleibt vorerst unverändert; neue Detailanalyse folgt nach Git-Bildarchivierung.
