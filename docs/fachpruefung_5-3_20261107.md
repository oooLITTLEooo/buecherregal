# Gezielte Nachprüfung Fach 5-3 – 07.11.2026

## Bildgrundlage

- Verbindliches Git-Original: `bilder/originale/PXL_20261105_151511259.jpg` (`FOTO0032`, 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Vier bereits im Git versionierte native Originalpixelbereiche einzeln gesichtet: `daten/bildanalyse/fullres/FOTO0032_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt`. Keine fremden Fotos, keine Rekonstruktion des Originalbilds.
- **Nur B00600, B00604, B00614, B00615, B00619** inhaltlich beurteilt. 17 andere bisher lesbare Buch-IDs unverändert belassen. Die unsichere tatsächliche Buchanzahl im Fach wird separat dokumentiert, ohne weitere Bücher neu zu inventarisieren.

## Entscheidungen

| Buch-ID | Position (vorläufig) | Bildbefund und Nachweis | Neuer Status |
| --- | ---: | --- | --- |
| **B00600** | 1 | FOTO0032 Teil 01, ganz links: schmaler orange-rot/schwarzer Band mit *Agatha Christie* und Zahl `822`; der Titel ist nicht lesbar. Keine Zuordnung allein aus der Zahl. | **offen** |
| **B00604** | 5 | FOTO0032 Teil 01: unmittelbar nach Ann Granger *Wer andern eine Grube gräbt* ein dunkler, unlesbarer Rücken mit farbigem Motiv; daneben schmaler gelber Rücken **Bertolt Brecht – Der gute Mensch von Sezuan**, anschließend Fabio Geda *Im Meer schwimmen Krokodile*. Ob B00604 der dunkle Band oder der gelbe Band ist und ob eine zusätzliche Buch-ID fehlt, ist ungeklärt. | **offen** |
| **B00614** | 15 | FOTO0032 Teil 03: schmaler Rücken **Schutting: Liebesgedichte**, `dtv 6346`. Das Werk von **Julian Schutting** ist bibliografisch nachgewiesen. | **lesbar** |
| **B00615** | 16 | FOTO0032 Teil 03: deutlich **Manchmal möchte ich ein Single sein** (nicht „Manchmal möchte ich eine Insel sein“). Die Autorin **Christine Nöstlinger** ist durch ihre offizielle Werkliste bestätigt. | **lesbar** |
| **B00619** | 20 | FOTO0032 Teil 04: `Solschenizyn: Zwischenfall`, `dtv 857` eindeutig sichtbar. Bibliografisch Titelvariante *Zwischenfall auf dem Bahnhof Kretschetowka*; der aufgedruckte Kurztitel *Zwischenfall* bleibt inventarisiert. | **lesbar** |

## Bibliografische Kontrollbelege

- Julian Schutting, *Liebesgedichte*: [Österreichische Nationalbibliothek](https://data.onb.ac.at/nlv/nlv_lex/perslex/Sch/Schutting_Julian.html) und [Google Books, dtv 6346](https://books.google.com/books/about/Liebesgedichte.html?id=uy5KAAAAYAAJ).
- Christine Nöstlinger, *Manchmal möchte ich ein Single sein*: [offizielle Werkübersicht](https://www.christine-noestlinger.at/buch) und [Buchdaten dtv 11573](https://www.eurobuch.de/buch/isbn/3423115734.html).
- Alexander Solschenizyn, *Zwischenfall auf dem Bahnhof Kretschetowka*: [Antiquariats-Katalognachweis dtv 857](https://diebuchsuche.at/buch-isbn-9783423090889.html).

Die bibliografisch bekannten Ausgabedaten sind keine automatische Bestätigung einer bestimmten Auflage des vorliegenden Exemplars.

## Notwendige Nachaufnahmen und physische Prüfung

1. **B00600:** Rücken und Titelblatt des äußersten linken Agatha-Christie-Bands frontal fotografieren; Zahl `822` nicht als Titelnachweis interpretieren.
2. **B00604:** Alle Buchrücken **zwischen Ann Granger *Wer andern eine Grube gräbt* und Fabio Geda *Im Meer schwimmen Krokodile*** einzeln frontal fotografieren und physisch zählen. Den dunklen Rücken und den gelben Bertolt-Brecht-Band (*Der gute Mensch von Sezuan*) separat erkennbar machen. Möglicherweise fehlt ein Inventareintrag, möglicherweise ist die Positionszuordnung verschoben. Noch **keine neue Buch-ID und keine Positionsänderung**.

## Nachgeführte Daten

- `daten/buecher.csv`: B00614, B00615 und B00619 auf `lesbar`; bei B00615 Titelverlesung und fehlenden Autor korrigiert. B00600/B00604 bleiben offen und bekommen genaue Nachfoto- bzw. Zählhinweise.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: alle fünf Prüfentscheidungen dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 5-3 = 22 vorläufige Einträge, 20 lesbar, 0 prüfen, 2 offen, zweite Sichtprüfung erfolgt.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: synchronisiert.
- Originalbilder, Bücher außerhalb der fünf genannten IDs, Positionen und Fotoreferenzen unverändert.

## Bilanz und Folgeschritt

**Fach 5-3:** 22 vorläufig erfasste Einträge, 20 lesbar, 0 prüfen, 2 offen. Nicht abhaken; physische Buchanzahl unklar.

**Gesamt:** 1048 vorläufige Datensätze, **987 lesbar, 23 prüfen, 38 offen** (61 unsicher). **19** Fächer vorläufig abgehakt, **8** noch ohne gezielte Prüfung, **23** bereits mit Zweitprüfung und Restunsicherheit.

**Nächstes Fach erst beim nächsten „Weiter“: 5-4**, nur B00627, B00631 und B00642.
