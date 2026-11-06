# Fachprüfung 7-1 – 06.11.2026

## Grundlage

- **Ausschließlich Fach 7-1** überprüft, keine weiteren Regalfächer angefasst.
- Foto-ID: `FOTO0046`; originales Git-Foto `bilder/originale/PXL_20261105_151624486.jpg` (8160 × 4590 Pixel).
- **Vier** aus Originalpixeln abgeleitete hochauflösende Bildausschnitte `daten/bildanalyse/fullres/FOTO0046_teil_01.jpg.base64.txt` bis `FOTO0046_teil_04.jpg.base64.txt` vollständig einzeln betrachtet. Textkodierte Ausschnitte bleiben unverändert.
- 19 bisher erfasste physische Bücher (Buch-IDs `B00914` bis `B00932`), Positionen 1 bis 19 von links nach rechts.

## Einzelabgleich

- 18 bereits als `lesbar` markierte Autor-/Titel-Kombinationen stimmen mit den lesbaren Buchrücken auf den vier Bildteilen überein.
- Beispiele entlang der sichtbaren Reihenfolge: B00914 John Grisham *Das Urteil* (Teil 1), B00915 Rosamunde Pilcher *Wintersonne* (Teil 1), B00917 John Grisham *Die Bruderschaft* (Teil 2), B00919 Herbert Dutzler *Letzter Applaus* (Teil 2), B00923 Erich Hackl *Entwurf einer Liebe auf den ersten Blick* (Teil 3), B00926 Ruth Cerha *Bora – Eine Geschichte vom Wind* (Teil 3), B00931 Jonas Jonasson *Die Analphabetin, die rechnen konnte* (Teil 4), B00932 Elfriede Hammerl *Wunderbare Valerie* (Teil 4).
- Keine weiteren sachlich belegbaren Titelkorrekturen bei diesen 18 Einträgen. Kein sichtbarer Band doppelt erfasst.

## Einzige verbleibende Unklarheit

| Buch-ID | Position | Status | Sichtbarer Bildbeleg | Bedarf |
| --- | ---: | --- | --- | --- |
| **B00916** | **3** | `offen` | `FOTO0046` Teil **1**: schmaler grauer Rücken mit goldfarbener handschriftlicher Beschriftung **zwischen** Rosamunde Pilcher *Wintersonne* (Position 2) und John Grisham *Die Bruderschaft* (Position 4). Weder Autor noch vollständiger Titel sicher entzifferbar | Frontales, scharfes Zusatzfoto vom einzelnen Buchrücken, idealerweise zusätzlich von der Vorderseite oder dem Titelblatt |

Keine spekulativen Titel ergänzt. Die Nachbarbücher werden nicht als Identifikation des unbekannten Bandes herangezogen.

## Änderungen im Git

- `daten/buecher.csv`: nur **B00916** um präzise Fotobeobachtung und nachzufotografierende Stelle ergänzt. Kein Wechsel der `buch_id`, Position, Fotoquelle oder des Status.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: nur **B00916** mit konkreter Nachfotografieranweisung ergänzt.
- `daten/fachstatus.csv`: früheren veralteten Statusvermerk `Einzelbucherfassung ausstehend` auf den tatsächlich geprüften Fortschritt aktualisiert.
- Originalfoto und byteidentische Kopie unverändert. Keine alphabetische Umsortierung.

## Ergebnis

- Fach 7-1: **19** physische Bucheinträge, davon **18 `lesbar`**, **1 `offen`** und **0 `pruefen`**.
- Global weiterhin **1048** vorläufige Bucheinträge: **944 `lesbar`**, **63 `pruefen`**, **41 `offen`**.
- Sichtbare Reihenfolge fachweise abgeglichen, aber bibliografische Details der verdeckten Buchseiten sind nicht aus dem Foto beweisbar.
- Nächster Bearbeitungsschritt **erst nach erneutem „Weiter“**: Fach **7-2**, wieder nur ein Fach.
