import json
import argparse
from random import randint
from pathlib import Path
import os

parser = argparse.ArgumentParser()

# Extend if needed
parser.add_argument("-w", "--write",
                    help="If 'True' it generates an output file in the local 'C:/Users/<USER>/Documents/My Games/Pokemon Showdown/Teams/full randomized' folder",
                    type=bool, required=False, default=False, nargs='?', const=True)

args = parser.parse_args()


def returnoutput(mons):
    """
    Returns the generated Pokémon in the right format.
    """
    outtext = ""
    for mon in mons:
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
    return (outtext)


def writeoutput(mons, out):
    """
    Writes the generated Pokémon to a file in the given directory. DOES ONLY WORK WITH THE DESKTOP APP ATM
    TODO: find a solution for browser version
    """
    outpath = "%s\\Documents\\My Games\\Pokemon Showdown\\Teams\\%s" % (Path.home(), out)
    numberset = []
    outfilename = "[gen7] Generated %s " % out

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
    with open("fullrandom.json") as source:
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
        nature.remove(x["nature"])
        x["ability"] = ability[randint(0, len(ability) - 1)]
        ability.remove(x["ability"])
        x["level"] = 0
        x["iv"] = ""
        x["item"] = item[randint(0, len(item) - 1)]
        item.remove(x["item"])
        x["moves"] = []
        for y in range(0, 4):
            x["moves"].append(moves[randint(0, len(moves) - 1)])
            moves.remove(x["moves"][y])

    print(returnoutput(mons))
    print("")

    if (args.write):
        writeoutput(mons, "full randomized")


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


def generateteams(case=0):
    """
    Calls another function. Only exists for possible UI tbh.
    """
    if case == 0:
        fullrandom()


if __name__ == '__main__':
    generateteams()