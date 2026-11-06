# Feinprüfung unsicherer Bucheinträge (2026-11-06)

Grundlage: **159** vorher offene/prüfpflichtige Einträge aus `daten/buecher.csv` (Stand zu Beginn dieser Runde). Es wurden Originalpixel-Bildausschnitte aus `daten/bildanalyse/fullres/` betrachtet, nicht nur die Miniaturvorschauen. Die bearbeiteten Datensätze behalten ihre Buch-ID, ihren unveränderten Originalfoto-Beleg und ihre physische Fachposition. **Die Anzahl der Buchexemplare ist unverändert.**

## Sichtbar bestätigte Korrekturen (27)

| Buch-ID | Fach-Position | Vorher | Nachher | Bildnachweis |
|---|---|---|---|---|
| B00085 | 2-2-6 | Friedell / Egon / Wozu das Theater? / pruefen | Friedell Egon / Wozu das Theater? | FOTO0007 Teil 2 |
| B00087 | 2-2-8 | Freud / Sigmund / Briefe / pruefen | Freud Sigmund / Briefe | FOTO0007 Teil 2 |
| B00102 | 2-2-23 | Reichl / Christoph / Schlaraffenland / pruefen | Reichl Christoph / Schlaraffenland | FOTO0007 Teil 3 |
| B00126 | 2-3-20 | Fitzgerald / F. Scott / Der Fluch der Fitzgeralds / pruefen | Fitzgerald F. Scott / Der Fluch der Fitzgeralds | FOTO0008 Teil 4 |
| B00177 | 2-6-11 | Gordon / Noah / Der Medicus / pruefen | Gordon Noah / Der Medicus | FOTO0011 Teil 3 |
| B00211 | 2-7-28 | Greene / Graham / Zentrum des Schreckens / pruefen | Greene Graham / Zentrum des Schreckens | FOTO0012 Teil 4 |
| B00251 | 3-1-22 | Hammerl / Elfriede / Schuldgefühle sind schön / pruefen | Hammerl Elfriede / Schuldgefühle sind schön | FOTO0014 Teil 3 |
| B00919 | 7-1-6 | Dutzler / Herbert / Letzter Applaus / pruefen | Dutzler Herbert / Letzter Applaus | FOTO0046 Teil 2 |
| B00923 | 7-1-10 | Hackl / Erich / Entwurf einer Liebe auf den ersten Blick / pruefen | Hackl Erich / Entwurf einer Liebe auf den ersten Blick | FOTO0046 Teil 3 |
| B00932 | 7-1-19 | Hammerl / Elfriede / Wunderbare Valerie / pruefen | Hammerl Elfriede / Wunderbare Valerie | FOTO0046 Teil 4 |
| B00942 | 7-2-10 | Noort / Tamar / Die Ewigkeit ist ein guter Ort / pruefen | Noort Tamar / Die Ewigkeit ist ein guter Ort | FOTO0047 Teil 3 |
| B00971 | 7-4-2 | Fielding / Joy / Tanz, Püppchen, tanz / pruefen | Fielding Joy / Tanz, Püppchen, tanz | FOTO0049 Teil 1 |
| B00982 | 7-4-13 | Walker / Martin / Eskapaden / pruefen | Walker Martin / Eskapaden | FOTO0049 Teil 3 |
| B00985 | 7-4-16 |  /  /  / offen | French Tana / Grabesgrün | FOTO0049 Teil 3 |
| B00992 | 7-5-5 | Irving / John / Der letzte Sessellift / pruefen | Irving John / Der letzte Sessellift | FOTO0050 Teil 2 |
| B01009 | 7-5-22 |  /  / Einsiedlerkrebse / pruefen | Ragde Anne B. / Einsiedlerkrebse | FOTO0050 Teil 4 |
| B01010 | 7-6-1 | Merburg / Marie / Sommerflimmern / pruefen | Merburg Marie / Sommerflimmern | FOTO0051 Teil 1 |
| B01011 | 7-6-2 | Ragde / Anne B. / Die Liebesangst / pruefen | Ragde Anne B. / Die Liebesangst | FOTO0051 Teil 1 |
| B01013 | 7-6-4 | Torberg / Friedrich /  / offen | Torberg Friedrich / Auch Nichtarier müssen sterben | FOTO0051 Teil 1 |
| B01014 | 7-6-5 | Scharsach / Hans-Henning / Stille Macht / pruefen | Scharsach Hans-Henning / Stille Machtergreifung | FOTO0051 Teil 1 |
| B01021 | 7-6-12 | Crombie / Deborah / Das verlorene Gedicht / Böses Erwachen / pruefen | Crombie Deborah / Das verlorene Gedicht / Böses Erwachen | FOTO0051 Teil 3 |
| B01025 | 7-6-16 | Ladstätter / Maja / Engel des Vergessens / pruefen | Haderlap Maja / Engel des Vergessens | FOTO0051 Teil 3 |
| B01029 | 7-6-20 |  /  / Aphorismen zur Lebenskunst / pruefen | Schopenhauer Arthur / Aphorismen zur Lebensweisheit | FOTO0051 Teil 4 |
| B01036 | 7-7-4 | Fried / Erich / Vorübungen für Wunder / pruefen | Fried Erich / Vorübungen für Wunder | FOTO0052 Teil 1 |
| B01039 | 7-7-7 | Raab / Thomas / Der Metzger sieht rot / pruefen | Raab Thomas / Der Metzger sieht rot | FOTO0052 Teil 2 |
| B01044 | 7-7-12 | Ragde / Anne B. / Tod im Fjord / Mord in Spitzbergen / pruefen | Ragde Anne B. / Tod im Fjord / Mord in Spitzbergen | FOTO0052 Teil 3 |
| B01046 | 7-7-14 | Maurer / Jörg / Die große Hitze / pruefen | Maurer Jörg / Die große Hitze | FOTO0052 Teil 4 |

