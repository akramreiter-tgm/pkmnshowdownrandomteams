import json
import argparse
from random import randint
from pathlib import Path
import os
import time
import traceback

parser = argparse.ArgumentParser()

# Extend if needed
parser.add_argument("-w", "--write",
					help="If 'True' it generates an output file in the local 'C:/Users/<USER>/Documents/My Games/Pokemon Showdown/Teams/full randomized' folder",
					type=bool, required=False, default=False, nargs='?', const=True)
parser.add_argument("-f", "--fullrandom",
					help="All random, all extreme",
					type=bool, required=False, default=False, nargs='?', const=True)
parser.add_argument("-lr", "--legitrandom",
					help="Legit random teams.",
					type=bool, required=False, default=False, nargs='?', const=True)

args = parser.parse_args()

def log(tolog):
	datetoday=time.strftime("%Y%m%d-%H%M%S")	
	with open("errorlog_%s"%datetoday,"a") as outfile:
		outfile.write("%s"%(tolog))
		exit(0)

def returnoutput(mons):
	"""
	Returns the generated Pokémon in the right format.
	"""
	outtext = ""
	for mon in mons:
		try:
			outtext += mon["name"] + " @ " + mon["item"] + "\n"
			outtext += "Ability: " + mon["ability"] + "\n"
			if mon["level"] > 0:
				outtext += "Level: " + str(mon["level"]) + "\n"
			if len(mon["ev"]) > 0:
				outtext += "EVs: " + mon["ev"] + "\n"
			outtext += mon["nature"] + " Nature" + "\n"
			if len(mon["iv"]) > 0:
				outtext += "IVs: " + mon["iv"] + "\n"
			for x in mon["moves"]:
				outtext += "- " + x + "\n"
			outtext += "\n"
		except Exception as err:
			log("%s\n}n%s"%(str(mon),str(err)))
	return (outtext)


def writeoutput(mons, out):
	"""
	Writes the generated Pokémon to a file in the given directory. DOES ONLY WORK WITH THE DESKTOP APP ATM
	TODO: find a solution for browser version
	"""
	outpath = "%s\Documents\My Games\Pokemon Showdown\Teams\%s" % (Path.home(), out)
	numberset = []
	outfilename = "[gen7] Generated %s " % out
	
	if not os.path.exists("%s\Documents\My Games\Pokemon Showdown\Teams\%s" % (Path.home(), out)):
		os.makedirs("%s\Documents\My Games\Pokemon Showdown\Teams\%s" % (Path.home(), out))
		with open("%s\Documents\My Games\Pokemon Showdown\Teams\%s\placeholder.drown" % (Path.home(), out),"w") as a:
			pass

	for filename in os.listdir(outpath):
		if filename.endswith(".txt"):
			filename = filename[:-4]
			filename = filename[len(outfilename):]
			numberset.append(int(filename))

	i = 1
	for n in numberset:
		if i + 1 == n:
			break
		i += 1

	with open("%s/[gen7] Generated %s %i.txt" % (outpath, out, i), "w") as outfile:
		outfile.write(returnoutput(mons))


def fullrandom():
	"""
	TODO: Doc comments
	"""
	with open("fullrandom.json","r") as source:
		temp = json.load(source)
	pkmn = temp["pkmn"]
	moves = temp["moves"]
	ability = temp["ability"]
	item = temp["item"]
	nature = temp["nature"]
	ev = ["252 HP","252 Atk","252 Def","252 SpA","252 SpD","252 Spe"]
	mons = []
	for x in range(0, 6):
		mons.append({})
	for x in mons:
		firstev = True
		x["ev"] = ""
		for y in ev:
			if randint(0,1) == 1:
				if firstev:
					firstev = False
					x["ev"] = y
				else:
					x["ev"] = x["ev"] + " / " + y
		x["name"] = pkmn[randint(0, len(pkmn) - 1)]
		pkmn.remove(x["name"])
		x["nature"] = nature[randint(0, len(nature) - 1)]
		x["ability"] = ability[randint(0, len(ability) - 1)]
		x["level"] = 0
		x["iv"] = ""
		x["item"] = item[randint(0, len(item) - 1)]
		x["moves"] = []
		for y in range(0, 4):
			x["moves"].append(moves[randint(0, len(moves) - 1)])
			moves.remove(x["moves"][y])

	print("\n"+returnoutput(mons))
	print("")

	if (args.write):
		writeoutput(mons, "full randomized")


