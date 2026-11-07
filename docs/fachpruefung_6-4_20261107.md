# Gezielte Nachprüfung Fach 6-4 – 07.11.2026

## Fotoquelle und Bearbeitungsgrenze

- Git-Original: `bilder/originale/PXL_20261105_151551048.jpg` = `FOTO0041`, laut `daten/fotos.csv` 8160 × 4590 Pixel.
- Bereits im Git gespeicherte native Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0041_teil_02.jpg.base64.txt`, `_teil_03.jpg.base64.txt` und `_teil_04.jpg.base64.txt` **einzeln** geprüft.
- **Nur B00804** (Position 15, Teil 03) und **B00811** (Position 22, Teil 04) aktualisiert. 22 andere als lesbar erfasste Bücher nicht erneut geprüft.
- Unverändert: Originalbilder, Foto-Kopien, IDs, Regalpositionen und Fotoreferenzen.

## Ergebnisse

| Buch-ID | Position | Befund und unabhängiger Abgleich | Ergebnis |
| --- | ---: | --- | --- |
| **B00804** | 15 | FOTO0041 Teil 03, schmaler heller Buchrücken im Heinrich-Böll-Abschnitt: **Böll** und **Warum haben wir ...** erkennbar. Berliner Bibliothekskatalog und Deutsche Biographie belegen **Heinrich Böll / Lew Kopelew – Warum haben wir aufeinander geschossen?**. Bisherige Angabe **Koppel...** war eine Verlesung des Namens Kopelew. | **lesbar** (vorher `pruefen`) |
| **B00811** | 22 | FOTO0041 Teil 04, sehr schmaler dunkelblauer Suhrkamp-Rücken nach Heinrich Böll *Der Zug war pünktlich* und vor Thomas Harris *Die Hannibal-Lecter-Romane*: Verlagsreihennummer **st 560**. Im Katalog des Deutschen Literaturarchivs Marbach steht **st 560** für **Peter Handke – Die linkshändige Frau**; ein Vergleichsfoto zeigt dieselbe blaue Paperback-Gestaltung. Der Titel steht in der aufgenommenen Rückenperspektive nicht vollständig lesbar da, die Kombination aus Reihennummer und Einband ist aber hinreichend spezifisch. | **lesbar** (vorher `offen`) |

## Externe bibliografische Belege

- **B00804**: [Verbund der Öffentlichen Bibliotheken Berlins – Heinrich Böll / Lew Kopelew, Warum haben wir aufeinander geschossen?](https://www.voebb.de/aDISWeb/app/prod00?sp=SAK00013617)
- **B00804**: [Deutsche Biographie – Böll, Gespräche und Interviews](https://www.deutsche-biographie.de/pnd118512676.html)
- **B00811**: [Deutsches Literaturarchiv Marbach – Katalogdatei, Eintrag Peter Handke, Die linkshändige Frau, suhrkamp taschenbuch 560](https://digital.dla-marbach.de/files/dbst02/public/2025/20251125/20251125-0001.pdf?media_access=public)
- **B00811**: [Booklooker – Peter Handke, Die linkshändige Frau, st 560](https://www.booklooker.de/B%C3%BCcher/Peter-Handke%2BDie-linksh%C3%A4ndige-Frau-Erz%C3%A4hlung/isbn/351837060X)
- **B00811**: [Vergleichsfoto der blauen Taschenbuch-Ausgabe st 560](https://knihobot.cz/g/713046)

**Wichtig:** Die bibliografische Ausgabebezeichnung stellt nicht sicher, welche konkrete Auflage oder Druckvariante das fotografierte Exemplar ist. Keine ISBN, Erscheinungsjahr- oder Auflagenangaben ungeprüft auf den Bestand übertragen.

## Git-Nachführung

- `daten/buecher.csv`: ausschließlich B00804 und B00811 inhaltlich korrigiert, jeweils `lesbar`; B00804 Mitverfasser **Lew Kopelew** und vollständiger Titel, B00811 Autor/Titel nach st 560 ergänzt; Quellen und Grenzen dokumentiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: zwei Einzelprüfungen mit Quellen als `korrigiert_und_lesbar` dokumentiert.
- `daten/pruefplan_faecher.csv`: Fach 6-4 jetzt **24/24 lesbar**, **0 prüfen**, **0 offen**, `vorlaeufig_abgehakt`, zweite Bildprüfung `ja`.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md`: synchronisiert.
- Originalfotos, Kopien, alle anderen Buch-IDs, die Positionen der beiden geprüften Bücher und sämtliche Fotoreferenzen unverändert.

## Abschlussstand der gezielten Nachprüfrunde

- **Fach 6-4:** 24 vorläufige Einträge, **24 lesbar, 0 prüfen, 0 offen**. Vorläufig abgehakt; keine physische Nachzählung durchgeführt.
- **Gesamt:** **1.048** vorläufige Einträge, davon **1.000 lesbar, 12 prüfen, 36 offen**, also **48 unsicher**.
- **22** fotografierte Fächer vorläufig abgehakt, **28** fotografierte Fächer mit verbliebenen Unsicherheiten nach zweiter Prüfung. **0** Fächer aus dieser fachweisen Nachprüfrunde noch unbearbeitet.
- Zusätzlich bleibt ein vorläufig vollständig lesbares Fach **3-3** mit physischem Positions-/Zählabgleich; auch in Fach **5-3** ist die Bandanzahl noch zu bestätigen.
- Die 13 bereits dokumentierten Regalpositionen ohne eigene Detailaufnahme sind ein **separater Foto-/Belegungsbedarf** und keine der jetzt abgeschlossenen Einzelbuchprüfungen.
- **STOP:** Nächster sinnvoller Projektabschnitt nur auf neue Benutzeraufforderung: die 48 unsicheren Buchdatensätze mit benötigten Nachfotos und die physischen Zählfragen gesammelt aus den vorhandenen Berichten aufbereiten, ohne unnötige Wiederholung derselben Originalbildausschnitte.
