# community-api
Freifunk Community API JSON

Vorbereitung: man muss aus dem Original `nodes.json` eine Datei für jeden Landkreis von hand (mit hilfe des Api Generators) erzeugen

Das script aktualisiert die Anzahl Nodes in allen Landkreis-Dateien, wobei die Anzahl Knoten pro Landkreis nur aproximiert wird indem die Gesamtzahl online Knoten durch die Anzahl Landkreise geteilt wird.

Zum neu generieren einfach das Script ausführen

    api.py
(basierend auf https://github.com/freifunkhamburg/ffmap-backend/blob/dev/node_number.py)

Autor: andre at hamburg.freifunk.net 

Im Script sind die Pfade noch absolut definiert: `/var/www/html/meshviewer/nord-community-api/`
und `/var/www/html/meshviewer/data/nodelist.json`. Diese müssen eventuell angepasst werden
