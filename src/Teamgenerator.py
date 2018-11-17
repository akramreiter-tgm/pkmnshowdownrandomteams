import json
from random import randint

def printoutput(mon):
    print(mon["name"] + " @ " + mon["item"])
    print("Ability: " + mon["ability"])
    if mon["level"] > 0:
        print("Level: " + str(mon["level"]))
    if len(mon["ev"]) > 0:
        print ("EVs: " + mon["ev"])
    print(mon["nature"] + " Nature")
    if len(mon["iv"]) > 0:
        print ("IVs: " + mon["iv"])
    for x in mon["moves"]:
        print("- " + x)
    pass

def fullrandom():
    with open("fullrandom.json") as source:
        temp = json.load(source)
        pkmn = temp["pkmn"]
        moves = temp["moves"]
        ability = temp["ability"]
        item = temp["item"]
        nature = temp["nature"]
        mons = [];
        mons.append({});
        mons.append({});
        mons.append({});
        mons.append({});
        mons.append({});
        mons.append({});
        for x in mons:
            x["ev"] = "252 HP / 252 Def / 252 SpD / 252 Spe"
            x["name"] = pkmn[randint(0,len(pkmn)-1)]
            pkmn.remove(x["name"])
            x["nature"] = nature[randint(0,len(nature)-1)]
            nature.remove(x["nature"])
            x["ability"] = ability[randint(0,len(ability)-1)]
            ability.remove(x["ability"])
            x["level"] = 0
            x["iv"] = ""
            x["item"] = item[randint(0, len(item) - 1)]
            item.remove(x["item"])
            x["moves"] = []
            for y in range(0,4):
                x["moves"].append(moves[randint(0, len(moves) - 1)])
                moves.remove(x["moves"][y])

        for x in mons:
            printoutput(x)
            print("")



def generateteams():
    pkmn = []
    fullrandom()
    exit(0)
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
    pass


if __name__ == '__main__':
    generateteams()
