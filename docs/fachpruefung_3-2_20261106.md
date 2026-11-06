# Gezielte Nachprüfung Fach 3-2 – 06.11.2026

## Prüfung

- Maßgebliches Git-Original: `bilder/originale/PXL_20261105_151315040.jpg` (FOTO0015, 8160 × 4590 Pixel nach `daten/fotos.csv`).
- Geprüft wurden die vorhandenen Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0015_teil_03.jpg.base64.txt` und `daten/bildanalyse/fullres/FOTO0015_teil_04.jpg.base64.txt`. Einziger zielgerichtet untersuchter vorher unsicherer Eintrag: **B00277**, Position 18. Keine anderen Buchtitel neu überprüft.
- Das Exemplar ist der dunkelblaue Amalthea-Band direkt nach **Anna Mitgutsch – Zwei Leben und ein Tag** (Position 17), vor **Peter James – So gut wie tot** (Position 19).

## Ergebnis B00277

- **Autoren: Ben Segenreich und Daniela Segenreich**. Beide Vornamen und gemeinsamer Nachname sind auf dem Buchrücken direkt erkennbar.
- **Titel: Fast ganz normal – Unser Leben in Israel**. `Fast ganz normal` ist am Buchrücken eindeutig zu lesen; der Untertitel wurde im Amalthea-Verlagskatalog ergänzend bibliografisch bestätigt.
- **Verlag: Amalthea**, am Buchrücken sichtbar. Veröffentlichung im Verlagskatalog 2018. Für das konkrete Exemplar wird keine nicht ablesbare Auflage oder ISBN behauptet.
- **Status: lesbar.** B00277 wurde von `pruefen` auf `lesbar` geändert und die Verfasserschaft als `autor_nachname=Segenreich`, `autor_vorname=Ben und Daniela` für das gemeinsame Buch im bisherigen Tabellenschema festgehalten.

### Bibliografische Belege

- Amalthea-Verlagskatalog, Frühjahr 2018: https://amalthea.at/wp-content/uploads/2016/12/FJ2018.pdf (Eintrag `Ben & Daniela Segenreich – FAST GANZ NORMAL – UNSER LEBEN IN ISRAEL`).
- Offizieller Verlags-Shop mit Buchtitel und Autor: https://amalthea.at/shop/?buecher=alle
- ORF Ö1-Redaktion zu beiden Autoren und dem Buchtitel: https://oe1.orf.at/programm/20180402/509748/Arik-Brauer-erzaehlt-das-Alte-Testament

## Git-Nachführung

- `daten/buecher.csv`: ausschließlich B00277 um beide Autoren, vollständigen Titel, belegte Fotoangabe und Status `lesbar` ergänzt.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: Einzelfall auf `korrigiert_und_lesbar` mit Foto-Beleg gesetzt.
- `daten/fachstatus.csv` und `daten/pruefplan_faecher.csv`: Fachprüfung dokumentiert und Fach vorläufig abgehakt.
- `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md`, `docs/inventur_fortschritt.md`: synchronisiert.
- **Originalfoto, Kopie, sämtliche IDs, Standort und Positionsnummern unverändert.**

## Bilanz

- Fach 3-2: **21** vorläufig erfasste Bücher, **21 lesbar**, **0 prüfen**, **0 offen**.
- Gesamt: **1048** vorläufige Einträge, **965 lesbar, 43 prüfen, 40 offen** = **83** unsicher.
- **16** Fächer vorläufig abgehakt, **22** noch gezielt nachzuprüfen, **13** bereits nachgeprüft mit offenen Fotofragen.
- Nächstes Fach **erst nach „Weiter“**: **3-3**, nur **B00292** und **B00300**.