## Nicht aufgelöste Fälle und weitere Schritte

- Noch unsichere Einträge sind in `daten/bildanalyse/feinpruefung_unsicher.csv` dokumentiert. Der Status `bleibt_unsicher_nach_bildpruefung` bedeutet: vorhandene Originalbildausschnitte dieses Faches betrachtet, ohne belastbare Vervollständigung der jeweiligen Buchinformation.
- `weitere_feinpruefung_ausstehend` ist **nicht** als geprüft oder erledigt anzusehen. Weitere Fächer spaltenweise anhand derselben Quelle nachprüfen.
- Nicht sichtbare Rückseiten, verdeckte Titel oder gegeneinander verschobene Bände lassen sich auch aus einer vorhandenen Aufnahme mit vergrößerten Bildausschnitten nicht zuverlässig rekonstruieren. Konkrete Zusatzaufnahme vor Ort ist dann erforderlich.
- Bildausschnitte sind JPG-Rekodierungen der **Originalpixel mit unverändertem Bildmaßstab**, das Original selbst bleibt unverändert. Zusätzliche JPEG-Kompression bringt keine neue Schärfe; für Grenzfälle den Originalpixelbereich möglichst verlustfrei neu ausschneiden.
- Fehlende Detailfotos: 8-1 und 8-2, sowie Sichtkontrolle 7-8.

## Zweiter Originalpixel-Prüfblock am 06.11.2026 – 25 zusätzliche sichere Identifizierungen

Die vorhandenen nativen Originalpixel-Ausschnitte zu den zuvor unsicheren Bucheinträgen wurden nach Fachposition erneut gelesen. Alle 51 vorhandenen Detailfotos sind berücksichtigt; für FOTO0042 (Fach 6-5) waren in der verbundenen GitHub-Auslieferung nur Teile 1 und 2 als Bild dekodierbar. Teile 3 und 4 blieben beim Lesen leer – ihre Zuordnung ist ausdrücklich nicht abgeschlossen. Bei verbleibenden Unklarheiten kein Titel geraten.

