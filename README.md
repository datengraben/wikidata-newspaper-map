# Abdeckung der Zeitungen als Karte

Diese Karte stellt die Abdeckung von Regionalzeitungen in Deutschland dar

Ursprüngliche Abfrage: https://w.wiki/4zS9

* [x] Sehr rudimentäre Abfrage ... ~ 20-30 Zeitungen, manuelle Blacklist für Bild usw.
* [ ] csv in pandas, dann blacklist filtern

* [ ] Für jede Zeitung überprüfen ob diese das Tuple hat für Abdeckung, wenn ja dieses benutzen, wenn nein, dann fallback-methoden benutzen. Diese aber im Bericht vermerken
* [ ] Erstellen eines Berichts (Wie viele Zeitungen habe ich exportiert, Wie viele Regionen sind abgedeckt
* [ ] Abfrage allgemeiner beschreiben, es werden jetzt mehr ungenaue Zeitungen reinkommen. Dafür dann noch gewisse Regeln zusätzlich zur Blacklist definieren (so können Nutzer auch in Wikidata sinnvolle Regeln eintragen um die Applikation zu steuern). Also zum Beispiel Zeitungen die nicht in Deutschland liegen oder nicht in Deutsch geschrieben sind. 

Beispiel für eine ausführlichere Abfrage. Die Teile im Oder ggf. 
alle noch optional und später eine Art Maß/Metrik bauen die das 
Vorkommen der Optionalen Werte einwertet/auswertet <https://w.wiki/4$FT>

## TODO

* [ ] Sparql-Queries auslagern
* [ ] Automatisches Update https://developer.datawrapper.de/docs/automatic-updates-for-live-data
* [ ] History aller commits erzeugen
* [x] Diff nach neuer Berechnung erzeugen und in einer HTML ablegen, so kann ich mir als Nutzer ein Bild machen
* [x] doppelte NUTS auch aus den anderen rausnehmen
* [ ] make file sources definieren und rm auf ein paar compiles?
