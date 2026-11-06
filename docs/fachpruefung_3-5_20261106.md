# Gezielte Nachprüfung Fach 3-5 – 06.11.2026

## Quelle und Prüfgrenze

- Git-Original: `bilder/originale/PXL_20261105_151324453.jpg` (FOTO0018), 8160 × 4590 Pixel gemäß `daten/fotos.csv`.
- In Git vorhandene Originalpixel-Ausschnitte `daten/bildanalyse/fullres/FOTO0018_teil_01.jpg.base64.txt` bis `_teil_04.jpg.base64.txt` betrachtet. Die zu prüfenden vier Buchrücken sind im Ausschnitt **Teil 02** zu lesen.
- Ausschließlich die zuvor als `pruefen` markierten Bücher **B00329, B00330, B00332, B00333** erneut identifiziert. Andere 12 `lesbar`-Einträge unverändert. Keine Fotos oder Buchpositionen verändert.

## Gezielte Einzelentscheidungen

| Buch-ID | Pos. | Befund | Entscheidung |
| --- | ---: | --- | --- |
| **B00329** | 6 | Im FOTO0018 Teil 02 sind **Gauß / Pollack**, *Das reiche Land der armen Leute* lesbar. Bibliografisch als von **Karl-Markus Gauß und Martin Pollack herausgegebenes** Lesebuch mit Untertitel *Literarische Wanderungen durch Galizien* belegt. Vorher `Grub / Polacek` falsch. | **lesbar** |
| **B00330** | 7 | Auf dem Buchrücken deutlich **Joy Fielding – Träume süß, mein Mädchen**. Vorher *Träume sind mein Mädchen* falsch. | **lesbar** |
| **B00332** | 9 | Buchrücken deutlich **Konstantin Wecker – Dann denkt mit dem Herzen**. Gütersloher Verlagshaus. | **lesbar** |
| **B00333** | 10 | Buchrücken **Gardner – Mord auf der Luxusjacht**. Vollständiger Autor bibliografisch **Erle Stanley Gardner**. | **lesbar** |

### Bibliografische Abgleichbelege

- B00329: <https://www.morawa.at/detail/ISBN-9783851296617/Gau%C3%9F-Karl-Markus/Das-reiche-Land-der-armen-Leute> – Gauß und Pollack sind Herausgeber, nicht die Verfasser sämtlicher Beiträge.
- B00330: <https://www.thalia.at/shop/home/artikeldetails/A1062457117> – Joy Fielding, *Träume süß, mein Mädchen*.
- B00332: <https://wecker.de/portfolio-item/dann-denkt-mit-dem-herzen> – offizielle Seite von Konstantin Wecker, Titel *Dann denkt mit dem Herzen*.
- B00333: <https://www.mordlust.de/erle-stanley-gardner/> – *Mord auf der Luxusjacht* unter Erle Stanley Gardner.

Keine konkrete ISBN oder Auflage der abgebildeten Einzelexemplare behauptet, sofern diese nicht am Rücken nachgewiesen wurde.

## Änderungen im Git

- `daten/buecher.csv`: **nur vier Datensätze** B00329 B00330 B00332 B00333 auf `lesbar` gesetzt und Autor/Titel korrigiert bzw. vervollständigt. Bei B00329 Herausgeberrollen im Bemerkungsfeld präzisiert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: vier Nachprüfergebnisse mit direktem Fotobeleg.
- `daten/pruefplan_faecher.csv`: Fach 3-5 mit 16 lesbar, 0 prüfen, 0 offen vorläufig abgehakt.
- `daten/fachstatus.csv`, Gesamtprüfplan, Inventurfortschritt und Protokoll synchronisiert.
- Originale, Fotokopien, Buch-IDs, Rechts-Links-Zuordnung und Gesamtanzahl unverändert.

## Bilanz und nächster Schritt

- Fach 3-5: **16** vorläufige Bücher, **16 lesbar**, **0 prüfen**, **0 offen**, vorläufig abgehakt.
- Gesamtes Inventar: **1048** vorläufige Einträge, **971 lesbar**, **38 prüfen**, **39 offen** (= **77** unsichere).
- **17** Fächer vorläufig abgehakt, **19** noch gezielt nachzuprüfen, **14** erneut geprüft mit verbliebenen Unsicherheiten, Sonderfall Fach 3-3 mit physischer Buchzählung.
- **Nächstes Fach erst auf „Weiter“:** Fach **3-6**, ausschließlich **B00340** und **B00360**.
