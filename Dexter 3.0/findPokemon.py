from operator import itemgetter, attrgetter, methodcaller

### Import csv files for analysis

pokemon_csv = open('pokemon.csv') #data
pokemon_moves_csv = open('pokemon_moves.csv') #movesData
moves_csv = open('moves.csv') #movesNamesMatrix
types_csv = open('types.csv') #typesMatrix
stats_csv = open('stats.csv') #statsMatrix
pokemon_stats_csv = open('pokemon_stats.csv') #statsData

### Break csv files into indexes

def readCSV(csvFile):
	data = []
	for line in csvFile:
		# split each line into a list of items.
		line = line.rstrip()
		items = line.split(',')
		# append this list of items to a variables called "data"
		data.append(items)
	return(data)

data = readCSV(pokemon_csv)
movesData = readCSV(pokemon_moves_csv)
movesNamesMatrix = readCSV(moves_csv)
typesMatrix = readCSV(types_csv)
statsMatrix = readCSV(stats_csv)
statsData = readCSV(pokemon_stats_csv)

### Define minor functions
## Minor functions do not call other functions from this script

def findNamefromNumber(number):
	name = str(data[number][1])
	name = name.capitalize()
	return(name)

def findNumberfromName(name):
	for d in data:
		if d[1] == str(name):
			number = d[2]
			return(number)

def findStatfromNumber(number, stat):
	for line in statsData:
		if line[0] == str(number):
			if line[1] == str(stat):
				statRetrieved = line[2]
	return(statRetrieved)

def findAllStatsfromNumber(number):
	statList = []
	for line in statsData:
		if line[0] == str(number):
			statList.append(line[2])
	return(statList)

def detectNumber(string):
	ifNumber = string.isdigit()
	if ifNumber == True:
		return(True)
	else:
		return(False)

def findDatafromNumber(idNumber):
	# needs id, not dex number, to find megas and forms
	for line in data:
		if line[0] == str(idNumber):
			return(line)

def findMoveset(idNumber):
	moves = []
	for i in movesData:
		#print("moving through movesLine in movesData")
		if i[0] == str(idNumber):
			#print("matches idNumber to line[0]")
			moves.append(i)
	return(moves)

def findMoveName(moveNumber):
	move = ""
	for line in movesNamesMatrix:
		if line[0] == moveNumber:
			move = line[1].capitalize()
	return(move)

def findMovePower(moveNumber):
	move = ""
	for line in movesNamesMatrix:
		if line[0] == moveNumber:
			movePower = line[4]
	return(movePower)

def findMovesStats(moveNumber):
	move = ""
	for line in movesNamesMatrix:
		if line[0] == moveNumber:
			move = line[1].capitalize()
			movePower = line[4]
			movePP = line[5]
			moveAccuracy = line[6]
	return(move, movePower, movePP, moveAccuracy)

def findTypefromTypeID(typeID):
	typeKind = ""
	for line in typesMatrix:
		if line[0] == typeID:
			typeKind = line[1]
	return(typeKind)


def convertLevel(moveset):
	for i in moveset:
		levelLearned = i[4]
		if int(levelLearned) < 10:
			i[4] = "0" + levelLearned
	return(moveset)

### Define semi-major functions
## Semi-major functions call only one other function
## They need to be ordered carefully

def findMovesetFromGeneration(idNumber, generation):
	moves = findMoveset(idNumber)
	moveset = []
	for line in moves:
		if line[1] == str(generation):
			moveset.append(line)
	return(moveset)

def findMoveType(moveID):
	typeID = ""
	moveType = ""
	for line in movesNamesMatrix:
		if line[0] == moveID:
			typeID = line[3]
			moveType = findTypefromTypeID(typeID).capitalize()
	return(moveType)

def findTypeforMoveset(moveset):
	for i in moveset:
		moveType = findMoveType(i[2])
		i.append(moveType)
	return(moveset)

### Define major functions
## Major functions call more than one other function
## They need to be ordered carefully

def findMovesetfromMethod(method, moveset): #levelup, tutor, egg, machine
	
	if method == "levelup": method = "1"
	elif method == "tutor": method = "2"
	elif method == "egg": method = "3"
	elif method == "machine": method = "4"

	newMoveset = []
	
	for line in moveset:
		if line[3] == method:
			move, movePower, movePP, moveAccuracy = findMovesStats(line[2])
			if movePower == "":
				movePower = "-"
			# if int(movePP) < 10:
			# 	movePP = "0" + movePP
			if moveAccuracy == "":
				moveAccuracy = "-"
			# elif int(moveAccuracy) < 100:
			# 	moveAccuracy = "0" + moveAccuracy		
			line.append(move)
			line.append(movePower)
			line.append(movePP)
			line.append(moveAccuracy)
			newMoveset.append(line)
	newMoveset = findTypeforMoveset(newMoveset)
	newMoveset = convertLevel(newMoveset)

	if method == "1":
		newMoveset = sorted(newMoveset, key = itemgetter(int(4)))
	else:
		newMoveset = sorted(newMoveset, key = itemgetter(6))
	return(newMoveset)

