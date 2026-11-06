# Fachprüfung 7-2 – 06.11.2026

## Umfang und Fotobelege

- In diesem Durchgang **ausschließlich Fach 7-2** geprüft.
- Originalfoto: `bilder/originale/PXL_20261105_151628605.jpg`, Foto-ID `FOTO0047`, 8160 × 4590 Pixel.
- Die vier originalpixelbasierten Ausschnitte `daten/bildanalyse/fullres/FOTO0047_teil_01.jpg.base64.txt` bis `FOTO0047_teil_04.jpg.base64.txt` wurden visuell nacheinander mit `daten/buecher.csv` abgeglichen.
- **19** vorläufige physische Bucheinträge `B00933`–`B00951` mit Positionen 1–19, von links nach rechts. Keine Einträge entfernt oder hinzugefügt.

## Zwei zuvor unklare Einträge bestätigt

| Buch-ID | Fachposition | Autor | Titel | Fotobeleg |
| --- | ---: | --- | --- | --- |
| `B00944` | 12 | Eva Rossmann | **Männerfreundschaft** | `FOTO0047`, Teil **3**: schmaler weißer Rücken, Schrift direkt lesbar |
| `B00951` | 19 | Joachim Meyerhoff | **Wann wird es endlich wieder so, wie es nie war** | `FOTO0047`, Teil **4**: blauer Rücken, Autoren- und Titelschrift lesbar |

Beide Einträge waren zuvor `pruefen` und hatten bereits korrekte Autor-/Titelfelder. Es wurde **nur der Identifikationsstatus `lesbar`** gesetzt und die Bildbeleg-Notiz konkretisiert. Buch-IDs, Titel, Autorendaten, Positionen und Originalfoto-Pfade unverändert.

## Abgleich der übrigen Einträge

- Die weiteren **17** bereits als `lesbar` notierten Titel lassen sich in den sichtbaren Ausschnitten nachvollziehen.
- Beispielhafte Belege: B00933 John Irving *Witwe für ein Jahr* (Teil 1); B00934 Minette Walters *Der Außenseiter* (Teil 1); B00935 Stephanie Doyon *Die wunderbare Welt des Francis Pinkham* (Teil 1); B00936 Daniel Glattauer *Darum* (Teil 2); B00937 Ann Granger *Tote kehren nicht zurück* (Teil 2); B00938 John Grisham *Die Erbin* (Teil 2); B00942 Tamar Noort *Die Ewigkeit ist ein guter Ort* (Teil 3); B00946 Thomas Mann *Der Tod in Venedig* (Teil 3); B00948 Adriana Altaras *Das Meer und ich waren im besten Alter* (Teil 4); B00949 Mary Higgins Clark *Mein ist die Stunde der Nacht* (Teil 4).
- Ein gesondertes zusätzliches Titel- oder Autorenkorrekturbedürfnis wurde in diesem Fach nicht festgestellt.
- Noch nicht sichtbare Innenseiten lassen sich naturgemäß nicht anhand des Regalfotos verifizieren; dies ist eine Prüfung des **sichtbaren Ist-Bestands**, keine externe bibliografische Prüfung.

## Änderungen im Git

- `daten/buecher.csv`: Nur B00944 und B00951 von `pruefen` auf `lesbar` umgestellt, mit Bildteil-Nachweis.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Die beiden Prüfentscheidungen auf `korrigiert_und_lesbar` gesetzt, mit konkreter Begründung.
- `daten/fachstatus.csv`: Veraltete Angabe `Einzelbucherfassung ausstehend` durch den aktuellen Prüfstand ersetzt.
- Bildoriginal und byteidentische benannte Kopie **nicht** verändert. Kein anderes Fach bearbeitet, keine physische oder alphabetische Umsortierung.

## Stand nach Fach 7-2

- **19/19** Bucheinträge mit Status `lesbar`; **0** `offen` und **0** `pruefen` innerhalb dieses Faches.
- Global unveränderte vorläufige Exemplaranzahl: **1048**, nun **946 `lesbar`**, **61 `pruefen`**, **41 `offen`** (102 ungeklärt).
- Fortsetzung erst auf weiteres `Weiter` und dann **nur Fach 7-3**.
