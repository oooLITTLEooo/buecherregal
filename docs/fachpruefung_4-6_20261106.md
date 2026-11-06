# Gezielte Nachprüfung Fach 4-6 – 06.11.2026

## Quelle und Umfang

- Original aus Git: `bilder/originale/PXL_20261105_151440329.jpg` (FOTO0027), 8160 × 4590 Pixel laut `daten/fotos.csv`.
- Gezielt betrachteter Originalpixel-Ausschnitt `daten/bildanalyse/fullres/FOTO0027_teil_01.jpg.base64.txt` mit B00492; zusätzlich Teil 02 zur Orientierung. Die 21 als lesbar markierten Bücher nicht systematisch neu geprüft.
- **Nur B00492** erneut analysiert; alle anderen Bucheinträge unverändert.

## Ergebnis

| Feld | Befund |
| --- | --- |
| Buch-ID | B00492 |
| Regalposition | Fach 4-6, Position 2 (vorläufig) |
| Direkt davor | B00491: Sabine Thiesler – *Hexenkind* |
| Direkt danach | B00493: Paul Auster – *Nacht des Orakels* |
| Fotobeobachtung | Teil 01 zeigt einen sehr schmalen, durch umliegende Bände verdeckten dunklen Bereich zwischen *Hexenkind* und *Nacht des Orakels*. Kein vollständiger Autor und kein zuverlässiger Titel ablesbar. Es ist nicht ausreichend sicher, ob der Bereich ein eigenständiger Buchband ist. |
| Entscheidung | **offen**, keine unbelegte Buchidentifikation; physische Zählung erforderlich |

## Nötiges Nachfoto

Den Übergang **Sabine Thiesler – Hexenkind / mutmaßlicher B00492 / Paul Auster – Nacht des Orakels** frontal fotografieren und die beiden bekannten Bände leicht auseinanderziehen. Dabei physisch kontrollieren, ob der dunkle Bereich tatsächlich einen **eigenständigen Band** bildet. Falls ja, den Buchrücken und das Titelblatt dieses Bandes einzeln aufnehmen. Die bisherige Position 2 ist bis zur Kontrolle vorläufig.

## Änderungen im Git

- `daten/buecher.csv`: ausschließlich die Belegbemerkung zu B00492 präzisiert. Status `offen`, Autor und Titel `offen`, Position 2, ID und Fotoquelle **unverändert**.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: erfolgte Originalpixel-Nachprüfung und konkreten Fotobedarf dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 4-6 als `neues_detailfoto_bei_bedarf`, `zweite_sichtpruefung=ja`, markiert.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md` nachgeführt.
- **Keine Originalfotos, Fotokopien, Buch-IDs, Zuordnungen, Positionen oder anderen Buchzeilen geändert.**

## Bilanz und Fortsetzung

- Fach 4-6: **22 vorläufige Einträge**, **21 lesbar**, **0 prüfen**, **1 offen**, nicht abgehakt. Physische Anzahl an Position 2 noch ungesichert.
- Gesamt unverändert **1048** vorläufige Einträge: **975 lesbar**, **34 prüfen**, **39 offen** (= 73 unsicher).
- **18** Fächer vorläufig abgehakt, **13** noch gezielt zu prüfen, **19** bereits nachgeprüft mit verbleibenden Identifikationsunsicherheiten. Fach 3-3 separat mit Positions-/Zählabgleich.
- **Nächstes Fach erst nach „Weiter“: 4-7**, ausschließlich **B00516**, **B00518**, **B00526**, **B00528**, **B00535**, **B00540**.
