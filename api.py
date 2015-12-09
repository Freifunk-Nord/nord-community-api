#!/usr/bin/env python

# Von andre at hamburg.freifunk.net , basierend auf https://github.com/freifunkhamburg/ffmap-backend/blob/dev/node_number.py

#Bibliotheken importieren
import time
import datetime
import json
import shutil

Landkreise={
        "Husum":[54.483218, 9.051240],
        "Schleswig":[54.521868, 9.561861],
        "Dithmarschen":[54.211523, 9.120454],
        "Rendsburg":[54.303842, 9.649755],
        "Itzehoe":[53.922188, 9.518219],
        "Segeberg":[53.923483, 10.114170],
        "Neumuenster":[54.085557, 9.977224],
        "Ploen":[54.202036, 10.431209],
        "Cuxhaven":[53.844976, 8.707192],
        "Stade":[53.582963, 9.459456],
        "Harburg":[53.325656, 9.868644]
}

path="/var/www/html/meshviewer/api/"
appendix="-api.json"

#Datei oeffnen
f = open('/var/www/html/meshviewer/data/nodelist.json')

#JSON einlesen
data = json.load(f)

#Nodes attribut aussortieren
nodes = data['nodes']

#Zaehler mit Wert 0 anlegen
num_nodes = 0

#Fuer jeden Knoten in nodes
for node in nodes:
        #Status Attribut aussortieren
        status = node['status']

        #Wenn der Status online entaehlt, hochzaehlen
        if status['online']:
                num_nodes += 1

#Knoten pro Landkreis
Knoten_pro_Landkreis = num_nodes/len(Landkreise)

#Zeit holen
thetime = datetime.datetime.now().isoformat()


for Landkreis in Landkreise:
	LandkreisAPI = path+Landkreis+appendix
	
	#Aus dem Original eine Datei fuer jeden Landkreis erzeugen
	shutil.copy2(path+'Original'+appendix,LandkreisAPI)

	#Freifunk API-Datei einladen und JSON lesen
        ffnord = None
	with open(LandkreisAPI, 'r') as fp:
        	ffnord = json.load(fp)

	#Attribute Zeitstempel und Knotenanzahl setzen
	ffnord['state']['lastchange'] = thetime
	ffnord['state']['nodes'] = Knoten_pro_Landkreis 
	ffnord['location']['city'] = Landkreis
	ffnord['location']['lat'] = Landkreise[Landkreis][0]
	ffnord['location']['lon'] = Landkreise[Landkreis][1]

	#Freifunk API-Datein mit geaenderten werten schreiben
	with open(LandkreisAPI, 'w') as fp:
		json.dump(ffnord, fp, indent=2, separators=(',', ': '))
