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
