# Gezielte Nachprüfung nur unsicherer Regalfächer (Stand 2026-11-07)

## Beschluss und Regeln

Ab sofort **ausschließlich Bücher prüfen, deren `identifikationsstatus` in `daten/buecher.csv` `pruefen` oder `offen` ist**, sowie gesonderte Unklarheiten bei Anzahl oder physischer Zuordnung. Kein erneutes vollständiges Lesen sicher erfasster Fächer. **Genau ein Fach pro Benutzeraufforderung `Weiter`**, anschließend Bericht und überprüfter Git-Commit. Die 51 bisher vorhandenen Fachfotos bleiben unverändert. Nie Titel erraten.

Dies ist ein Arbeitsplan aus der **momentanen Git-Inventarliste**, keine neue Bildprüfung der hier vorläufig abgehakten Fächer. `lesbar` kann im ersten Inventurdurchgang gesetzt worden sein; ein vorläufiges Abhaken ist deshalb **keine unabhängige zweite Sichtprüfung**. Bei später entdeckten Widersprüchen, Zählfehlern oder neuen Detailfotos wird ein Fach erneut geöffnet.

Maschinenlesbare vollständige Übersicht: `daten/pruefplan_faecher.csv`. Nach jeder weiteren gezielten Fachprüfung muss auch dieser Arbeitsplan bei veränderten Unsicherheiten aktualisiert werden; **`daten/buecher.csv` bleibt maßgeblich**.

## Zusammenfassung

- Raster: **64** Fachpositionen, davon **51** mit Foto und vorhandenen Bucheinträgen.
- **21** fotografierte Fächer mit `0` offenen/prüfpflichtigen Bucheinträgen → **vorläufig abhaken**.
- **29** fotografierte Fächer mit zusammen **50** `pruefen`/`offen`-Einträgen.
- Von diesen 29 ist **1** noch nicht in der neuen fachweisen Nachkontrolle behandelt worden → als nächstes **gezielt nur die unsicheren Bücher prüfen**.
- **28** weitere wurden bereits mit den einschlägigen Originalpixel-Ausschnitten erneut geprüft, bleiben aber ungeklärt → erneute identische Bildprüfung ohne neuen Hinweis vermeiden; bei Bedarf neues Detailfoto.
- **2** fotografierte Fächer mit gesondertem Positions-/Zählabgleich: 3-3 (möglicher zusätzlicher Band *Deutschlandreise*) und 5-3 (neben einem dunklen Buchrücken auch gelber Brecht-Rücken *Der gute Mensch von Sezuan* sichtbar).
- Daneben **13 Positionen ohne Fachdetailfoto**: 3 mit Foto- oder Sichtbedarf, 6 mit unklarer/leer wirkender Belegung, 4 laut Übersicht leer oder mit Lampe.
- Global: **1048** vorläufige Exemplare, davon **998 lesbar, 13 prüfen, 37 offen**. Fotos, Buch-IDs und positionsbezogene Originalreferenzen werden nicht geändert.

## Vorläufig abgehakt — 21 Fächer

- `1-5` — zweite Sichtprüfung durchgeführt
- `1-6` — zweite Sichtprüfung durchgeführt
- `1-7` — gezielte Nachprüfung B00034 erfolgreich, siehe `docs/fachpruefung_1-7_20261106.md`
- `1-8` — gezielte Nachprüfung B00055 erfolgreich, siehe `docs/fachpruefung_1-8_20261106.md`
- `2-5` — gezielte Nachprüfung beider unklarer Buchrücken erfolgreich, siehe `docs/fachpruefung_2-5_20261106.md`
- `2-6` — gezielte Nachprüfung B00170 erfolgreich, siehe `docs/fachpruefung_2-6_20261106.md`
- `2-7` — alle drei verbleibenden Unsicherheiten nach Bild- und Bibliografieprüfung geklärt, siehe `docs/fachpruefung_2-7_20261106.md`
- `3-2` — B00277 als gemeinsames Buch von Ben und Daniela Segenreich identifiziert; Bericht `docs/fachpruefung_3-2_20261106.md`
- `3-5` — vier zuvor unsichere Buchrücken vollständig geklärt und korrigiert; Bericht `docs/fachpruefung_3-5_20261106.md`
- `3-8` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `4-1` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `4-4` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `4-5` — drei verbliebene Unsicherheiten aus FOTO0026 geklärt, siehe `docs/fachpruefung_4-5_20261106.md`
- `4-8` — beide verbliebenen Buchidentifikationen (Richard Picker, Arthur Schnitzler) geklärt, siehe `docs/fachpruefung_4-8_20261106.md`
- `5-4` — B00627 (Dieter Noll), B00631 (Hanns Marzini), B00642 (Melitta Breznik) geklärt, siehe `docs/fachpruefung_5-4_20261107.md`
- `6-2` — B00767 als Alfred Komarek / János Kalmár, *Schräge Vögel: Faszinierende Lebensentwürfe* (Text/Fotos) identifiziert; Bericht `docs/fachpruefung_6-2_20261107.md`
- `6-3` — nur im ersten Inventurdurchgang erfasst, keine offenen Datensätze
- `6-5` — zweite Sichtprüfung durchgeführt
- `6-7` — zweite Sichtprüfung durchgeführt
- `7-2` — zweite Sichtprüfung durchgeführt
- `7-4` — zweite Sichtprüfung durchgeführt

