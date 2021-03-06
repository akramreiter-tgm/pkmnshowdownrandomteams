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
					help="Generates an output file in the local 'C:/Users/<USER>/Documents/My Games/Pokemon Showdown/Teams/full randomized' folder",action='store_true')
					
parser.add_argument("-f", "--fullrandom",
					help="All random, all extreme values. CUSTOM GAMES ONLY",action='store_true')
					
parser.add_argument("-lr", "--legitrandom",
					help="Random teams with legit movesets only.",action='store_true')
					
parser.add_argument("-sr", "--structuredrandom",
					help="Random teams with preset movesets",action='store_true')
						
parser.add_argument("-fe", "--fullyevolved",
					help="Limits teams to fully evolved pokémon only.\nWorks with -lr",action='store_true')
					
parser.add_argument("-lm", "--legitmoves",
					help="Limits teams to commonly accepted useful moves only.\nWorks with -lr",action='store_true')
					
parser.add_argument("-m", "--mega",
					help="Limits amount of mega evolutions in teams.\nWorks with -sr",
					type=int, required=False, default=1, nargs='?', const=True)
			
parser.add_argument("-zm", "--zmove",
					help="Limits amount of Z moves in teams.\nWorks with -sr",
					type=int, required=False, default=1, nargs='?', const=True)
					
parser.add_argument("-c", "--choice",
					help="Limits amount of choice items in teams.\nWorks with -sr",
					type=int, required=False, default=-1, nargs='?', const=True)

parser.add_argument("-ub", "--ultrabeast",
					help="Limits amount of ultra beasts in teams.\nWorks with -sr",
					type=int, required=False, default=-1, nargs='?', const=True)
					
parser.add_argument("-ut", "--uniquetypes",
					help="Every Pokemon in the team has an unique type.\nWorks with -sr", action='store_true')

					
					
args = parser.parse_args()

def log(tolog):
	datetoday=time.strftime("%Y%m%d%H%M%S")
	if not os.path.exists("logs"):
		os.makedirs("logs")
	with open("logs/errorlog_%s.log"%datetoday,"a") as outfile:
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
			log("%s\n}n%s"%(str(mon), str(err)))

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

def ivrandom():
	iv=[]
	for i in range(0,6):	
		iv.append(randint(30,31))
	return("%i HP / %i Atk / %i Def / %i SpA / %i SpD / %i Spe" % (iv[0],iv[1],iv[2],iv[3],iv[4],iv[5]))
	
	