def legitrandom():
	with open("fullrandom.json", "r") as source:
		itemp = json.load(source)
	item = itemp["item"]
	nature = itemp["nature"]
	with open("fullsets.json","r") as source:
		temp=json.load(source)

	mons = []
	for x in range(0, 6):
		mons.append({})
	
	for x in mons:
		ev = [0,0,0,0,0,0]
		for y in range(0,255):
			rng=randint(0,5)
			if ev[rng]==252:
				y+=-1
			else:
				ev[rng]+=2
		x["ev"]="%i HP / %i Atk / %i Def / %i SpA / %i SpD / %i Spe" % (ev[0],ev[1],ev[2],ev[3],ev[4],ev[5])
			
		exit=False
		while exit==False:
			pnr=str(randint(0, len(temp) - 1))
			for i in mons:
				if temp[pnr]["name"] not in i.values():
					x["name"] = temp[pnr]["name"]
					exit=True
		
		ability=temp[pnr]["abil"]
		moves=temp[pnr]["moves"]
		item.append(temp[pnr]["items"])
		
		x["nature"] = nature[randint(0, len(nature) - 1)]
		
		try:
			if len(ability)==1:
				x["ability"] = ability[0]
			else:
				x["ability"] = ability[randint(0, len(ability) - 1)]
		except Exception as err:
			log("Anzahl Ability, Max Index : %i, %i\nPokeset: %s\n\n%s"%(len(ability),len(ability)-1,str(temp[pnr]),str(err)))
		ability.remove(x["ability"])
		x["level"] = 0
		x["iv"] = ""
		x["item"] = item[randint(0, len(item) - 1)]
		item.remove(x["item"])
		x["moves"] = []
		if(len(moves)>=4):
			for y in range(0, 4):
				x["moves"].append(moves[randint(0, len(moves) - 1)])
				moves.remove(x["moves"][y])
		else:
			i=0
			for y in range(0, len(moves)-i):
				x["moves"].append(moves[randint(0, len(moves) - 1)])
				moves.remove(x["moves"][y])
				i+=1
			
	
	print("\n"+returnoutput(mons))
	print("")
	if (args.write):
		writeoutput(mons, "balanced randomized")
		
		
def alexrandom():
	"""
	TODO: Tell me Alex ~~~
	"""
	"""
	with open("generate.json") as source:
		pkmn = json.load(source)["pkmn"]

	print(pkmn)
	temp = {}
	temp["name"] = pkmn[0]["name"]
	setnr = 1
	movenr = 1
	temp["item"] = pkmn[0]["sets"][setnr]["item"]
	temp["ability"] = pkmn[0]["sets"][setnr]["ability"]
	temp["level"] = pkmn[0]["sets"][setnr]["level"]
	temp["ev"] = pkmn[0]["sets"][setnr]["ev"]
	temp["nature"] = pkmn[0]["sets"][setnr]["nature"]
	temp["iv"] = pkmn[0]["sets"][setnr]["iv"]
	temp["moves"] = pkmn[0]["sets"][setnr]["movesets"][movenr]

	for x in pkmn:
		print(x)
	printoutput(temp)
	"""
	pass


def generateteams():
	"""
	Calls another function. Only exists for possible UI tbh.
	"""
	if args.fullrandom:
		fullrandom()
	if args.legitrandom:
		legitrandom()


if __name__ == '__main__':
	generateteams()