## Noch gezielt prüfen — 1 Fach

Reihenfolge folgt der Regalnummerierung. Nur die betroffenen IDs öffnen und einen passenden Bildausschnitt lesen; klar lesbare Bücher nicht erneut bearbeiten.

| Fach | Unsichere Bücher | IDs |
| --- | ---: | --- |
| 6-4 | 2 | `B00804`, `B00811` |

**Nächstes Fach:** `6-4`, ausschließlich **B00804** und **B00811**.

## Bereits erneut geprüft, aber weiterhin ungeklärt — 28 Fächer

Diese Fächer sind **nicht** abgehakt. Ohne neue Fotodetails oder einen anderen konkret vielversprechenden Bildansatz nicht erneut dieselben Ausschnitte verarbeiten:

| Fach | Offen/Prüfen | IDs | Fachbericht |
| --- | ---: | --- | --- |
| 2-1 | 3 | `B00061`, `B00071`, `B00078` | `docs/fachpruefung_2-1_20261106.md` |
| 2-2 | 1 | `B00094` | `docs/fachpruefung_2-2_20261106.md` |
| 2-3 | 1 | `B00123` | `docs/fachpruefung_2-3_20261106.md` |
| 2-4 | 1 | `B00131` | `docs/fachpruefung_2-4_20261106.md` |
| 2-8 | 1 | `B00226` | `docs/fachpruefung_2-8_20261106.md` |
| 3-1 | 3 | `B00235`, `B00240`, `B00258` | `docs/fachpruefung_3-1_20261106.md` |
| 3-4 | 1 | `B00318` | `docs/fachpruefung_3-4_20261106.md` |
| 3-6 | 1 | `B00340` | `docs/fachpruefung_3-6_20261106.md` |
| 3-7 | 1 | `B00373` | `docs/fachpruefung_3-7_20261106.md` |
| 4-2 | 2 | `B00418`, `B00433` | `docs/fachpruefung_4-2_20261106.md` |
| 4-3 | 2 | `B00448`, `B00454` | `docs/fachpruefung_4-3_20261106.md` |
| 4-6 | 1 | `B00492` | `docs/fachpruefung_4-6_20261106.md` |
| 4-7 | 3 | `B00516`, `B00518`, `B00540` | `docs/fachpruefung_4-7_20261106.md` |
| 5-1 | 1 | `B00563` | `docs/fachpruefung_5-1_20261106.md` |
| 5-2 | 1 | `B00585` | `docs/fachpruefung_5-2_20261107.md` |
| 5-3 | 2 | `B00600`, `B00604` | `docs/fachpruefung_5-3_20261107.md` |
| 5-5 | 2 | `B00645`, `B00647` | `docs/fachpruefung_5-5_20261107.md` |
| 5-6 | 2 | `B00686`, `B00688` | `docs/fachpruefung_5-6_20261107.md` |
| 5-7 | 1 | `B00706` | `docs/fachpruefung_5-7_20261107.md` |
| 5-8 | 1 | `B00711` | `docs/fachpruefung_5-8_20261107.md` |
| 6-1 | 2 | `B00727`, `B00748` | `docs/fachpruefung_6-1_20261107.md` |
| 6-6 | 3 | `B00848`, `B00860`, `B00869` | `docs/fachpruefung_6-6_20261106.md` |
| 6-8 | 1 | `B00896` | `docs/fachpruefung_6-8_20261106.md` |
| 7-1 | 1 | `B00916` | `docs/fachpruefung_7-1_20261106.md` |
| 7-3 | 3 | `B00953`, `B00954`, `B00957` | `docs/fachpruefung_7-3_20261106.md` |
| 7-5 | 3 | `B01001`, `B01007`, `B01008` | `docs/fachpruefung_7-5_20261106.md` |
| 7-6 | 3 | `B01017`, `B01030`, `B01031` | `docs/fachpruefung_7-6_20261106.md` |
| 7-7 | 1 | `B01035` | `docs/fachpruefung_7-7_20261106.md` |

