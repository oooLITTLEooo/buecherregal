# Gezielte Nachprüfung Fach 3-6 – 06.11.2026

## Umfang und belegbare Quelle

- Git-Original: `bilder/originale/PXL_20261105_151327949.jpg`, Foto-ID FOTO0019, laut `daten/fotos.csv` **8160 × 4590 Pixel**.
- Native Git-Ausschnitte: `daten/bildanalyse/fullres/FOTO0019_teil_01.jpg.base64.txt` für B00340; `FOTO0019_teil_03.jpg.base64.txt` und `FOTO0019_teil_04.jpg.base64.txt` für B00360.
- Ausschließlich die beiden vorhandenen `pruefen`-Datensätze **B00340** und **B00360** nachgeprüft. Die weiteren 23 Bücher nicht systematisch erneut identifiziert.

## Ergebnisse

| Buch-ID | Pos. | Befund und Entscheidung | Status |
| --- | ---: | --- | --- |
| B00340 | 1 | Auf dem schwarzen Buchrücken in FOTO0019 Teil 01 ist **Veit Heinichen** erkennbar. Der bisherige Inventarfragmenttext **„Kalte Tage des …“** ist im Foto nicht sicher zu lesen und in den konsultierten Heinichen-Werklisten nicht bestätigt. Die Abwesenheit eines Titels in einer Liste beweist nicht, welches Buch vorliegt. **Keine erfundene Titelergänzung.** | **pruefen** |
| B00360 | 21 | Am Bereich von FOTO0019 Teilen 03/04 ist **Garrido** dem Buchrücken und **„Das Pergament …“** als bereits erfasster Titelanfang zugeordnet. Der Verlag **Aufbau** bestätigt den vollständigen Werktitel **Das Pergament des Himmels** und den Autor **Antonio Manuel Garrido**. | **lesbar** |

### Bibliografische Kontrollbelege

- [Aufbau Verlage: Antonio Manuel Garrido und „Das Pergament des Himmels“](https://www.aufbau-verlage.de/autor-in/antonio-manuel-garrido) – Titelnachweis von Originalverlag.
- [Stadtbibliothekskatalog Stendal](https://bibliothek-katalog.stendal.de/Mediensuche/Einfache-Suche?focusModule=searchmodule&module=1&search=himmels&top=y) – führt den Titel als Buch von Antonio Garrido.
- [Literaturhaus Graz: Veit Heinichen und seine Werke](https://www.literaturhaus-graz.at/mitwirkende/veit-heinichen/) – in der verfügbaren Werkliste keine Bestätigung des Fragments „Kalte Tage des …“. Daher bewusst kein Titel geraten.

Die konkrete Auflage/ISBN der Bücher wurde nicht als am Bild nachgewiesen behauptet. Insbesondere ist B00340 **nicht** automatisch als ein anderes Buch Heinichens identifiziert worden.

## Benötigte Aufnahme B00340

Den **ganz linken, breiten schwarzen Rücken** in Fach 3-6 einzeln frontal und scharf aufnehmen (mit Autorenname Veit Heinichen). Falls der Titel nicht zweifelsfrei sichtbar wird, das Exemplar herausziehen und **Titelblatt sowie Vorderseite** fotografieren. Kein erneutes Prüfen derselben Bildausschnitte ohne neue Information.

## Dokumentierte Git-Änderungen

- `daten/buecher.csv`: B00360 vervollständigt, Autorenvorname `Antonio Manuel` und Status `lesbar`. Bei B00340 nur Nachprüfung und Beweisgrenze im Bemerkungsfeld ergänzt; Status `pruefen`, alter Titelfragmentwert und Position unverändert.
- `daten/bildanalyse/feinpruefung_unsicher.csv`: beide Einzelfallprüfungen konkret dokumentiert.
- `daten/pruefplan_faecher.csv` und `daten/fachstatus.csv`: Fach mit offenem Fotobedarf als nachgeprüft geführt, aber nicht abgehakt.
- `docs/PRUEFPLAN_NUR_UNSICHERE_FAECHER_20261106.md`, `docs/protokoll.md` und `docs/inventur_fortschritt.md` synchronisiert.
- Keine Originalfotos, Bildkopien, Buch-IDs, Positionen oder anderen Buchzeilen verändert.

## Inventarstand und Fortsetzung

- Fach 3-6: **25** vorläufig erfasste Bücher, **24 lesbar**, **1 prüfen** (B00340), **0 offen**.
- Gesamtbestand: **1048** vorläufige Bucheinträge, **972 lesbar**, **37 prüfen**, **39 offen** = **76** noch unsicher.
- **17** Fächer vorläufig abgehakt, **18** noch gezielt zu prüfen, **15** bereits gezielt geprüft mit verbliebenen offenen Identifikationen. Fach 3-3 zusätzlich wegen Zähl-/Positionsabweichung zu prüfen.
- **Nächstes Fach erst auf „Weiter“:** Fach **3-7**, ausschließlich **B00373**.
