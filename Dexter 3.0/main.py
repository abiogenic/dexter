import sys
import os
import glob
import shutil
import random

import save
from operator import itemgetter, attrgetter, methodcaller

wd = os.path.abspath(__file__)
wd = wd.rsplit("/", 1)[0]+"/"
tempFileLocation = wd + "temp_save.csv"

def readCSV(csvFile):
	data = []
	for line in csvFile:
		# split each line into a list of items.
		line = line.rstrip()
		items = line.split(',')
		# append this list of items to a variables called "data"
		data.append(items)
	return(data)

with open('temp_save.csv', 'w') as tempSave:

	request = input("Type 'new' for a new game or 'load' to load a save file. >>> ")
	if request.lower() == 'new':
		print("Starting new game.")	
		loadFile = 0
		characterName = input("What should I call you? >>> ")
		characterGender = input("What is your gender? >>> ")
		tempSave.write("name,gender,level,occupation\n")
		tempSave.write(characterName + "," + characterGender + ",1,beginner\n")


	elif request.lower() == 'load':
		print("Attempting to load most recent save file...")
		loadFile = 1
		saveFile = save.loadSave()
		characterName = save.protagonistsName(saveFile)

	

import wildPokemonEncounter

playerPokemon = []
starterPokemon = wildPokemonEncounter.generatePokemonfromNumber(random.choice([1,4,7]),5)
print(starterPokemon)
playerPokemon.append(starterPokemon)
print(playerPokemon)

listOfPokemonHere = [[16,[12,16],[0,80]],[17,[20,22],[80,100]]]
wildPokemon = wildPokemonEncounter.wildPokemonEncounter(listOfPokemonHere, playerPokemon)

wildPokemonEncounter.pokemonBattle(wildPokemon, playerPokemon)

# print("As a reminder, you can see your menu by entering 'menu' from most input screens. ")
# request = input("Try it! >>> ")
# if request.lower() == 'menu':
# 	save.startMenu(characterName)

#def mainMenu():
	# request = input(">>> ")
	# if request.lower() == 'menu':
	# 	save.startMenu(characterName)