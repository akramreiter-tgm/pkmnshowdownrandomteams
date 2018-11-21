# Pokemon Showdown Random Team Generator
developed by KlausRüdiger and ArchmageMomo

# Teamgenerator.py
This is the main script for generating teams. At the moment, the following generation methods are supported:
- Fullrandom: Completely random Pokemon, moves and abilities are picked out of all existing ones in gen 7. Only playable in custom battles
- Legitrandom: Random Pokemon are picked and get moves and abilities that it could realistically have in-game. Some currently unpreventable errors due to breeding and event moves and abilities. Most of the time the output teams are playable in Uber.
- Structuredrandom: Picks randomly from premade sets and movesets. Playable in Uber. Currently WIP since the sets are written manually and we don't have unlimited amounts of free time.

# LoadData.py
It is used to load the specific data of each Pokemon PokeAPI supports and save it into a .json file. It is meant to be used when the data needs to be updated due to a new generation and the data will most likely be uploaded to this repository anyway.

# usage and start parameters

TODO
