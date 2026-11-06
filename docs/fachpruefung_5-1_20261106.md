# Gezielte Nachprüfung Fach 5-1 – 06.11.2026

## Bildgrundlage und Umfang

- Git-Original `bilder/originale/PXL_20261105_151503183.jpg` (FOTO0030, 8160 × 4590 Pixel nach `daten/fotos.csv`).
- Alle vier im Git versionierten nativen Originalpixelbereiche `daten/bildanalyse/fullres/FOTO0030_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` gesichtet.
- Nur die vier bislang unsicheren Buch-IDs **B00560, B00563, B00575, B00579** neu bewertet; 18 andere lesbar erfasste Einträge nicht erneut systematisch geprüft.

## Einzelfallentscheidungen

| Buch-ID | Position | Originalpixel-Befund / bibliografischer Nachweis | Neuer Status |
| --- | ---: | --- | --- |
| **B00560** | 2 | Teil 01: rötlicher Goldmann-Rücken **Marlo Morgan – Traumfänger**, sichtbare Reihennummer **43740**. Der bisherige Vorname `Mario` war eine Verlesung. Reihennummer und Autor im Buchkatalog bestätigt. | **lesbar** |
| **B00563** | 5 | Teil 01 rechts / Teil 02 links: schmaler, teils überlagerter Bereich zwischen Håkan Nesser *Barins Dreieck* und Claudie Gallay *Die Brandungswelle*. Der bisherige Autor **Eduard Mörike** bleibt vorläufig eingetragen, die konkrete Werkausgabe und der Titel sind aus diesen Ausschnitten nicht sicher bestimmbar. | **offen** |
| **B00575** | 17 | Teil 03: heller schmaler **detebe 22936**-Rücken zwischen Donna Leon *In Sachen Signora Brunetti* und *Die dunkle Stunde der Serenissima*. Verlagsreihe **22936** ist bibliografisch eindeutig **Donna Leon – Endstation Venedig**. Kein Auflagenjahr für dieses Exemplar behauptet. | **lesbar** |
| **B00579** | 21 | Teil 04: deutlich **Norman Levine** und *Django, Karfunkelstein & Rosen* auf dem Buchrücken. Korrektur des bisherigen Titels `Django Kaffein & Rosen`. Passende Claassen-Buchausgabe bestätigt. | **lesbar** |

### Bibliografische Kontrollquellen

- B00560: [Buchhandelskatalog – Marlo Morgan, Traumfänger (43740)](https://www.thalia.at/shop/home/artikeldetails/A1000405769) und [Bibliothekskatalog](https://www.bibliotheca-marci-iacobi.ch/unternehmen/einfachesuche.php?Oui=Oui&Showtime=000010835).
- B00575: [Ausgabenübersicht detebe 22936](https://www.buch-sammler.de/ausgabe/endstation-venedig.2721) und [Buchhandelstitel Donna Leon, Endstation Venedig](https://www.morawa.at/detail/ISBN-9783257229363/Leon-Donna/Endstation-Venedig).
- B00579: [Buchhandelskatalog Claassen-Ausgabe 1987](https://diebuchsuche.at/buch-isbn-9783546459655.html) und [Ausgaben-Katalog](https://knihobot.cz/g/3801248).

Die angegebenen Ausgaben und Nummern sind **bibliografische Kontrollbelege**; Auflage oder Zustand des individuellen Exemplars wurden nicht automatisch aus Katalogangaben abgeleitet.

## Nötiges Nachfoto

Nur noch **B00563**: den Rücken direkt **zwischen Håkan Nesser *Barins Dreieck* und Claudie Gallay *Die Brandungswelle*** frontal aufnehmen, gegebenenfalls den Band vorsichtig herausziehen und **Titelblatt sowie Buchgrenze** fotografieren. Der bisherige Autorenname Eduard Mörike ist zu verifizieren, kein Werktitel geraten.

## Git-Nachführung

- `daten/buecher.csv`: B00560 (Marlo Morgan), B00575 (Donna Leon) und B00579 (Norman Levine) inhaltlich korrigiert und auf `lesbar` gesetzt. Bei B00563 nur den Nachprüfbefund und Nachfotobedarf präzisiert, Status `offen` unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: vier Entscheidungen direkt am Foto dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 5-1 von `gezielte_pruefung` zu `neues_detailfoto_bei_bedarf`, 21 lesbar, 0 prüfen, 1 offen.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md` aktualisiert.
- Originalfoto, Kopie, andere Buchdatensätze, IDs, Fach- und Positionsnummern nicht verändert.

## Bilanz und nächste Prüfung

- Fach 5-1: **22** vorläufig erfasste Bücher, **21 lesbar, 0 prüfen, 1 offen**. Nicht abgehakt.
- Gesamt: **1048** vorläufig erfasste Bücher, **983 lesbar, 27 prüfen, 38 offen** (= **65** weiterhin unsicher).
- **19** Fächer vorläufig abgehakt, **10** noch gezielt zu prüfen, **21** bereits nachgeprüft mit Restunsicherheiten; zusätzlich Fach 3-3 mit gesondertem Positions-/Zählabgleich.
- **Nächstes Fach erst auf „Weiter“: 5-2**, ausschließlich B00585 und B00599.
