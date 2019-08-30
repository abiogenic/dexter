import sys
import os
import glob
import shutil


def readCSV(csvFile):
	data = []
	for line in csvFile:
		# split each line into a list of items.
		line = line.rstrip()
		items = line.split(',')
		# append this list of items to a variables called "data"
		data.append(items)
	return(data)

def loadSave():
	save_csv = open('save.csv') #saveFile
	saveFile = readCSV(save_csv)
	print("Welcome back, " + str(saveFile[1][0]))
	return(saveFile)

def protagonistsName(saveFile):
	name = str(saveFile[1][0])
	return(name)

def checkToSave(characterName):
	request = input("Would you like to save the game? >>> ")
	if request.lower() == 'yes' or 'y':
		print("Saving...")
		shutil.move('temp_save.csv','save.csv')
		print(characterName.capitalize() + " saved the game!")
	return()

def startMenu(characterName):
	request = 0
	print("1. Pokédex")
	print("2. Pokémon")
	print("3. Bag")
	print("4. Save")
	print("5. Settings")
	print("6. Close")
	while request == 0 or 1 or 2 or 3 or 4 or 5:
		request = input(" >>> ")
		if int(request) == 1:
			import Dexter
			return()
		elif int(request) == 2:
			print("You have no Pokémon yet.")
		elif int(request) == 3:
			print("You don't have any items yet.")
		elif int(request) == 4:
			checkToSave(characterName)
		elif int(request) == 5:
			print("LOL there aren't any settings yet.")
		elif int(request) == 6:
			return()
	return()
