#!/usr/bin/env python

# Von andre at hamburg.freifunk.net , basierend auf https://github.com/freifunkhamburg/ffmap-backend/blob/dev/node_number.py

#Bibliotheken importieren
import time
import datetime
import json
import shutil

Landkreise={
	"cuxhaven":[53.844976, 8.707192,"","",""],
	#"dithmarschen":[54.211523, 9.120454,"Offener Kanal Westkueste","Landvogt-Johannsen-Strasse 11, Heide","25746"],
	"malente":[],
	"neumuenster":[54.085557, 9.977224,"","",""],
	"nordfriesland":[54.483218, 9.051240,"","",""],
	"nordheide":[53.325656, 9.868644,"","",""],
	"ploen":[54.202036, 10.431209,"","",""],
	"rendsburg-eckernfoerde":[54.303842, 9.649755,"","",""],
	"schleswig":[54.521868, 9.561861,"","",""],
	"segeberg":[53.923483, 10.114170,"","",""],
	"stade":[53.582963, 9.459456,"","",""],
	"steinburg":[53.922188, 9.518219,"","",""],
	"sylt":[],
	"tarp":[]
}

path="/var/www/html/meshviewer/nord-community-api/"
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

#Knoten pro Landkreis (Berechnet aus Gesamtzahl Nodes minus 329 Fix-Knoten in Dittmarschen)
Knoten_pro_Landkreis = (num_nodes-329) / len(Landkreise)

#Zeit holen
thetime = datetime.datetime.now().isoformat()


for Landkreis in Landkreise:
	LandkreisAPI = path+Landkreis+appendix
	
	#Aus dem Original eine Datei fuer jeden Landkreis erzeugen
	#shutil.copy2(path+'Original'+appendix,LandkreisAPI)

	#Freifunk API-Datei einladen und JSON lesen
        ffnord = None
	with open(LandkreisAPI, 'r') as fp:
        	ffnord = json.load(fp)

	#Attribute Zeitstempel und Knotenanzahl setzen
	ffnord['state']['lastchange'] = thetime
	ffnord['state']['nodes'] = Knoten_pro_Landkreis 
	#ffnord['location']['city'] = Landkreis
	#ffnord['location']['lat'] = Landkreise[Landkreis][0]
	#ffnord['location']['lon'] = Landkreise[Landkreis][1]
	#ffnord['location']['address']['Name'] = Landkreise[Landkreis][2]
	#ffnord['location']['address'] ['Street']= Landkreise[Landkreis][3]
	#ffnord['location']['address'] ['Zipcode']= Landkreise[Landkreis][4]

	#Freifunk API-Datein mit geaenderten werten schreiben
	with open(LandkreisAPI, 'w') as fp:
		json.dump(ffnord, fp, indent=2, separators=(',', ': '))
