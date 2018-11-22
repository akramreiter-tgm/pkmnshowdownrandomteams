# Pokemon Showdown Random Team Generator
developed by KlausRüdiger and ArchmageMomo

# Primary script: Teamgenerator.py
This is the main script for generating teams. At the moment, the following generation methods are supported:
* Fullrandom: Completely random Pokemon, moves and abilities are picked out of all existing ones in gen 7. Only playable in custom battles
* Legitrandom: Random Pokemon are picked and get moves and abilities that it could realistically have in-game. Some currently unpreventable errors due to breeding and event moves and abilities. Most of the time the output teams are playable in Uber.
* Structuredrandom: Picks randomly from premade sets and movesets. Playable in Uber. Currently WIP since the sets are written manually and we don't have unlimited amounts of free time.

## Requirements
The scripts are written in Python 3.7, thus require an installation of it. You also need to install the required packages using `pip install requirements.txt`. We recommend using [virtualenv](https://pypi.org/project/virtualenv/ "virtualenv project page") to keep your host system clean.

## Usage and start parameters
To use the script call `python Teamgenerator.py`. This by itself doesn't do anything without args.

The following args can be used to generate teams:
* -f , --fullrandom: All random, all extreme values. CUSTOM GAMES ONLY
* -lr , --legitrandom: Random teams with legit movesets only.
* -sr , --structuredrandom: Random teams with preset movesets

The following args can be used to modify the generation of teams:
* -fe , --legitrandomfullyevolved: Limits teams to fully evolved pokémon only. Works with -lr
* -lm , --legitrandomlegitmoves: Limits teams to commonly accepted useful moves only. Works with -lr
* -m , --mega: Limits amount of mega evolutions in teams. Works with -sr
* -zm , --zmove: Limits amount of Z moves in teams. Works with -sr
* -c , --choice: Limits amount of choice items in teams. Works with -sr
* -ub , --ultrabeast: Limits amount of ultra beasts in teams. Works with -sr
* -ut , --uniquetypes: Every Pokemon in the team has an unique type. Works with -sr

The following args can make your life a little bit easier:
* -h, , --help: show this help message and exit
* -w , --write: Generates an output file in the local 'C:/Users/<USER>/Documents/My Games/Pokemon Showdown/Teams/full randomized' folder

# Secondary script: LoadData.py
It is used to load the specific data of each Pokemon PokeAPI supports and save it into a .json file. It is meant to be used when the data needs to be updated due to a new generation. The data will most likely be uploaded to this repository anyway, so there is no need to use this script whatsoever. If you really need to, use `python LoadData.py -h`.

