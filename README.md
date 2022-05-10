# Abdeckung der Zeitungen als Karte

Die Beschreibung in Deutsch folgt hier nach.
This repository creates an interactive map (with datawrapper.de software) from wikidata csv exports.
At the moment this is written in german, because the generated map only reflects german districts and newspapers.
As soon as the genearation also creates maps for non-german speaking countries I will add a english description.

Blog: https://datengraben.com/posts/2022-05-05-wikidata-datawrapper-regionalzeitungen

Diese Karte stellt die Abdeckung von Regionalzeitungen in Deutschland dar, also die Gebiete über welche Sie berichten.

## Karte erstellen

Zur Erstellung der Karte bzw. dem Runterladen und Aggregieren der Daten wird ein Makefile genutzt.
Das Makefile führt aber auch das Pythonskript, welches zwei Python-Module benötigt `docopt` und `pandas`.

```shell
pip install -r requirement.txt
make
```

Das Makefile definiert Quellen und Ziele und löst diese Abhängigkeiten auf.
Im Fall der Karte sind das z.B. die Abfragen definiert als `scripts/*.rq` die Skripte zur Generierung der Inhalte.
Wenn sich z.B. eine Abfrage-Datei ändert wird der Teil der diese Quelle bzw. Ziele enthält erneut ausgeführt.

## Offene Punkte

Ursprüngliche Abfrage: https://w.wiki/4zS9

* [x] Sehr rudimentäre Abfrage ... ~ 20-30 Zeitungen, manuelle Blacklist für Bild usw.
* [x] csv in pandas, dann blacklist filtern

* [ ] Für jede Zeitung überprüfen ob diese das Tuple hat für Abdeckung, wenn ja dieses benutzen, wenn nein, dann fallback-methoden benutzen. Diese aber im Bericht vermerken
* [ ] Erstellen eines Berichts (Wie viele Zeitungen habe ich exportiert, Wie viele Regionen sind abgedeckt
* [ ] Abfrage allgemeiner beschreiben, es werden jetzt mehr ungenaue Zeitungen reinkommen. Dafür dann noch gewisse Regeln zusätzlich zur Blacklist definieren (so können Nutzer auch in Wikidata sinnvolle Regeln eintragen um die Applikation zu steuern). Also zum Beispiel Zeitungen die nicht in Deutschland liegen oder nicht in Deutsch geschrieben sind. 

Beispiel für eine ausführlichere Abfrage. Die Teile im Oder ggf. 
alle noch optional und später eine Art Maß/Metrik bauen die das 
Vorkommen der Optionalen Werte einwertet/auswertet <https://w.wiki/4$FT>

## TODO

* [x] Sparql-Queries auslagern
* [x] Automatisches Update https://developer.datawrapper.de/docs/automatic-updates-for-live-data
* [ ] History aller commits erzeugen
* [x] Diff nach neuer Berechnung erzeugen und in einer HTML ablegen, so kann ich mir als Nutzer ein Bild machen
* [x] doppelte NUTS auch aus den anderen rausnehmen
* [x] make file sources definieren und rm auf ein paar compiles?
