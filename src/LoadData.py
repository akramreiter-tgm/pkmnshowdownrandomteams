import json
import argparse
from pathlib import Path
import requests

papiurl="https://pokeapi.co/api/v2/pokemon/%s/"
maxrequests=1000
specialforms=[
			"deoxys-attack","deoxys-defense","deoxys-speed",
			"diglett-alola","dugtrio-alola","exeggutor-alola","geodude-alola","grimer-alola","golem-alola","graveler-alola","marowak-alola","muk-alola","raticate-alola","rattata-alola","raichu-alola","ninetales-alola","sandshrew-alola","vulpix-alola","sandslash-alola",
			"tornadus-therian","landorus-therian","thundurus-therian",
			"hoopa-unbound",
			"keldeo-resolute",
			"kyurem-black","kyurem-white",
			"oricorio-pau","oricorio-pom-pom","oricorio-sensu",
			"lycanroc-dusk","lycanroc-midnight",
			"necrozma-dawn-wing","necrozma-dusk-mane"
			]

def reassemble():
	"""
	WARNING: Using this script takes a hell of a time. Go on coffee break or something while it runs
	"""
	
	x={}

	for i in range(1,maxrequests):
		try:
			acturl=papiurl % str(i)
			res=requests.get(acturl)
			jout=res.json()
			x[str(i)]={}
			x[str(i)]['name']=jout['name']
			x[str(i)]['items']=[]
			x[str(i)]['abil']=[]
			x[str(i)]['moves']=[]
			for n in jout['abilities']:
				x[str(i)]['abil'].append(n['ability']['name'])
			for n in jout['moves']:
				x[str(i)]['moves'].append(n['move']['name'])
			print("Done: %i"%i)
		except:
			break
			
	lx=len(x)+1
	for i in range(0,len(specialforms)):
		try:
			acturl=papiurl % specialforms[i]
			res=requests.get(acturl)
			jout=res.json()
			x[str(lx)]={}
			x[str(lx)]['name']=jout['name']
			x[str(lx)]['items']=[]
			x[str(lx)]['abil']=[]
			x[str(lx)]['moves']=[]
			for n in jout['abilities']:
				x[str(lx)]['abil'].append(n['ability']['name'])
			for n in jout['moves']:
				x[str(lx)]['moves'].append(n['move']['name'])
			print("Done: %s"%specialforms[i])
		except:
			print("ERROR at %s"%specialforms[i])
		lx+=1
	with open("specialitems.json","r") as specialfile:
		specialitems=json.load(specialfile)
		
	for i in range(1,len(x)):
		if x[str(i)]['name'] in specialitems:
			for n in specialitems[x[str(i)]['name']]:
				x[str(i)]['items'].append(n)
				print("Item for "+x[str(i)]['name']+" loaded: "+n)
	
	with open("temp.json","w") as outfile:
		outfile.write(json.dumps(x, indent=4, sort_keys=True))
		
	
			
if __name__=="__main__":
	reassemble()