## Fach mit besonderem Positions-/Zählabgleich

- **3-3** – B00292 (C. G. Jung, *Erinnerungen, Träume, Gedanken*) und B00300 (Jakob Wassermann, *Etzel Andergast*) sicher identifiziert. FOTO0016 Teil 02 zeigt neben Eva Rossmann *Alles rot* einen zusätzlichen schmalen Rücken mit John Irving / *Deutschlandreise*, Teil 03 zeigt anschließend den Jung-Band. Mögliches 22. physisches Buch statt 21 erfassten Einträgen. Die bisherige Buchzählung und die Positionen ab dieser Stelle sind **vorläufig**. Keine neue ID oder Positionsverschiebung ohne erneute Sicherung. Nachfoto oder Nachzählung von *Alles rot* bis Jung erforderlich. Siehe `docs/fachpruefung_3-3_20261106.md`.

**Zusatzkontrolle 5-3:** FOTO0032 Teil 01 zeigt zwischen Ann Granger *Wer andern eine Grube gräbt* und Fabio Geda *Im Meer schwimmen Krokodile* neben einem breiten dunklen Rücken einen schmalen gelben Rücken *Bertolt Brecht – Der gute Mensch von Sezuan*. Es ist noch nicht geklärt, ob ein separat zu inventarisierender Band fehlt und wie B00604 zugeordnet werden muss. Bis zu einer physischen Fachzählung bleiben alle IDs und Positionen unverändert; siehe `docs/fachpruefung_5-3_20261107.md`.

## Fächer ohne eigene Detailbilder

- `7-8`: durch Gegenstand verdeckt, Belegung unklar — zusätzliches Foto/Einblick.
- `8-1`, `8-2`: Bücher laut Gesamtansicht vorhanden — Detailbilder erforderlich.
- `8-3` bis `8-8`: laut Gesamtbild leer/unklar — tatsächliche Belegung bestätigen.
- `1-1` bis `1-3`: laut Gesamtbild leer. `1-4`: Lampe.

## Aktualisierung nach jeder Fachprüfung

1. Nur ein Fach und dessen unsichere Buch-IDs anhand der vorhandenen Originalpixel prüfen.
2. `daten/buecher.csv` und `daten/bildanalyse/feinpruefung_unsicher.csv` nur bei belegbaren Korrekturen ändern; Besonderheiten in einem Fachprüfbericht nachweisen.
3. Den vorhandenen Fotostatus in `daten/fachstatus.csv` erhalten; keine vorgetäuschte Gewissheit.
4. `daten/pruefplan_faecher.csv` synchronisieren, sobald ein Unsicherheitsstatus wechselt.
5. Nach Commit die CSV-Strukturen, Anzahl, IDs und die Änderung im Git verifizieren. Dann STOP und Ergebnis berichten.

## Separat bemerkte bibliografische Abweichung (kein weiterer Foto-Check)

- In Fach **2-3** ist **B00126 – Der Fluch der Fitzgeralds** derzeit fälschlich **F. Scott Fitzgerald** zugeordnet, obwohl das Werk bibliografisch **John D. Fitzgerald** zugeschrieben wird. Der Datensatz blieb gemäß der Vorgabe, nur unsichere IDs zu bearbeiten, unverändert. Siehe `docs/fachpruefung_2-3_20261106.md`. Bei einer separaten Datenbereinigung korrigieren.
