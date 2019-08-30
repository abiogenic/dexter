import sys
import os
import glob
import shutil
import random

import findPokemon

def generateIVs():
	IVlist = []
	for i in range(0,6):
		IV = int(random.uniform(0,31))
		IVlist.append(IV)
	return(IVlist)

def generateEVs():
	EVlist = [0,0,0,0,0,0]
	return(EVlist)

def generateStats(baseStatList, IVlist, EVlist, level, nature):
#also nature needed
	statHP = ((2*int(baseStatList[0])+IVlist[0]+EVlist[0]/4)*level/100)+level+10
	statList = [statHP]
	for stat in range(1,6):
		tempStat = (((2*int(baseStatList[stat])+IVlist[stat]+EVlist[stat]/4)*int(level)/100)+5)*int(nature)
		statList.append(tempStat)
	return(statList)

def generatePokemonfromNumber(number,level):
	name = findPokemon.findNamefromNumber(number)
	baseStatList = findPokemon.findAllStatsfromNumber(number)
	moveset = findPokemon.findMovesetFromGeneration(number, 2)
	encounterMoveset = findPokemon.findMovesetfromMethod("levelup", moveset)[-5:-1]
	encounterIVlist = generateIVs()
	encounterEVlist = generateEVs()
	nature = 1
	encounterStatList = generateStats(baseStatList, encounterIVlist, encounterEVlist, level, nature)
	return(name, encounterMoveset, encounterIVlist, encounterEVlist, encounterStatList, nature)

def wildPokemonEncounter(listOfListsOfPokemon, playerPokemon):
	# each list of ListsOfPokemon
	# [number,levelRange,encounterRate]
	encounterDraw = random.randint(0,100)
	for pokemon in listOfListsOfPokemon:
		number = pokemon[0]
		levelRange = pokemon[1]
		encounterRate = pokemon[2]
		if encounterDraw in range(encounterRate[0],encounterRate[1]):
			level = random.randint(levelRange[0],levelRange[1])
			wildPokemon = generatePokemonfromNumber(number, int(level))

	HPstat = int(wildPokemon[4][0])
	name = wildPokemon[0]
	print("-----------------------------------------")
	print("Nice!  A wild " + str(name) + " appeared!")
	print("")
	print("                " + str(name.upper()))
	print("[==============================] HP " + str(HPstat) + "/" + str(HPstat))
	for i in range(0,16):
		print("")

	return(wildPokemon)

def pokemonBattle(wildPokemon, playerPokemon):

	encounterStatList = wildPokemon[4]
	playerStatList = playerPokemon[0][4]
	oppHPstat, oppATKstat, oppDEFstat, oppSPKstat, oppSDFstat, oppSPDstat = int(encounterStatList[0]),int(encounterStatList[1]),int(encounterStatList[2]),int(encounterStatList[3]),int(encounterStatList[4]),int(encounterStatList[5])
	playerHPstat, playerATKstat, playerDEFstat, playerSPKstat, playerSDFstat, playerSPDstat = int(playerStatList[0]),int(playerStatList[1]),int(playerStatList[2]),int(playerStatList[3]),int(playerStatList[4]),int(playerStatList[5])

	print("-----------------------------------------")
	print("Nice!  A wild " + str(wildPokemon[0]) + " appeared!")
	print("")
	print("                " + str(wildPokemon[0].upper()))
	print("[==============================] HP " + str(oppHPstat) + "/" + str(oppHPstat))
	for i in range(0,10):
		print("")
	print("HP " + str(playerHPstat) + "/" + str(playerHPstat) + " [==============================]")
	print("")
	print("")


	return()


		

	









