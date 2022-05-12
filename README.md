# Abdeckung der Zeitungen als Karte

Die Beschreibung in Deutsch folgt hier nach: 

    This repository creates an interactive map (with datawrapper.de software) from wikidata csv exports.
    Geoinformation is derived from the NUTS-Code (EU only) of the relevant regions.
    At the moment this is written in german, because the generated map only reflects german districts and newspapers.
    As soon as the genearation also creates maps for non-german speaking countries I will add an english description.

Blog: https://datengraben.com/posts/2022-05-05-wikidata-datawrapper-regionalzeitungen

Diese Karte stellt die Abdeckung von Regionalzeitungen in Deutschland dar, also die Gebiete über welche Sie berichten.
Die Geoinformationen werden immer für den NUTS3-Code einer Region dargestellt.
In Deutschland sind NUTS3-Code hauptsächlich Landkreise und kreisfreie Städte.


## Karte erstellen

Zur Erstellung der Karte bzw. dem Runterladen und Aggregieren der Daten wird ein Makefile genutzt.
Das Makefile führt ein Pythonskript aus, welches zwei Python-Module benötigt `docopt` und `pandas`.

```shell
pip install -r requirement.txt
make
```
Danach liegen in den beiden erstellen Dateien `merged-nuts-count.csv` (die Anzahl Zeitungen pro NUTS3-Kreis) und `zeitungen-mit-nuts.csv` alle eindeutigen Zuordnungen von Zeitung zu NUTS3-Kreis.
Die CSV-Dateien können mit der von Github gerenderten Oberfläche durchsucht werden.

## Offene Punkte

* [x] Sparql-Queries auslagern
* [x] Automatisches Update https://developer.datawrapper.de/docs/automatic-updates-for-live-data
* [x] Diff nach neuer Berechnung erzeugen und in einer HTML ablegen, so kann ich mir als Nutzer ein Bild machen
* [x] doppelte NUTS auch aus den anderen rausnehmen
* [x] make file sources definieren und rm auf ein paar compiles?
* [ ] History aller commits mit `git-history` erzeugen und visualisieren
