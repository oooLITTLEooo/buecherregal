# Fachprüfung 7-3 – 06.11.2026

## Umfang und Quelle

- In diesem Durchgang **ausschließlich Regalfach 7-3** untersucht.
- Foto-ID `FOTO0048`; Original `bilder/originale/PXL_20261105_151635704.jpg`, laut Foto-Inventar 8160 × 4590 Pixel.
- Alle vier tatsächlichen aus dem Original abgeleiteten hochauflösenden Ausschnitte `daten/bildanalyse/fullres/FOTO0048_teil_01.jpg.base64.txt` bis `FOTO0048_teil_04.jpg.base64.txt` einzeln visuell kontrolliert.
- Bestand vor und nach diesem Durchgang: **18 vorläufige Bucheinträge** `B00952` bis `B00969`. Die Positionen im Fach (1–18) wurden unverändert gelassen, sind aber **nicht abschließend physisch gesichert**, weil ein Band quer hinter der vorderen Reihe liegt.

## Sicher bestätigter Eintrag

| Buch-ID | Position | Autor | Titel | Nachweis |
| --- | ---: | --- | --- | --- |
| B00962 | 11 | Ludwig Hirsch | **Ich weiß es nicht, wohin die Engel fliegen** | FOTO0048, Teil 3; Titel und Autor sind auf dem sichtbaren schwarzen Buchrücken lesbar |

Der Datensatz `B00962` wurde von `pruefen` auf `lesbar` gesetzt, ohne Autor, Titel, ID oder Position zu ändern. Die übrigen zuvor als `lesbar` erfassten Buchrücken wurden stichhaltig auf allen vier Bildteilen abgeglichen, ohne zusätzliche Buchzählung oder spekulative Angaben.

## Drei verbleibende Unklarheiten

| Buch-ID | Vorläufige Position | Status | Bildbefund | Benötigtes Zusatzfoto |
| --- | ---: | --- | --- | --- |
| B00953 | 2 | `offen` | FOTO0048 Teil 1: Hinter den vorderen Büchern liegt ein **eigenständiger schwarzer Band quer**. Auf dem sichtbaren Rücken sind **Rita Mae Brown & Sneaky Pie Brown** zu lesen; der Titel ist durch die aufrecht stehenden Bücher verdeckt. | Quer liegendes Buch kurz herausnehmen und Rücken/Vorderseite fotografieren. Dabei kontrollieren, ob die Zählung/Position der physischen Exemplare noch stimmt. |
| B00954 | 3 | `pruefen` | FOTO0048 Teil 1: heller schmaler Buchrücken, **Die Klinik** ist als Titel sichtbar, Autor nicht sicher abzulesen. | Rücken und Vorderseite bzw. Titelblatt frontal fotografieren. |
| B00957 | 6 | `offen` | FOTO0048 Teil 1: braunroter Rücken, **Rita Mae Brown** erkennbar und Titelanfang **Rache auf …**, Rest nicht sicher lesbar. | Buch herausziehen und Rücken/Vorderseite scharf aufnehmen. |

**Keine erfundenen vollständigen Titel.** Bei B00953 ist die zweite Autorin/Autorenangabe auf dem sichtbaren Rücken dokumentiert; das vorhandene Feldformat wurde nicht unkontrolliert umgebaut.

## Nachweise weiterer vorhandener Einträge

Die Lesungen im bestehenden Inventar sind anhand der sichtbaren Buchrücken nachvollziehbar, darunter:

- B00952 – Rita Mae Brown / Sneaky Pie Brown, *Eine Maus kommt selten allein* (Teil 1).
- B00955 – Heinrich Böll, *Zur Verteidigung der Waschküchen* (Teil 1).
- B00956 – Helene Hanff, *84, Charing Cross Road* (Teil 1).
- B00958 – Joyce Carol Oates, *Geheimnisse* (Teil 2).
- B00959 – Ken Follett, *Das Fundament der Ewigkeit* (Teil 2).
- B00960 – Friedrich Torberg, *Die Tante Jolesch* (Teil 2).
- B00961 – Alice Munro, *Liebes Leben* (Teil 2).
- B00963 – Patricia Highsmith, *Small g – eine Sommeridylle* (Teil 3).
- B00964 – Peter Høeg, *Fräulein Smillas Gespür für Schnee* (Teil 3).
- B00965 – Noah Gordon, *Der Medicus von Saragossa* (Teil 3).
- B00966 – Nina George, *Das Lavendelzimmer* (Teil 3).
- B00967 – Felicitas Mayall, *Hundszeiten* (Teil 4).
- B00968 – Martha Grimes, *Die Trauer trägt Schwarz* (Teil 4).
- B00969 – Kilian Kleinschmidt, *Weil es um die Menschen geht* (Teil 4).

## Git-Änderungen und Qualitätssicherung

- `daten/buecher.csv`: nur B00953, B00954 und B00957 mit genaueren Bildbelegen versehen und B00962 auf `lesbar` gesetzt. **Keine Buch-IDs, Autoren, Titel oder Positionen neu erfunden, verändert oder gelöscht**.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: die vier betroffenen Prüfzeilen mit genauer Sichtbeobachtung dokumentiert, B00962 als `korrigiert_und_lesbar` abgeschlossen.
- `daten/fachstatus.csv`: veralteten Fachvermerk aktualisiert, Anzahl und offene Fälle benannt.
- Originalfoto und positionsbenannte byteidentische Kopie nicht verändert. Keine alphabetische Umsortierung.

## Ergebnis

- Fach **7-3**: 18 vorläufige Bücher, **15 `lesbar`**, **1 `pruefen`**, **2 `offen`**.
- Gesamtbestand unverändert **1048** vorläufige Bücher: **947 `lesbar`**, **60 `pruefen`**, **41 `offen`**. Das sind **101** ungeklärte Einträge.
- Für eine **endgültige physische Zählung und Positionierung** sind besonders die quer gelagerten Bücher zu prüfen.
- **Nächstes Fach erst nach einem neuen „Weiter“: 7-4.**
