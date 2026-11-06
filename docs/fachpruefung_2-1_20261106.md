# Gezielte Nachprüfung Fach 2-1 – 06.11.2026

## Vorgabe und Beleg

- **Nur Fach 2-1**, darin ausschließlich die vorher offenen/prüfpflichtigen Einträge **B00061, B00071, B00078** nachgeprüft.
- Original im Git: `bilder/originale/PXL_20261105_151059664.jpg` (`FOTO0006` laut `daten/fotos.csv`, 8160 × 4590 Pixel). Alle Originaldateien und die positionsbenannte Kopie bleiben unverändert.
- Die drei fraglichen Positionen wurden anhand der nativen Ausschnitte `daten/bildanalyse/fullres/FOTO0006_teil_01.jpg.base64.txt`, `_teil_02`, `_teil_03` und `_teil_04` kontrolliert. Die angrenzenden bereits lesbaren Bücher dienten nur zur Lokalisierung.
- **Keiner der drei Rücken lässt sich mit vorhandenen Bildern zuverlässig vollständig identifizieren.** Titel und Autor nicht raten; die Unsicherheit über die physische Buchgrenze besonders bei B00071 und B00078 ausdrücklich beibehalten.

## Die drei Fälle

| Position | Buch-ID | Status | Bildbefund | Benötigtes Zusatzfoto |
|---:|---|---|---|---|
| 2 | **B00061** | `offen` | FOTO0006 Teil 1. Nach *Gut, aber tot* von Eva Rossmann und vor *Die Sonntagsfrau* von Fruttero/Lucentini ist ein zurückstehender dunkler Buchkörper erkennbar. Autor und Titel werden weitgehend verdeckt. | Dunklen Band herausnehmen, Rücken und Vorderseite frontal fotografieren. |
| 12 | **B00071** | `pruefen` | FOTO0006 Teile 2–3. Im Bereich hinter/zwischen *Sofia und Anders* von Marianne Fredriksson und *Der dritte Zwilling* von Ken Follett bleibt ein schmaler Bereich beziehungsweise die genaue Bandgrenze unsicher. Kein verlässlicher Titel. Bisherige Marianne-Fredriksson-Zuordnung ist **nicht als sicher bestätigt**. | Verdächtigen Band isolieren, Rücken und Titelblatt/Vorderseite fotografieren, eigenständige Bandgrenze kontrollieren. |
| 19 | **B00078** | `pruefen` | FOTO0006 Teil 4. Dunkler Buchbereich im Umfeld von Nicci Frenchs *Das rote Zimmer* und vor Marianne Fredrikssons *Die Jahre mit Jan*. Kein vollständiger Titel sicher erkennbar; Trennung der Bände anhand Foto nicht endgültig gesichert. | Betroffenes dunkles Buch separat herausnehmen und Rücken/Vorderseite fotografieren. |

## Ergebnis

- **20** vorläufige Buchdatensätze in Fach 2-1; **17 lesbar, 2 prüfen, 1 offen**. Keine von den drei Unsicherheiten ist zuverlässig aufgelöst.
- Die 17 bereits als `lesbar` markierten Bücher wurden entsprechend der Nutzerentscheidung **nicht** erneut vollständig überprüft.
- Es wurde **kein** Bucheintrag gelöscht, eingefügt oder in Titel/Autor/Buch-ID/Position verändert. Keine alphabetische oder physische Umsortierung.
- `daten/buecher.csv`: Nur die Nachweis-/Fotoanforderungsbemerkungen von B00061, B00071, B00078 präzisiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Die drei Prüfzeilen mit genauerer Quellenbeobachtung aktualisiert, aber `bleibt_unsicher_nach_hochaufloesungspruefung` **nicht** auf `lesbar` geändert.
- `daten/fachstatus.csv`: Fachprüfstatus mit offenem Fotobedarf dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 2-1 von `gezielte_pruefung` auf `neues_detailfoto_bei_bedarf` gestellt; **kein** vorläufiges Abhaken.
- `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: aktualisierter Listenstand.
- Keine Manipulation der Bildquellen, keine spekulative Identifikation.

## Gesamtfortschritt

- Regal unverändert: **1048** vorläufig inventarisierte Bucheinträge, **949 lesbar**, **59 prüfen**, **40 offen** = **99** ungeklärt.
- Von den **51** fotografierten Fächern sind **12** vorläufig abgehakt. **39** weisen noch Unsicherheiten auf, davon jetzt **31** mit gezielter Überprüfung ausstehend, **8** nach Hochauflösungsprüfung weiterhin mit Zusatzfoto-Bedarf.
- Fotos für 7-8, 8-1 und 8-2 fehlen weiterhin, Belegung 8-3 bis 8-8 muss später geklärt werden.

**Nächster Durchgang nur auf neues „Weiter“:** Fach **2-2**, **ausschließlich B00094**.
