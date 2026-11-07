# Gezielte Nachprüfung Fach 5-5 – 07.11.2026

## Quellen und Prüfungsumfang

- Git-Original `bilder/originale/PXL_20261105_151520019.jpg` (Foto-ID `FOTO0034`, laut `daten/fotos.csv` 8160 × 4590 Pixel). Unveränderte Positionskopie: `bilder/umbenannt/Regal_5-5.jpg`.
- Bereits vorhandene native Ausschnitte `daten/bildanalyse/fullres/FOTO0034_teil_01.jpg.base64.txt` und `FOTO0034_teil_02.jpg.base64.txt` einzeln untersucht; **die für beide fraglichen Bücher relevanten Pixel stehen in Teil 01**.
- Ausschließlich die Datensätze **B00645** (Position 2) und **B00647** (Position 4) kontrolliert. Die übrigen 19 als lesbar erfassten Bücher dieses Fachs nicht erneut systematisch inventarisiert.
- Keine Originalfotos modifiziert, keine Positions- oder Buch-ID-Verschiebung.

## Befunde

| Buch-ID | Position | Sichtbarer Bildbefund | Status |
| --- | ---: | --- | --- |
| **B00645** | 2 | Dunkler, teils spiegelnder Rücken im Übergang zwischen Saul Bellow *Der Regenkönig* und Thomas Bernhard *Ein Kind*. Aus den vorhandenen Pixeln weder Autor noch Werktitel sicher erkennbar. | **offen** |
| **B00647** | 4 | Sehr schmaler bzw. teilweise überdeckter Rücken im Übergang zwischen Thomas Bernhard *Ein Kind* und John Irving *Die imaginäre Freundin*. Eine Titelidentifikation aus dem sichtbaren Rücken ist nicht möglich. | **offen** |

### Abgrenzung zur detebe-Nummer 23308

Die sichtbar benachbarte Nummer **23308** ist laut [Diogenes-Verlag: Die imaginäre Freundin](https://www.diogenes.ch/leser/titel/john-irving/die-imaginaere-freundin-9783257233087.html) dem Buch *John Irving – Die imaginäre Freundin* zugeordnet, das bereits als **B00648** inventarisiert ist. Diese Kennzeichnung **identifiziert B00647 gerade nicht**. Kein weiterer Titel wird aus der Nummer abgeleitet.

## Benötigte Fotos

1. **B00645:** Dunklen Rücken **zwischen Saul Bellow *Der Regenkönig* und Thomas Bernhard *Ein Kind*** frontal und mit besserer Beleuchtung fotografieren, bei Bedarf Band herausziehen und Titelblatt aufnehmen.
2. **B00647:** Schmalen Rücken **zwischen Thomas Bernhard *Ein Kind* und John Irving *Die imaginäre Freundin*** freistellen; eine Einzelaufnahme des Rückens und ein Foto des Titelblatts machen. Die beiden angrenzenden Bücher zur Positionssicherung mit aufnehmen.

Ohne zusätzliche Fotos wäre eine bibliografische Identifizierung geraten. Daher **kein Statuswechsel auf `lesbar`** und Fach **nicht abgehakt**.

## Git-Dokumentation und Bilanz

- `daten/buecher.csv`: nur die Bemerkungen von B00645 und B00647 mit präzisen Bildbefunden und Fotohinweisen ergänzt; IDs, Fach, Position, Foto, Status und offene Titel unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: diese beiden erneuten Prüfungen dokumentiert; beide bleiben `bleibt_unsicher_nach_hochaufloesungspruefung`.
- `daten/pruefplan_faecher.csv`: Fach 5-5 nun `neues_detailfoto_bei_bedarf`, zweite Sichtprüfung `ja`. 21 vorläufige Einträge, 19 lesbar, 0 prüfen, 2 offen.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md` nachgeführt.
- Bestand insgesamt unverändert **1048 vorläufige Bucheinträge = 990 lesbar, 20 prüfen, 38 offen**, also **58 unsicher**.
- **20** Fächer vorläufig abgehakt, **6** noch nicht in dieser Runde gezielt geprüft, **24** nachgeprüft mit verbleibenden Unsicherheiten, Fach 3-3 zusätzlich mit Positions-/Zählabgleich.
- **Nächstes Fach erst auf „Weiter“: 5-6**, nur B00668, B00671, B00673, B00680, B00686 und B00688.
