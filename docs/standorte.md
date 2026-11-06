# Standort- und Erfassungsregeln

## Regalfachnummerierung

`X-Y` bedeutet **Spalte X von links**, **Fach Y von oben**. Beispiel `1-5`: erste Spalte, fünftes Fach von oben.

Die **tatsächliche Zahl** von Spalten und Fächern ist nicht vorgegeben und wird anhand der **im Git-Repository liegenden Gesamtübersicht** und Detailfotos bestimmt.

## Bücher innerhalb eines Faches

Jedes physische Buchexemplar erhält einen eigenen Datensatz. `position_im_fach` zählt sichtbare Bücher **von links nach rechts**, beginnend bei `1`. Mehrfach vorhandene Exemplare eines Titels sind eigene Einträge.

`daten/buecher.csv` enthält nach abgeschlossener Prüfung: `buch_id`, `autor_nachname`, `autor_vorname`, `titel`, `standort`, `position_im_fach`, `identifikationsstatus`, `foto_referenz`, `bemerkungen`.

Nicht lesbare Angaben als `offen` oder `pruefen` kennzeichnen und mit der Fotoquelle verbinden, nicht erfinden.

## Bilder

Alle Originalfotos zunächst aus dem tatsächlichen **aktuellen Git-Bestand** erfassen, unter `bilder/originale/` mit **unverändertem Dateinamen** ablegen; Dubletten und Standorte überprüfen. Danach **Kopien** unter `bilder/umbenannt/` ablegen: Zielnamen `Regal_Gesamt`, `Regal_X-Y`, ggf. `Regal_X-Y_02`, mit tatsächlicher Dateierweiterung. Keine Position allein aus Uhrzeit oder ursprünglichem Dateinamen ableiten.

Bei einem Foto, das Teile eines Nachbarfachs zeigt, Bücher nur dem richtigen Fach zuweisen.

## Spätere alphabetische Sortierung

Erst nach Abschluss des vollständigen Ist-Inventars und erneuter Anweisung: **Autoren-Nachname A–Z**, bei Gleichstand Vorname, danach Titel. Die Fachabfolge läuft spaltenweise von links nach rechts und innerhalb jeder Spalte von oben nach unten.

Siehe [Übergabe für neuen Chat](NEUER_CHAT_BESTANDSANALYSE.md).
