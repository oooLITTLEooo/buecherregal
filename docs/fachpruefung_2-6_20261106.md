# Gezielte Nachprüfung Fach 2-6 – 06.11.2026

## Bildgrundlage und Umfang

- Git-Original `bilder/originale/PXL_20261105_151125834.jpg`, Foto-ID `FOTO0011`, Bildgröße 8160 × 4590 Pixel laut `daten/fotos.csv`.
- Die zugehörigen Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0011_teil_01.jpg.base64.txt` und `FOTO0011_teil_02.jpg.base64.txt` für die gezielte Sichtprüfung der Position 4 herangezogen.
- Ausschließlich den bisher als `pruefen` markierten Datensatz `B00170` in Fach 2-6 erneut identifiziert. Die anderen 16 als `lesbar` erfassten Datensätze nicht systematisch neu geprüft.

## Ergebnis

**B00170, Position 4:** Schwarzer Buchrücken direkt zwischen Martha Grimes *Auferstanden von den Toten* (Position 3) und Martha Grimes *Das Mädchen ohne Namen* (Position 5).

- Im Originalausschnitt FOTO0011 Teil 2 direkt sichtbar: `GÖTZ SCHRAGE`, `1000X VERLIEBT` und unten `MILENA`.
- Im Katalog des Verlags wird der bibliografische Titel als **Tausendmal verliebt** geführt. Die Schreibweise `1000x verliebt` ist die sichtbare Rückenbeschriftung desselben Werkes.
- Autor vollständig **Götz Schrage**. Buch eindeutig identifiziert. Status von `pruefen` auf **lesbar**.
- Verlagsquelle: https://www.milena-verlag.at/index.php?item=literatur (Abschnitt Götz Schrage, *Tausendmal verliebt*).
- Weitere Ausgabenbestätigung ISBN 978-3-903184-12-1: https://www.kulturkaufhaus.de/de/detail/ISBN-9783903184121/Schrage-G%C3%B6tz/Tausendmal-verliebt. Die abgebildete Auflage/ISBN des einzelnen Exemplars wurde nicht geprüft.

## Git-Änderungen

- `daten/buecher.csv`: ausschließlich B00170 mit identifiziertem Autor, normiertem Verlagstitel, konkretem Fotobefund und `lesbar` korrigiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Einzelfall mit Bildbeleg als geklärt markiert.
- `daten/pruefplan_faecher.csv`: Fach 2-6, 17 lesbar, 0 prüfen, 0 offen, vorläufig abgehakt.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md` synchron nachgeführt.
- Keine Veränderungen an Originalen, Positionskopien, Buch-IDs oder Links-rechts-Positionen.

## Bilanz

- Fach 2-6: **17** vorläufige Bucheinträge, **17 lesbar**, **0 prüfen**, **0 offen**.
- Gesamt: **1048** vorläufige Bucheinträge, **956 lesbar**, **52 prüfen**, **40 offen** (= 92 unsicher).
- **14** Fächer vorläufig abgehakt, **26** Fächer noch gezielt zu prüfen, **11** bereits nachgeprüft mit verbliebenen Unsicherheiten.
- **Nächstes Fach erst nach „Weiter“:** 2-7, nur B00185, B00188 und B00198.
