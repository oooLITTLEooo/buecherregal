# Gezielte Nachprüfung von Fach 1-8 – 06.11.2026

## Umfang

- **Nur Fach 1-8**, und ausschließlich den vorher offenen Eintrag **B00055** (vorläufige Position **11**) behandelt. Die 14 bereits als `lesbar` erfassten Bände blieben ungeprüft und unverändert.
- Originalfoto aus dem Git-Repository: `bilder/originale/PXL_20261105_151050073.jpg` (`FOTO0005`, **8160 × 4590 Pixel** laut `daten/fotos.csv`).
- Visuell gesichtete Originalpixel-Ausschnitte: `daten/bildanalyse/fullres/FOTO0005_teil_03.jpg.base64.txt` (B00055) sowie Teil 02 (benachbarte Fächer/Positionsübergang) und Teil 04 (rechter Bereich).

## Identifikation des zuvor offenen Buches

| Feld | Vorher | Neu |
| --- | --- | --- |
| Buch-ID | B00055 | B00055 |
| Fachposition | 1-8 / 11 | 1-8 / 11 |
| Autor Nachname | offen | **Rebhandl** |
| Autor Vorname | offen | **Manfred** |
| Titel | offen | **Der König der Schweine** |
| Identifikationsstatus | offen | **lesbar** |
| Fotoquelle | FOTO0005 | unverändert |

**Primärer Foto-Nachweis:** In `FOTO0005` Teil 03 ist zwischen **Noah Gordon, *Der Rabbi*** (Position 10), und **Charlotte Link, *Der Verehrer*** (Position 12) der eigene orangefarbene Buchrücken zu erkennen. Die Namenszeile **Manfred Rebhandl** und der markante Titelbestandteil **Schweine** sind bildlich erkennbar. Aus der Gesamtbeschriftung zusammen mit dem Verlagskatalog ergibt sich die Titelidentifikation.

**Unabhängige bibliografische Bestätigung des Werkes:** Der Verlag Haymon führt `Manfred Rebhandl – Der König der Schweine` (https://www.haymonverlag.at/produkt/der-koenig-der-schweine/). Die genaue Auflage bzw. ISBN des *konkreten abgebildeten Exemplars* wurde **nicht** verifiziert und wird daher nicht in das Inventar übernommen.

## Git-Protokoll

- `daten/buecher.csv`: nur **B00055** in Autor, Titel, Identifikationsstatus und begründender Bildreferenz geändert. Buch-ID, Fach, Position und Git-Originalpfad unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: B00055 von `bleibt_unsicher_nach_hochaufloesungspruefung` auf `korrigiert_und_lesbar` gestellt, Nachweis ergänzt.
- `daten/fachstatus.csv`: Fach 1-8 als **vorläufig abgehakt** gekennzeichnet; das ist keine unabhängige Nachprüfung der übrigen 14 Bücher.
- `daten/pruefplan_faecher.csv`: Status **vorlaeufig_abgehakt**, 15 lesbar, 0 prüfen, 0 offen; B00055 aus Warteschlange genommen.
- `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`: Kennzahlen und nächste Aufgaben synchronisiert.
- **Originalfoto, Ausschnitte, benannte Foto-Kopie und alle anderen Buchdatensätze unverändert.**

## Ergebnis

- Fach **1-8**: **15** Einträge, **15 `lesbar`**, **0 `pruefen`**, **0 `offen`**, daher vorläufig abgehakt.
- Gesamtinventar: **1048** vorläufige Bucheinträge, davon **949 `lesbar`**, **59 `pruefen`**, **40 `offen`** = **99** ungeklärte.
- **12** von 51 fotografierten Fächern vorläufig abgehakt; **39** Fächer mit weiterhin unklaren Einträgen. Davon **32** ausstehende gezielte Einzelfachprüfungen und **7** bereits fachweise geprüft mit Bedarf nach neuer Evidenz.
- Nächster Schritt **nur auf neues „Weiter“**: Fach **2-1**, dabei nur **B00061, B00071, B00078**.