| ID | Fach / Position | Alte Lesung | Aus dem Fotobereich bestätigt | Git-Bildausschnitt |
| --- | --- | --- | --- | --- |
| B00309 | 3-4 / 8 | Walter, Ilse / Passende Wüste für Fata Morgana gesucht [pruefen] | Walter, Ilse / Passende Wüste für Fata Morgana gesucht | FOTO0017 Teil 2 |
| B00311 | 3-4 / 10 | Walser, Martin / Der Hexer [pruefen] | Walser, Martin / Der Hexer | FOTO0017 Teil 3 |
| B00393 | 3-8 / 11 | Wecker, Konstantin / offen [offen] | Wecker, Konstantin / Schon Schweigen ist Betrug: Die kompletten Liedtexte | FOTO0021 Teil 4 |
| B00401 | 4-1 / 1 | Kappacher, Walter / Der Fliege [pruefen] | Kappacher, Walter / Der Fliege | FOTO0022 Teil 1 |
| B00419 | 4-2 / 2 | Tegetthoff, Folke / Kräutermärchen [pruefen] | Tegetthoff, Folke / Kräutermärchen | FOTO0023 Teil 1 |
| B00423 | 4-2 / 6 | Sperber, Manès / Churban [pruefen] | Sperber, Manès / Churban | FOTO0023 Teil 2 |
| B00457 | 4-4 / 1 | Barons, Eva / Sehnsucht nach Salina [pruefen] | Bakos, Eva / Sehnsucht nach Salina | FOTO0025 Teil 1 |
| B00498 | 4-6 / 8 | Altenberg, Peter / Sonnenuntergang im Prater [pruefen] | Altenberg, Peter / Sonnenuntergang im Prater | FOTO0027 Teil 2 |
| B00547 | 4-8 / 5 | Lukas, Leo / Mörder Quoten [pruefen] | Lukas, Leo / Mörder Quoten | FOTO0029 Teil 2 |
| B00595 | 5-2 / 15 | Adamson, Joy / Die Löwin Elsa und ihre Jungen [pruefen] | Adamson, Joy / Die Löwin Elsa und ihre Jungen | FOTO0031 Teil 3 |
| B00628 | 5-4 / 7 | offen, offen / offen [offen] | Galloway, Steven / Der Cellist von Sarajevo | FOTO0033 Teil 2 |
| B00632 | 5-4 / 11 | Bock, Ute / Zeit im Wind [pruefen] | Sparks, Nicholas / Zeit im Wind | FOTO0033 Teil 3 |
| B00669 | 5-6 / 5 | Wieninger, Manfred / Die Spur der Katzen [pruefen] | Wieninger, Manfred / Die Spur der Katzen | FOTO0035 Teil 2 |
| B00690 | 5-7 / 2 | Danella, Utta / offen [offen] | Danella, Utta / Wo hohe Türme sind | FOTO0036 Teil 1 |
| B00698 | 5-7 / 10 | Komarek, Alfred / Polt [pruefen] | Komarek, Alfred / Polt | FOTO0036 Teil 3 |
| B00714 | 5-8 / 8 | Walser, Martin / Femme fatale [pruefen] | Walser, Martin / Femme fatale | FOTO0037 Teil 2 |
| B00735 | 6-1 / 9 | Dahl, Arne / Misterioso / Böses Blut [pruefen] | Dahl, Arne / Misterioso / Böses Blut | FOTO0038 Teil 2 |
| B00752 | 6-2 / 3 | Wagner, Christoph / Schattenbach [pruefen] | Wagner, Christoph / Schattenbach | FOTO0039 Teil 1 |
| B00754 | 6-2 / 5 | Walser, Martin / Protokolleure [pruefen] | Walser, Martin / Protokolleure | FOTO0039 Teil 2 |
| B00765 | 6-2 / 16 | Eschbach, Andreas / NSA [pruefen] | Eschbach, Andreas / NSA | FOTO0039 Teil 3 |
| B00766 | 6-2 / 17 | Ansh..., Martin / Typisch Welt [offen] | Amanshauser, Martin / Typisch Welt | FOTO0039 Teil 4 |
| B00774 | 6-3 / 5 | Stermann, Dirk / 6 österreichische ... [pruefen] | Stermann, Dirk / 6 Österreicher unter den ersten 5 | FOTO0040 Teil 1 |
| B00895 | 6-8 / 4 | offen, offen / offen [offen] | Muliar, Fritz / Streng indiskret! | FOTO0045 Teil 1 |
| B00898 | 6-8 / 7 | Köpf, Gerhard / Eulenspiegel [pruefen] | Köpf, Gerhard / Eulensehen | FOTO0045 Teil 2 |
| B00911 | 6-8 / 20 | Besser, Doris Knecht / Besser [pruefen] | Knecht, Doris / Besser | FOTO0045 Teil 4 |

**Kumulative Zweitprüfung:** 52 von ursprünglich 159 vormals unsicheren Datensätzen auf `lesbar` umgestellt; 107 bleiben `offen` oder `pruefen`. Unter ihnen sind teils zwar Titel lesbar, aber Autor, Buchgrenze oder ursprüngliche Positions-ID nicht hinreichend belegt. Ein Bildausschnitt kann kein verdecktes Objekt sichtbar machen. Aktuelle Einzelstatus in `daten/bildanalyse/feinpruefung_unsicher.csv`.

**Wichtige Fachkontrollen:** 6-5 erfordert Nachzugriff auf die Originalpixel der Bildteile 3/4; fehlende zusätzliche Regal-Detailfotos bleiben 8-1, 8-2 sowie Sichtprüfung 7-8. Die physische Reihenfolge und Buchexemplar-Zählung von insgesamt 1048 bleiben vorläufig. Keine alphabetische Umsortierung.

