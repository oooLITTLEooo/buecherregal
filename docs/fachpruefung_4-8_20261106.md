# Gezielte Nachprüfung Fach 4-8 – 06.11.2026

## Bildquellen und Umfang

- Original aus Git `bilder/originale/PXL_20261105_151457999.jpg` (Foto-ID `FOTO0029`), laut `daten/fotos.csv` 8160 × 4590 Pixel.
- Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0029_teil_01.jpg.base64.txt`, `_teil_02.jpg.base64.txt`, `_teil_03.jpg.base64.txt` und `_teil_04.jpg.base64.txt` betrachtet.
- Ausschließlich die bisher unsicheren Datensätze **B00545** und **B00558** gezielt analysiert. Die übrigen 14 als `lesbar` markierten Einträge nicht systematisch neu geprüft.

## Einzelentscheidungen

| Buch-ID | Pos. | Bildbefund und bibliografischer Abgleich | Status |
| --- | ---: | --- | --- |
| B00545 | 3 | FOTO0029 Teil 01: Buch von **Richard Picker – Das Ende vom Lied?** zwischen Ruth Rendell *Der Sonderling* (Pos. 2) und Eva Rossmann *Evelyns Fall* (Pos. 4) lesbar. **Czernin Verlag** auf dem Rücken erkennbar. Aus dem Verlagskatalog stammt der vollständige Titel **Das Ende vom Lied? Positionen eines Lebens zwischen Hitlerjugend, Psychotherapie und Kirche**. | **lesbar** |
| B00558 | 16 | FOTO0029 Teil 04: ganz rechts **grüner, breiter Rücken „Schnitzler Lesebuch“** klar lesbar nach Sándor Márai *Bekenntnisse eines Bürgers* (Pos. 15). Werke von **Arthur Schnitzler**, bibliografisch als `Lesebuch` vorhanden. Der genaue Herausgeber sowie Jahrgang/Verlagsausgabe dieses grünen Exemplars sind **nicht** am Rücken gesichert. Nicht als die neuere Fischer-Ausgabe *Das große Lesebuch* inventarisiert. | **lesbar** |

### Bibliografische Belege

- [Czernin Verlag, Das Ende vom Lied? – Richard Picker](https://www.czernin-verlag.com/buecher/sachbuch?page=2&sort=datum_asc&view=list) mit Verlags-ISBN 978-3-7076-0225-8. Diese ISBN ist ein **Katalognachweis, nicht eine direkt am fotografierten Exemplar überprüfte Nummer**.
- [Bibliografischer Volltitel zu Richard Picker](https://diebuchsuche.at/buch-isbn-9783707602258.html).
- [Arthur Schnitzler, Lesebuch (Fischer 1978) – antiquarischer Ausgabennachweis](https://www.abebooks.com/book-search/title/lesebuch/author/schnitzler-arthur/). Er belegt den Autoren und einen Werk-/Ausgabentitel, **nicht** die Identität der konkreten grünen Ausgabe.
- [Fischer Verlag zu Arthur Schnitzler als Autor von Lesebüchern](https://www.fischerverlage.de/autor/arthur-schnitzler-1002047). Die moderne Ausgabe *Das große Lesebuch* wird bewusst nicht auf das abgebildete Buch übertragen.

## Git-Nachführung

- `daten/buecher.csv`: nur B00545 um den belegten vollständigen Buchtitel ergänzt und auf lesbar gesetzt sowie B00558 mit Autor **Arthur Schnitzler** und Titel **Lesebuch** als lesbar eingetragen. Beweise und Editionsvorbehalt jeweils im Bemerkungsfeld.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: beide Nachprüfungen einzeln mit Bildbezug und Quellen dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 4-8 mit 16 lesbar, 0 prüfen, 0 offen als `vorlaeufig_abgehakt` gesetzt.
- `daten/fachstatus.csv`, Gesamtprüfplan, Protokoll und Inventurfortschritt synchronisiert.
- **Keine Originalfotos, Buch-IDs, physische Positionen oder anderen Buchzeilen verändert.**

## Gesamtstand und nächste Prüfung

- Fach 4-8: **16** vorläufige Bücher, **16 lesbar**, **0 prüfen**, **0 offen**. Vorläufig abgehakt.
- Gesamtes Inventar: **1048** vorläufige Einträge, **980 lesbar**, **29 prüfen**, **39 offen** (= **68** verbleibende Unsicherheiten).
- **19** Fächer vorläufig abgehakt, **11** weitere noch gezielt zu prüfen, **20** bereits nachgeprüfte mit Restunsicherheiten; Fach 3-3 separat wegen Zähl-/Positionsabweichung.
- **Nächstes Fach erst auf „Weiter“:** Fach **5-1**, nur die vier unsicheren IDs **B00560, B00563, B00575, B00579**.
