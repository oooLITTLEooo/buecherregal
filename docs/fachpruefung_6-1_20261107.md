# Gezielte Nachprüfung Fach 6-1 – 07.11.2026

## Quelle und Umfang

- Git-Original: `bilder/originale/PXL_20261105_151539726.jpg`, Foto-ID `FOTO0038`, 8160 × 4590 Pixel gemäß `daten/fotos.csv`.
- Verifizierte positionsbezogene Kopie: `bilder/umbenannt/Regal_6-1.jpg`.
- Genau die im Git versionierten nativen Bildteile `daten/bildanalyse/fullres/FOTO0038_teil_01.jpg.base64.txt` und `FOTO0038_teil_04.jpg.base64.txt` einzeln untersucht. Diese zeigen die für die beiden fraglichen Positionen relevanten linken bzw. rechten Fachbereiche.
- **Nur B00727 und B00748** nachgeprüft. Die übrigen 21 bereits als lesbar erfassten Bucheinträge nicht erneut bewertet; keine Fotos, Buch-IDs, Reihenfolge oder Positionen verändert.

## Ergebnisse

| Buch-ID | Position (vorläufig) | Sichtbarer Originalbildbefund | Entscheidung |
| --- | ---: | --- | --- |
| **B00727** | 1 | `FOTO0038` Teil 01: am äußersten linken Ende ein sehr schmaler dunkler Rücken, weitgehend vom großen hellen Band **Leo Lukas – Das Leo Lukas Lesebuch** (B00728) verdeckt. Weder Autor noch Werktitel sind sicher ablesbar. Die physische Abgrenzung gegenüber dem Nachbarbuch bleibt zusätzlich kontrollbedürftig. | **offen**, kein Titel geraten |
| **B00748** | 22 | `FOTO0038` Teil 04: schmaler dunkler Rücken im Spalt zwischen **Axel Munthe – Das Buch von San Michele** (B00747, blau) und **Håkan Nesser – Sein letzter Fall** (B00749, grauer btb-Band). Eine rote btb-artige Markierung ist im Spalt sichtbar, gehört aber nicht nachweislich zu einer bestimmten Ausgabe. Kein eindeutiger Autor oder Titel lesbar. | **offen**, kein Titel geraten |

Es liegt **kein verlässlicher bibliografischer Ansatz** zur Titelidentifizierung der beiden verdeckten Bücher vor. Die Nachbarbücher dienen nur zur Ortsbestimmung, nicht als Beweis für Titel, Verfasser oder Verlagszugehörigkeit der gesuchten Bände.

## Genau benötigte Nachfotos und physische Kontrolle

1. **B00727, Fachposition 1:** Das schmale Buch **ganz links neben Leo Lukas – Das Leo Lukas Lesebuch** vorsichtig freistellen oder herausziehen; **vollständigen Rücken frontal** sowie **Titelblatt** fotografieren. Mit einem Überblick die linksseitige Fachgrenze und das Leo-Lukas-Buch dokumentieren. Prüfen, ob tatsächlich ein gesonderter Band vorhanden ist.
2. **B00748, Fachposition 22:** Den schmalen Band **zwischen Axel Munthe – Das Buch von San Michele und Håkan Nesser – Sein letzter Fall** herausziehen; **Buchrücken frontal**, **Titelblatt** und bei Bedarf **Impressum** fotografieren. Vor Ort die tatsächliche Buchgrenze beziehungsweise die vorhandene Zahl der Bände bestätigen.

Eine vergrößerte Darstellung derselben bereits verdeckten Pixel kann keine sicher unsichtbaren Titel sichtbar machen. Die 23 Bucheinträge und Positionen bleiben bis zur physischen Bestätigung vorläufig.

## Git-Nachführung

- `daten/buecher.csv`: nur die `bemerkung`-Felder von **B00727** und **B00748** präzisiert; beide bleiben `offen`; keine Autor-/Titelvermutungen.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: neue Prüfbegründung und Fotobedarf bei diesen beiden IDs dokumentiert, weiterhin `bleibt_unsicher_nach_hochaufloesungspruefung`.
- `daten/pruefplan_faecher.csv`: Fach 6-1 behält **23 vorläufige Einträge, 21 lesbar, 0 prüfen, 2 offen**, bekommt `neues_detailfoto_bei_bedarf` und zweite Prüfung `ja`; offene IDs B00727 und B00748.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: Status und Fortsetzung synchronisiert.
- Sämtliche vorhandenen Originalbilder, Buchnummern, Positionsangaben und Fotoreferenzen unangetastet.

## Bilanz und Stopp

- **Fach 6-1:** 23 vorläufig erfasste Bücher, **21 lesbar, 0 prüfen, 2 offen**. Wegen verdeckter Einzelbände **nicht abgehakt**.
- **Gesamt:** **1.048** vorläufige Bucheinträge, **997 lesbar, 14 prüfen, 37 offen** = **51 unsicher**. Die Identifikationszahlen ändern sich gegenüber der vorherigen Prüfung nicht.
- **20** Fächer vorläufig abgehakt; **2** Fächer in der laufenden gezielten Erst-Nachprüfung noch ausständig; **28** Fächer in dieser Runde erneut geprüft und wegen Restunsicherheiten nicht abgehakt. Zusätzlich sind die physischen Zähl-/Positionsabgleiche 3-3 und 5-3 offen.
- **Nächstes Fach erst nach neuem „Weiter“: 6-2**, ausschließlich **B00767**.
