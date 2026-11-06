# Fachprüfung 1-6 – zweite Einzelfachkontrolle am 06.11.2026

## Umfang und Bildquelle

- **Ausschließlich Regalfach 1-6** geprüft, kein anderes Regalfach bearbeitet.
- Originalfoto im Git: `bilder/originale/PXL_20261105_151037823.jpg`, Foto-ID `FOTO0003`, laut `daten/fotos.csv` 8160 × 4590 Pixel.
- Die vier originalpixelbasierten Ausschnitte `daten/bildanalyse/fullres/FOTO0003_teil_01.jpg.base64.txt` bis `FOTO0003_teil_04.jpg.base64.txt` wurden einzeln tatsächlich als Bilder angesehen und gegen `daten/buecher.csv` kontrolliert.
- 15 vorläufige physische Bucheinträge mit Buch-IDs `B00015` bis `B00029`, Positionen 1–15 von links nach rechts. Keine neuen Bücher erfunden, keine vorhandenen entfernt.

## Bildgestützter Einzelabgleich

| Position | Buch-ID | Autor bzw. auf dem Rücken genannte Namen | Titel | Fotoausschnitt |
| ---: | --- | --- | --- | ---: |
| 1 | B00015 | Henning Mankell | Der Mann, der lächelte | 1 |
| 2 | B00016 | Henning Mankell | Der Chinese | 1 |
| 3 | B00017 | Jodi Picoult | 19 Minuten | 1 |
| 4 | B00018 | Thomas Mann | Der Zauberberg | 2 |
| 5 | B00019 | Erika Pluhar | Mulldus Erfindungen | 2 |
| 6 | B00020 | Jodi Picoult | Die Wahrheit meines Vaters | 2 |
| 7 | **B00021** | **Hugo Portisch / Sepp Riff** | **Österreich II** | **2/3** |
| 8 | B00022 | Elizabeth George | Wer Strafe verdient | 3 |
| 9 | B00023 | Alexander Solschenizyn | Iwan Denissowitsch | 3 |
| 10 | B00024 | Karin Slaughter | Belladonna | 3 |
| 11 | B00025 | Christoph Ransmayr | Atlas eines ängstlichen Mannes | 3 |
| 12 | B00026 | Alfred Komarek | Narrenwinter | 4 |
| 13 | B00027 | Topsy Küppers | Nix wie Zores! | 4 |
| 14 | B00028 | Timur Vermes | Die Hungrigen und die Satten | 4 |
| 15 | B00029 | Minette Walters | Dunkle Kammern | 4 |

## Eine belegte bibliografische Ergänzung

- **B00021, Position 7:** Das Inventar führte bisher nur **Hugo Portisch** als Verfasser von `Österreich II`.
- Auf `FOTO0003` Teil 2, am Übergang zu Teil 3, stehen auf dem Rücken **„Hugo Portisch · Sepp Riff“**.
- Entsprechend wurden `autor_nachname` von `Portisch` auf `Portisch / Riff` und `autor_vorname` von `Hugo` auf `Hugo / Sepp` aktualisiert. Die beiden Namen bleiben durch Schrägstrich in derselben Reihenfolge gekoppelt.
- **Keine Änderung** an Titel, Buch-ID, Identifikationsstatus, Position oder Fotoquelle. Es handelt sich um **einen** physischen Band.

Die 14 anderen Autoren-/Titelzuordnungen sind mit den sichtbaren Rücken vereinbar, einschließlich des schmalen Erika-Pluhar-Bands, des Solschenizyn-Bands und des großen Werkes von Timur Vermes.

## Git-Änderungen und Integrität

- `daten/buecher.csv`: nur bei `B00021` zweite auf dem Buch sichtbare Namensangabe und Bildbeleg ergänzt.
- `daten/fachstatus.csv`: bisherige veraltete Angabe `Einzelbucherfassung ausstehend` durch den Status dieser zweiten Kontrolle ersetzt.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: unverändert, da keine Bücher in diesem Fach unsicher blieben.
- Originalbild, positionsbenannte Kopie und alle vier Ausschnitte unverändert; keine physische oder alphabetische Umsortierung.

**Ergebnis:** 15/15 sichtbare Bücher **lesbar**, 0 `pruefen`, 0 `offen`, eine Autoren-Ergänzung. Die Sichtprüfung ersetzt keine Untersuchung der Buchinnenseiten.

**Gesamter vorläufiger Inventarstand nach Fach 1-6:** 1048 Bucheinträge, davon 947 `lesbar`, 60 `pruefen`, 41 `offen` (101 ungeklärt). Die Fachanzahl für den zweiten Kontrolllauf erhöht sich auf **13 von 51** fotografierten Regalfächern; **38** verbleiben.

**Nächster Schritt erst nach einem neuen „Weiter“:** ausschließlich Fach **1-7**.
