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