def findStats(number, name):

	statList = findAllStatsfromNumber(number)

	print("-----" + name.capitalize() + "-----")
	print("HP is " + str(statList[0]) + ".")
	print("Attack is " + str(statList[1]) + ".")
	print("Defense is " + str(statList[2]) + ".")
	print("Special Attack is " + str(statList[3]) + ".")
	print("Special Defense is " + str(statList[4]) + ".")
	print("Speed is " + str(statList[5]) + ".")

# def findStats(number, name):
# 	i = findAllStatsfromNumber(number)
# 	idNumber, identifier, dex, height, weight, base_exp = i[0], i[1].capitalize(), i[2], i[3], i[4], i[5]
# 	order, is_default, hp, attack, defense, spatk, spdef, speed = i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]
# 	print("******************************************************************")
# 	print(("Stats for ").rjust(20, "-") + identifier.ljust(20, "-"))
# 	# print(name.capitalize() + "'s HP is " + str(hpStat) + ".")
# 	# print(name.capitalize() + "'s Attack is " + str(atkStat) + ".")
# 	# print(name.capitalize() + "'s Defense is " + str(defStat) + ".")
# 	# print(name.capitalize() + "'s Special Attack is " + str(spatkStat) + ".")
# 	# print(name.capitalize() + "'s Special Defense is " + str(spdefStat) + ".")
# 	# print(name.capitalize() + "'s Speed is " + str(speedStat) + ".")

def findMovesetForGeneration(generation, number, name):
	print(">>> In game " + generation + ", " + name.capitalize() + " learns...")
	
	moveset = findMovesetFromGeneration(number, generation)
	levelUpMoveset = findMovesetfromMethod("levelup", moveset)
	machineMoveset = findMovesetfromMethod("machine", moveset)
	tutorMoveset = findMovesetfromMethod("tutor", moveset)

	# Print each moveset with the type
	
	print("******************************************************************")
	### Level Up
	print("By Level Up:")
	if len(levelUpMoveset) == 0:
		print(("     None").ljust(20, " "))
	# Header
	else:
		print("---Move----------------Type------Level----Power--Accuracy----PP---")
	
	# Print moveset
	for i in levelUpMoveset:
		moveName, moveType, moveLevel, movePower, movePP, moveAccuracy = i[6], i[10], i[4], i[7], i[8], i[9]
		print("   " + moveName.ljust(20, " ") + moveType.ljust(10, " ") + 
			("lvl " + moveLevel).ljust(5, " ") + ("").ljust(3, " ") + 
			movePower.rjust(5, " ") + moveAccuracy.rjust(7, " ") + ("").ljust(5, " ") +
			movePP.rjust(2, " ") + (" PP").rjust(3, " "))
	
	print("******************************************************************")
	### Machine
	
	print("By Machine (TM/HM):")
	if len(machineMoveset) == 0:
		print(("     None").ljust(20, " "))
	# Header
	else:
		print("---Move----------------Type---------------Power--Accuracy----PP---")
	
	# Print moveset
	for i in machineMoveset:
		#print(i)
		moveName, moveType, movePower, movePP, moveAccuracy = i[6], i[10], i[7], i[8], i[9]
		print("   " + moveName.ljust(20, " ") + moveType.ljust(10, " ") + 
			("   ").ljust(6, " ") + ("").ljust(3, " ") + 
			movePower.rjust(5, " ") + moveAccuracy.rjust(7, " ") + ("").ljust(5, " ") +
			movePP.rjust(2, " ") + (" PP").rjust(3, " "))

	print("******************************************************************")
	### Tutor

	print("By Tutor:")
	if len(tutorMoveset) == 0:
		print(("     None").ljust(20, " "))
	# Header
	else:
		print("---Move----------------Type---------------Power--Accuracy----PP---")
	
	# Print moveset
	for i in tutorMoveset:
		#print(i)
		moveName, moveType, movePower, movePP, moveAccuracy = i[6], i[10], i[7], i[8], i[9]
		print("   " + moveName.ljust(20, " ") + moveType.ljust(10, " ") + 
			("   ").ljust(6, " ") + ("").ljust(3, " ") + 
			movePower.rjust(5, " ") + moveAccuracy.rjust(7, " ") + ("").ljust(5, " ") +
			movePP.rjust(2, " ") + (" PP").rjust(3, " "))

	### Egg
	if input("Print egg moves? (y/n) >>> ").lower() == "y":
		eggMoveset = findMovesetfromMethod("egg", moveset)
		
		print("******************************************************************")
		print("By Breeding:")
		if len(eggMoveset) == 0:
			print(("     None").ljust(20, " "))
		# Header
		else:
			print("---Move----------------Type---------------Power--Accuracy----PP---")
	
		# Print moveset
		for i in eggMoveset:
			#print(i)
			moveName, moveType, movePower, movePP, moveAccuracy = i[6], i[10], i[7], i[8], i[9]
			print("   " + moveName.ljust(20, " ") + moveType.ljust(10, " ") + 
				("   ").ljust(6, " ") + ("").ljust(3, " ") + 
				movePower.rjust(5, " ") + moveAccuracy.rjust(7, " ") + ("").ljust(5, " ") +
				movePP.rjust(2, " ") + (" PP").rjust(3, " "))

