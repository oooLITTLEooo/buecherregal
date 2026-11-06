# Gezielte Nachprüfung Fach 3-1 – 06.11.2026

## Originalquelle und Prüfgrenze

- Aus dem aktuellen Git-Repository: `bilder/originale/PXL_20261105_151311331.jpg`, FOTO0014, laut `daten/fotos.csv` **8160 × 4590** Pixel.
- Alle vier originalpixelbasierten Teilausschnitte unter `daten/bildanalyse/fullres/FOTO0014_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` visuell geprüft.
- **Nur B00232, B00235, B00240, B00241, B00247, B00249, B00257, B00258** geändert. Andere bislang als `lesbar` geführte Einträge wurden nicht erneut geprüft; 30 Einträge bleiben vorläufig.

## Einzelfallentscheidungen

| ID | Pos. | Befund am Foto und Literaturabgleich | Status nachher |
| --- | ---: | --- | --- |
| B00232 | 3 | Teil 1: gelber rororo-Rücken mit **Eric Malpass**, **Wenn süß das Mondlicht…**; Verlagsbibliografie ergänzt den vollständigen Titel *Wenn süß das Mondlicht auf den Hügeln schläft*. | **lesbar** |
| B00235 | 6 | Teil 1/2: sehr schmaler dunkler Bereich nach Roger Willemsen *Gute Tage* vor Stephen King *In einer kleinen Stadt*. Titel und selbstständige Buchgrenze nicht gesichert. | **offen** |
| B00240 | 11 | Teil 2: schmaler grauer Rücken nach Alfred Komarek *Polterabend* vor André Kaminski *Flimmergeschichten*; Schrift nicht zweifelsfrei zu entziffern. | **offen** |
| B00241 | 12 | Teil 2: gelbes Suhrkamp-Buch **st 2164**, deutlich *Kaminski Flimmergeschichten*. Autor **André Kaminski**, ursprünglicher Titel *Kriminalgeschichten* war falsch. | **lesbar** |
| B00247 | 18 | Teil 3: gelbes Suhrkamp-Buch **st 1807** mit *Kaminski Kiebitz*. Autor **André Kaminski** vom Verlag bestätigt. | **lesbar** |
| B00249 | 20 | Teil 3: grünes Suhrkamp-Buch **st 930** mit *Kaminski Die Gärten des Mulay Abdallah*. Ursprüngliche Lesung *Mullah* falsch. Autor **André Kaminski**. | **lesbar** |
| B00257 | 28 | Teil 4: weißes Suhrkamp-Buch **st 1637**, *Kaminski Schalom allerseits*. Autor **André Kaminski**. | **lesbar** |
| B00258 | 29 | Teil 4: braun gemusterter, unbeschriftet erscheinender Rücken zwischen *Schalom allerseits* und John Irving *Garp und wie er die Welt sah*. Titel nicht feststellbar. | **offen** |

## Kontrollquellen für bibliografische Ergänzungen

- Rowohlt, Eric Malpass: https://www.rowohlt.de/buch/eric-malpass-wenn-suess-das-mondlicht-auf-den-huegeln-schlaeft-9783688108596
- Suhrkamp, André Kaminski *Flimmergeschichten* (st 2164): https://www.suhrkamp.de/buch/andre-kaminski-flimmergeschichten-t-9783518386644
- Suhrkamp, André Kaminski *Kiebitz* (st 1807): https://www.suhrkamp.de/buch/andre-kaminski-kiebitz-t-9783518383070
- Suhrkamp, André Kaminski *Die Gärten des Mulay Abdallah* (st 930): https://www.suhrkamp.de/buch/andre-kaminski-die-gaerten-des-mulay-abdallah-t-9783518374306
- Suhrkamp, André Kaminski *Schalom allerseits* (st 1637): https://www.suhrkamp.de/buch/andre-kaminski-schalom-allerseits-t-9783518381373

Reihennummern am Rücken sind ablesbar; keine ungesehenen Auflagen der konkreten Exemplare behauptet. Die fünf IDs entsprechen fünf eindeutigen physischen Büchern.

## Nachfotografieren

- B00235: sehr schmalen dunklen Bereich zwischen Roger Willemsen *Gute Tage* und Stephen King *In einer kleinen Stadt* einzeln aufnehmen und prüfen, ob ein selbstständiger Band vorliegt.
- B00240: grauen Rücken zwischen Alfred Komarek *Polterabend* und André Kaminski *Flimmergeschichten* frontal fotografieren; bei verblasster Schrift Titelblatt.
- B00258: den gemusterten braunen Rücken zwischen André Kaminski *Schalom allerseits* und John Irving *Garp und wie er die Welt sah* herausziehen und Titelblatt aufnehmen.

## Sonstige bibliografische Beobachtung (nicht geändert)

Auch die derzeit als `lesbar` markierten B00248 (*Der Sieg über die Schwerkraft*) und B00250 (*Nächstes Jahr in Jerusalem*) sind dem Schriftsteller **André Kaminski** zugeordnet, im CSV jedoch ohne Vornamen. Wegen der Vorgabe, nur unsichere IDs zu bearbeiten, wurden diese Daten nicht geändert. Mögliche spätere separate bibliografische Bereinigung.

## Git und Zählstand

- `daten/buecher.csv`: fünf sichere Bücher ergänzt/korrigiert und auf `lesbar` gesetzt; bei drei weiterhin offenen Büchern allein die Nachprüfbemerkungen konkretisiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: acht Einzelentscheidungen samt Beleg-/Fotobedarf synchronisiert.
- `daten/pruefplan_faecher.csv`, `daten/fachstatus.csv`, Gesamtprüfplan und Protokolle aktualisiert.
- **Originalfoto und Kopie nicht verändert**, keine Buch-IDs, Fachzuordnungen, Buchpositionen oder Bücherzahl geändert.
- Fach 3-1: **30** vorläufige Exemplare, **27 lesbar**, **0 prüfen**, **3 offen**.
- Gesamt: **1048** vorläufige Exemplare, **964 lesbar**, **44 prüfen**, **40 offen** = **84 unsicher**.
- **15** Fächer vorläufig abgehakt, **23** noch gezielt zu prüfen, **13** bereits nachgeprüft und nicht ganz geklärt.
- **Nächstes Fach erst nach „Weiter“: 3-2**, nur B00277.
