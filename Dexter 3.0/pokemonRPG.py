import sys

request = input("Type 'new' for a new game or 'load' to load a save file. >>> ")
if request.lower() == 'new':
	print("Starting new game.")	
	loadFile = 0

elif request.lower() == 'load':
	print("Attempting to load most resent save file...")
	loadFile = 1

import findPokemon
#import Dexter