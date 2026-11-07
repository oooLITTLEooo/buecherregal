# Gezielte Nachprüfung Fach 6-2 – 07.11.2026

## Verbindliche Git-Quelle und Umfang

- Git-Original: `bilder/originale/PXL_20261105_151543813.jpg` = `FOTO0039` (8160 × 4590 Pixel gemäß `daten/fotos.csv`).
- Zuordnungskopie: `bilder/umbenannt/Regal_6-2.jpg`.
- Ausschließlich `daten/bildanalyse/fullres/FOTO0039_teil_04.jpg.base64.txt` als **einzeln geladenen nativen Originalpixel-Ausschnitt** geprüft; nur **B00767**, Position 18, erneut bewertet. 19 zuvor als lesbar eingestufte Bucheinträge nicht erneut inventarisiert.
- Originalfotos, Buch-IDs, Positionen, Fach- und Fotoreferenzen nicht verändert.

## Bildbefund und Identifikation

| Buch-ID | Vorläufige Position | Direkt im Bild lesbar | Bibliografisch bestätigt | Status |
| --- | ---: | --- | --- | --- |
| **B00767** | 18 | Blauer Rücken, Aufdruck `Komarek/Kalmár`, **Schräge Vögel**, darunter **Faszinierende Lebensentwürfe**, Verlagszeichen **K&S** | **Alfred Komarek** (Text) und **János Kalmár** (Fotografien), *Schräge Vögel: Faszinierende Lebensentwürfe*, Kremayr & Scheriau | **lesbar** (vorher `pruefen`) |

### Rollentrennung und bibliografische Belege

- [Morawa: gebundenes Buch *Schräge Vögel, Faszinierende Lebensentwürfe*](https://www.morawa.at/detail/ISBN-9783218009348/Komarek-Alfred/Schr%C3%A4ge-V%C3%B6gel-Faszinierende-Lebensentw%C3%BCrfe) — nennt Alfred Komarek als Autor und János Kalmár für die Fotografien.
- [Kremayr & Scheriau: Autorenporträt Alfred Komarek](https://www.kremayr-scheriau.at/autorenportraet-alfred-komarek/) — bestätigt die Zusammenarbeit und das Werk.
- [ORF Ö1: Alfred Komarek](https://oe1.orf.at/programm/20201004/614580/Der-Schriftsteller-Alfred-Komarek) — beschreibt das Buch mit Fotografien von János Kalmár.

Die zwei vorhandenen Inventar-Namensfelder enthalten nun `Komarek / Kalmár` sowie `Alfred / János`, während der konkrete **Text-/Fotografie-Anteil** explizit in der Anmerkung steht. Diese Rollen sind **nicht** als zwei Autoren desselben Textes zu verstehen. Der vollständige Untertitel ist bibliografisch und durch den fotografierten Rücken belegt. Eine im Buchhandel angeführte ISBN, Auflage oder Erscheinungsjahresangabe wurde **nicht** ungeprüft auf das abgebildete Exemplar übertragen.

## Git-Nachführung

- `daten/buecher.csv`: nur B00767 geändert; Status `pruefen` → `lesbar`, vollständige Namen, vollständiger Titel und Bild-/Katalogbelege.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: B00767 auf `korrigiert_und_lesbar`, Begründung ergänzt.
- `daten/pruefplan_faecher.csv`: Fach 6-2 jetzt **20 von 20 lesbar, 0 prüfen, 0 offen**, Status `vorlaeufig_abgehakt`, zweite Nachprüfung `ja`.
- `daten/fachstatus.csv` und `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: synchronisiert.
- `docs/protokoll.md` und `docs/inventur_fortschritt.md`: Fachprüfung und neue Gesamtzahlen dokumentiert.
- Kein anderes Buch in `daten/buecher.csv` bearbeitet; keine Originalfoto- oder Positionsänderung.

## Bilanz und Halt

- **Fach 6-2:** 20 vorläufige Bucheinträge, **20 lesbar, 0 prüfen, 0 offen** → **vorläufig abgehakt** (keine physische Fachzählung durchgeführt).
- **Gesamt:** 1048 vorläufige Bucheinträge = **998 lesbar, 13 prüfen, 37 offen**, also **50 unsicher**.
- **21** fotografierte Fächer vorläufig abgehakt; **1** Fach noch in dieser gezielten Nachprüfrunde: **6-4** mit **B00804** und **B00811**. Die **28** zuvor erneut geprüften Fächer mit Restunsicherheiten und die zwei bekannten physischen Zähl-/Positionsfragen bleiben bestehen.
- **Nächster Schritt nur auf neue Aufforderung „Weiter“:** Fach 6-4, ausschließlich B00804 und B00811. Danach STOP.
