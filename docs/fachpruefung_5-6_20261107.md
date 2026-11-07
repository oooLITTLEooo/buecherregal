# Gezielte Nachprüfung Fach 5-6 – 07.11.2026

## Quellen und Umfang

- Original-Foto im Git: `bilder/originale/PXL_20261105_151523610.jpg` (`FOTO0035`, 8160 × 4590 Pixel laut `daten/fotos.csv`), zugeordnete Kopie `bilder/umbenannt/Regal_5-6.jpg`.
- Vier bereits vorhandene native Originalpixel-Teile `daten/bildanalyse/fullres/FOTO0035_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` einzeln gelesen. Für die sechs Fälle sind Teile 02–04 relevant.
- **Nur** B00668, B00671, B00673, B00680, B00686 und B00688 aktualisiert. Die anderen 18 Bucheinträge von Fach 5-6 nicht erneut inventarisiert. Keine Foto-, ID-, Reihenfolge- oder Positionsänderung.

## Ergebnisse

| Buch-ID | Vorläufige Position | Direkt am Git-Foto / bibliografische Ergänzung | Entscheidung |
| --- | ---: | --- | --- |
| **B00668** | 4 | FOTO0035 Teil 02 links: schmaler Rücken **Weigel – Die Leiden der jungen …**. Die Hans-Weigel-Bibliografie bestätigt den vollständigen Titel **Die Leiden der jungen Wörter** (Untertitel *Ein Antiwörterbuch*). | **lesbar** |
| **B00671** | 7 | FOTO0035 Teil 02: orangefarbener Rücken **TATORT Kaffeehaus**, oben **Kneifl (Hg.)**. Nach Falter-Verlag **Edith Kneifl** als Herausgeberin. Bisheriges „Tarot Kaffeehaus“ war eine Verlesung. | **lesbar**, Titel korrigiert |
| **B00673** | 9 | FOTO0035 Teil 02: weißer detebe-Rücken **23574 – Erlesene Verbrechen – Kriminalgeschichten**. Buchkatalog nennt **Daniel Keel und Daniel Kampa** als Herausgeber. Dies ist ein Sammelband, kein Werk eines einzelnen Verfassers. | **lesbar** |
| **B00680** | 16 | FOTO0035 Teil 03: schmaler Rücken **Zeller: Lampenfieber**, dtv **1238**. Bibliografische Belege identifizieren **Eva Zeller**. | **lesbar**, Vorname ergänzt |
| **B00686** | 22 | FOTO0035 Teil 04: großer weißer Rücken mit **OSKAR WERNER** und **J&V**. Es ist nicht verifizierbar, ob dies Werktitel, Gegenstand oder Verfasser ist; genauer Buchtitel fehlt. | **offen**, kein Titel geraten |
| **B00688** | 24 | FOTO0035 Teil 04 ganz rechts: bläulicher Band mit **Frank Hoffmann** lesbar, goldene Kursive unter spiegelnder Plastikfolie nicht sicher entzifferbar. | **offen**, kein Titel geraten |

### Bibliografische Kontrollquellen

- B00668: [Hans-Weigel-Bibliografie](https://www.hans-weigel.at/bibliographie/) sowie [Österreichische Nationalbibliothek](https://data.onb.ac.at/nlv_lex/perslex/W/Weigel_Hans.htm).
- B00671: [Falter-Verlagskatalog, TATORT-Reihe (PDF)](https://www.falterverlag.at/downloads/Buecherpost20.pdf) und [ORF Ö1, Tatort Kaffeehaus](https://oe1.orf.at/artikel/276700/Tatort-Kaffeehaus).
- B00673: [Stadtbibliothek Salzburg, Erlesene Verbrechen / detebe 23574](https://buch.stadt-salzburg.gv.at/Mediensuche/Einfache-Suche?focusModule=searchmodule&id=&page=2&search=verbrechen&top=y), [Buch-Sammler mit Herausgeberangaben](https://www.buch-sammler.de/verlag/diogenes-falsch.3596/5), [Buchhandel-Katalog](https://diebuchsuche.at/buch-isbn-9783257235746.html). Die beiden Daniel sind **Herausgeber**, nicht Autoren aller enthaltenen Geschichten.
- B00680: [CiNii, Eva Zeller und dtv 1238](https://ci.nii.ac.jp/author/DA04970461) und [Munzinger-Biografie, Eva Zeller](https://www.munzinger.de/register/portrait/biographien/eva%2Bzeller/00/17419).

Bibliografische Katalogangaben dienen zur Identifikation von Werken und Personen, **nicht** als Nachweis einer exakten Auflage oder des Erscheinungsjahrs der abgebildeten Exemplare.

## Notwendige gezielte Nachfotos

- **B00686:** Das große weiße Buch mit „OSKAR WERNER“ (zwischen Ernst Jandl *Lechts und rinks* und Erich Fried *Liebesgedichte*) herausziehen; **Titelblatt**, Verfasserangabe und frontalen Rücken aufnehmen. „Oskar Werner“ nicht ungeprüft als Autor und Titel zugleich interpretieren.
- **B00688:** Das letzte Buch ganz rechts hinter Erich Fried *Liebesgedichte*, mit Namenszug **Frank Hoffmann**, **ohne Reflexion der Plastikfolie** frontal fotografieren, wenn möglich Umschlag/Folie vorsichtig beiseite nehmen; zusätzlich **Titelblatt** und gegebenenfalls Impressum aufnehmen.

## Git-Nachführung

- `daten/buecher.csv`: nur sechs genannte Buch-IDs geändert; vier sichere Bücher auf `lesbar`, bei zwei offenen Einträgen lediglich Nachfotobedarf und sichtbaren Befund präzisiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: genau diese sechs Nachprüfungen mit Bild- und Quellenbelegen dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 5-6 = **24 vorläufige Bucheinträge, 22 lesbar, 0 prüfen, 2 offen**; `neues_detailfoto_bei_bedarf`, zweite Prüfung `ja`, offene IDs B00686 und B00688.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md` nachgeführt.
- Keine Originalbilder, Positionskopien, sonstigen Buch-IDs, Positionsnummern oder Fotoreferenzen verändert.

## Bilanz und Fortsetzung

- Fach **5-6**: 24 Einträge, 22 lesbar, 0 prüfen, 2 offen – **noch nicht abgehakt**.
- Gesamt **1048** vorläufige Einträge: **994 lesbar, 16 prüfen, 38 offen** (54 unsicher).
- **20** Fächer vorläufig abgehakt; **5** weitere erstmals gezielt zu prüfen; **25** bereits nachgeprüft mit Restunsicherheiten (plus Fach 3-3 mit Zähl-/Positionsbedarf).
- **Nächstes Fach erst bei einem neuen „Weiter“: 5-7**, ausschließlich **B00701** und **B00706**.
