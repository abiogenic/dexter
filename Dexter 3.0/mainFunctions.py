from operator import itemgetter, attrgetter, methodcaller

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
	name = saveFile[1][0]
	return(name)
