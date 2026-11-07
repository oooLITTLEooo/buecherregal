# Gezielte Nachprüfung Fach 5-4 – 07.11.2026

## Git-Quelle und Umfang

- Original: `bilder/originale/PXL_20261105_151516438.jpg` (`FOTO0033`, 8160 × 4590 Pixel laut `daten/fotos.csv`).
- Im Git vorhandene native Bildbereiche `daten/bildanalyse/fullres/FOTO0033_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` **einzeln** betrachtet. Die für Entscheidungen relevanten Bereiche sind Teil **02, 03, 04**.
- Ausschließlich **B00627**, **B00631** und **B00642** inhaltlich geprüft und aktualisiert. Alle anderen 19 Buch-IDs des Fachs sowie alle Originalfotos, Fotoreferenzen und Positionen unverändert.

## Befunde

| Buch-ID | Vorläufige Position | Direkt im Git-Foto beobachtet | Bibliografische Ergänzung | Status |
| --- | ---: | --- | --- | --- |
| **B00627** | 6 | FOTO0033 Teil 02, roter Buchrücken mit Autorenname **Dieter Noll** und Titel **Die Abenteuer des Werner Holt**, Nummer `1043`. | Werk und Autor auch bei Aufbau Verlag nachgewiesen. **Keine Aussage zur Auflage des konkreten Exemplars.** | **lesbar** |
| **B00631** | 10 | FOTO0033 Teil 03, am linken Bildrand schwarzer Buchrücken mit **Nie wieder Hummer**; Autorenname aus diesem Rückenbereich nicht sicher lesbar. | Bibliografischer Katalog identifiziert Autor **Hanns Marzini** und Werktitel *Nie wieder Hummer*. Genaue Ausgabe/ISBN des abgebildeten Buchs nicht belegt. | **lesbar** |
| **B00642** | 21 | FOTO0033 Teil 04, schmaler Rücken mit Aufdruck **Sammlung Luchterhand – Breznik – Figuren**, neben Simon Beckett *Die Chemie des Todes* und Rosamunde Pilcher *Heimkehr*. | Buchkatalog nennt Autorin **Melitta Breznik**, *Figuren*. `2008` ist die Sammlungsnummer, **kein bestätigtes Erscheinungsjahr des vorhandenen Exemplars**. | **lesbar** |

## Bibliografische Kontrollquellen

- Dieter Noll, *Die Abenteuer des Werner Holt*: [Aufbau Verlag](https://www.aufbau-verlage.de/aufbau-taschenbuch/die-abenteuer-des-werner-holt/978-3-7466-2871-4) und [Google Books](https://books.google.com/books/about/Die_Abenteuer_des_Werner_Holt.html?id=tY3h3jvjsLsC).
- Hanns Marzini, *Nie wieder Hummer*: [ZVAB-Katalognachweis](https://www.zvab.com/9783950172607/Marzini-nie-Hummer-3950172602/plp) und [LovelyBooks](https://www.lovelybooks.de/autor/Hanns-Marzini/Nie-wieder-Hummer-Eine-widerw%C3%A4rtige-Geschichte-%C3%BCber-einen-Segelt%C3%B6rn-durch-die-kroatische-Adria-219053317-w/).
- Melitta Breznik, *Figuren*: [Buchhaus / Luchterhand](https://www.buchhaus.ch/de/buecher/taschenbuch/romane/detail/ISBN-9783630620084/Breznik-Melitta/Figuren) und [ZVAB-Katalognachweis Sammlung Luchterhand 2008](https://www.zvab.com/signiert/Figuren-Erz%C3%A4hlungen-Sammlung-Luchterhand-2008-Breznik/32253380928/bd).

Die genannten Katalogausgaben belegen Autor und Werk; eine exakte ISBN, Auflage oder ein Erscheinungsjahr wurde **nicht automatisch auf das fotografierte Exemplar übertragen**.

## Git-Änderungen

- `daten/buecher.csv`: ausschließlich B00627, B00631 und B00642 auf `lesbar` gesetzt, fehlende Autoren ergänzt und Titel präzisiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: diese drei Prüffälle auf `korrigiert_und_lesbar` gesetzt und Bild-/Bibliografienachweise eingetragen.
- `daten/pruefplan_faecher.csv`: Fach 5-4 nun **22 lesbar, 0 prüfen, 0 offen**, `vorlaeufig_abgehakt`.
- `daten/fachstatus.csv`, `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md`: synchronisiert.
- Keine Änderung an Bilddateien, anderen Bucheinträgen, Buch-IDs, Positionen oder Fotoreferenzen.

## Bilanz und Halt

- **Fach 5-4:** 22 vorläufig erfasste Bücher, **22 lesbar, 0 prüfen, 0 offen**. **Vorläufig abgehakt** (keine unabhängige physische Nachzählung).
- **Gesamt:** **1048** vorläufige Bucheinträge, **990 lesbar, 20 prüfen, 38 offen** = **58** unsicher.
- **20** fotografierte Fächer vorläufig abgehakt, **7** weitere Fächer in der gezielten Prüfliste, **23** bereits nachgeprüfte Fächer mit Restunsicherheiten, zusätzlich Fach 3-3 mit physischem Zähl-/Positionsbedarf.
- **Nächstes Fach bei neuem „Weiter“: 5-5**, ausschließlich **B00645** und **B00647**.
