import json

def printoutput():


def generateteams():
    pkmn = []
    with open("generate.json") as source:
        pkmn = json.load(source)["pkmn"]

    temp = {}
    temp["name"]: pkmn[0]
    setnr = 0
    movenr = 0
    temp["item"]: 

    for x in pkmn:
        print(x)
    pass


if __name__ == '__main__':
    generateteams()