def evrandom():
	ev=[0,0,0,0,0,0]
	for y in range(0,254):
		rng=randint(0,5)
		if ev[rng]==252:
			y+=-1
		else:
			ev[rng]+=2
	for i in range(0,len(ev)):
		if ev[i]%4==2:
			for n in range(0,len(ev)):
				if i != n and ev[n]%4==2:
					f=randint(0,1)
					if f==0:
						ev[i]+=-2
						ev[n]+=2
					else:
						ev[i]+=2
						ev[n]+=-2
	return("%i HP / %i Atk / %i Def / %i SpA / %i SpD / %i Spe" % (ev[0],ev[1],ev[2],ev[3],ev[4],ev[5]))
	
		
		
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
		x["iv"] = ivrandom()
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
	with open("pokewhitelist.json") as source:
		whitelist=json.load(source)
	with open("moveblacklist.json") as source:
		blacklist=json.load(source)
	with open("fullsets.json","r") as source:
		temp=json.load(source)

	mons = []
	for x in range(0, 6):
		mons.append({})
	
	for x in mons:
		x["ev"]=evrandom()
			
		used=[]
		for y in mons:
			try:
				used.append(y["name"])
			except:
				break
			
		exit=False
		while exit==False:
			pnr=str(randint(0, len(temp) - 1))
			for i in mons:
				if temp[pnr]["name"] not in used:
					if (temp[pnr]["name"] in whitelist["whitelist"] and args.fullyevolved) or not args.fullyevolved:
						x["name"] = temp[pnr]["name"]
						exit=True
		
		ability=temp[pnr]["abil"]
		moves=temp[pnr]["moves"]
		itemtemp=item
		for i in range(0,len(temp[pnr]["items"])):
			itemtemp.append(temp[pnr]["items"][i])
		
		x["nature"] = nature[randint(0, len(nature) - 1)]
		
		try:
			if len(ability)==1:
				x["ability"] = ability[0]
			else:
				x["ability"] = ability[randint(0, len(ability) - 1)]
		except Exception as err:
			log("Anzahl Ability, Max Index : %i, %i\nPokeset: %s\n\n%s\n\n%s"%(len(ability),len(ability)-1,str(temp[pnr]),str(err),str(mons)))
		x["level"] = 0
		
		x['iv']=ivrandom()
		
		x["item"] = itemtemp[randint(0, len(item) - 1)]
		item.remove(x["item"])
		x["moves"] = []
		if(len(moves)>=4):
			y=0
			limiter=500
			while y<4:
				rinteger=randint(0, len(moves) - 1)
				if ((moves[rinteger] not in blacklist["blacklist"] and args.legitmoves) or not args.legitmoves) or limiter<=0:
					x["moves"].append(moves[rinteger])
					moves.remove(x["moves"][y])
					y+=1
				else:
					limiter+=-1
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
		
		
def structuredrandom(zmons = 1, megamons = 1, choice = 1, ultrabeast = 1, uniquetypes = False):
	"""
	Formerly known as AlexRandon
	TODO: Implement uniquetypes
	"""
	with open("structeredsets.json","r") as source:
		pkmn = json.load(source)["pkmn"]

	print(pkmn)
	temp = []
	utypes = []
	for x in range(0,6):
		temp.append({})
	for x in temp:
		while True:
			tmon = pkmn[randint(0,len(pkmn) - 1)]
			for tempset in tmon["sets"]:
				if "z" in tempset["tags"]:
					if zmons == 0:
						tmon["sets"].remove(tempset)
						continue
				if "mega" in tempset["tags"]:
					if megamons == 0:
						tmon["sets"].remove(tempset)
						continue
				if "choice" in tempset["tags"]:
					if choice == 0:
						tmon["sets"].remove(tempset)
						continue
				if "ub" in tempset["tags"]:
					if ultrabeast == 0:
						tmon["sets"].remove(tempset)
						continue
				if uniquetypes:
					types = []
					for stri in tempset["tags"]:
						if stri.startswith("mt"):
							types.append(stri)
					broken = False
					for stri in types:
						if stri in types:
							broken = True
					if (broken):
						tmon["sets"].remove(tempset)
						continue

			if len(tmon["sets"]) == 0:
				pkmn.remove(tmon)
				continue
			sets = []
			for y in range(0, len(tmon["sets"])):
				for z in range(0, tmon["sets"][y]["weight"]):
					sets.append(y)
			print(sets)
			setnr = sets[randint(0, len(sets) - 1)]
			temp2set = tmon["sets"][setnr]
			if uniquetypes:
				for stri in temp2set["tags"]:
					if stri.startswith("mt"):
						utypes.append(stri)
			if "z" in temp2set["tags"]:
				zmons -= 1
			if "mega" in temp2set["tags"]:
				megamons -= 1
			if "choice" in temp2set["tags"]:
				choice -= 1
			if "ub" in temp2set["tags"]:
				ultrabeast -= 1
			x["name"] = tmon["name"]
			x["item"] = ""
			x["item"] = temp2set["item"]
			x["ability"] = temp2set["ability"]
			x["level"] = temp2set["level"]
			x["ev"] = temp2set["ev"]
			x["iv"] = temp2set["iv"]
			x["nature"] = temp2set["nature"]
			x["moves"] = temp2set["movesets"][randint(0, len(temp2set["movesets"]) - 1)]

			if len(tmon["group"]) > 0:
				for mon in pkmn:
					if mon["group"] == tmon["group"]:
						pkmn.remove(mon)
			else:
				pkmn.remove(tmon)
			break

	print(temp)
	print(returnoutput(temp))
	pass


def generateteams():
	"""
	Calls another function. Only exists for possible UI tbh.
	"""
	if args.fullrandom:
		fullrandom()
	if args.legitrandom:
		legitrandom()
	if args.structuredrandom:
		structuredrandom(args.zmove, args.mega, args.choice, args.ultrabeast, args.uniquetypes)


if __name__ == '__main__':
	generateteams()