import sys
import findPokemon



print("****************************************")
print("**------------------------------------**")

print(("I AM DÉXTER (v 0.1)").center(40, " "))

print("**------------------------------------**")
print("****************************************")

print("Enter a Pokémon name or national dex number:")
arg1 = input(">>> ")

print("What would you like to know?")
print("1. Moveset")
if input(">>> ") == "1":
	print("1. red/blue")
	print("2. yellow")
	print("3. gold/silver")
	print("4. crystal")
	print("5. ruby/sapphire")
	print("6. emerald")
	print("7. firered/leafgreen")
	print("8. diamond/pearl")
	print("9. platinum")
	print("10. heartgold/soulsilver")
	print("11. black/white")
	print("12. colosseum")
	print("13. xd")
	print("14. black2/white2")
	print("15. x/y")
	print("16. omegaruby/alphasapphire")
	generation = input(">>> ")
else: quit

arg2 = ""

### Check for additional arguments and assign them values

#if len(sys.argv) > 1:
#	arg1 = sys.argv[1]
if len(sys.argv) > 2:
	arg2 = sys.argv[2]
if len(sys.argv) > 3:
	arg3 = sys.argv[3]

### Determine if first input (arg1) is number or name
### Assign number and name values

isDexNumber = findPokemon.detectNumber(arg1)
if isDexNumber == True:
	number = int(arg1)
	name = findPokemon.findNamefromNumber(number)
	#print(name, number)

elif isDexNumber == False:
	name = str(arg1)
	number = findPokemon.findNumberfromName(name)
	number = int(number)
	#print(name, number)

### If user asks for number, return it

if arg2.lower() == "number":
	print(">>> Finding Pokémon's national Pokédex number from name...")
	print(name.capitalize() + "'s number is " + str(number) + ".")

### If user asks for name, return it

if arg2.lower() == "name":
	print(">>> Finding name from number...")
	print("Pokémon #" + str(number) + " is " + name + ".")

### If user asks for stat, find which and return it or all

if arg2.lower() =="stat":
	statRequested = arg3.lower()

	if statRequested.lower() == "all":
		hpStat, atkStat, defStat, spatkStat, spdefStat, speedStat = findPokemon.findAllStatsfromNumber(number)
		print(">>> Finding all stats for " + name.capitalize() + "...") 
		print(name.capitalize() + "'s HP is " + str(hpStat) + ".")
		print(name.capitalize() + "'s Attack is " + str(atkStat) + ".")
		print(name.capitalize() + "'s Defense is " + str(defStat) + ".")
		print(name.capitalize() + "'s Special Attack is " + str(spatkStat) + ".")
		print(name.capitalize() + "'s Special Defense is " + str(spdefStat) + ".")
		print(name.capitalize() + "'s Speed is " + str(speedStat) + ".")
	
	else:
		print(">>> Finding " + statRequested.capitalize() + " stat for " + name.capitalize() + "...")
		statNameFound, stat = findPokemon.findStatfromNumber(number, statRequested)
		print(name.capitalize() + "'s " + statNameFound + " is " + str(stat) + ".")

else:
	if arg2.lower() == "gen":
		generation
		print(">>> In generation " + generation + ", " + name.capitalize() + " learns...")
		moveset = findPokemon.findMovesetFromGeneration(number, generation)
		moveset = findPokemon.findLevelupMoveset(moveset)
		
		#checking for longest name length
		lengthNameLongest = 0	
		for i in moveset:
			moveName = findPokemon.findMoveName(i[2])
			name = len(str(moveName))
			if name > lengthNameLongest:
				lengthNameLongest = name

		#print each move with the level
		for i in moveset:
			moveName = findPokemon.findMoveName(i[2])
			if len(moveName) < (lengthNameLongest/2+1):
				print(moveName + "\t" + "\t" + " level " + i[4])
			elif len(moveName) >= (lengthNameLongest):
				print(moveName + "\t" + " level " + i[4])
			else:
				print(moveName + "\t" + " level " + i[4])

	#else:
		#print("no generation specified")
		#mainDataPokemon = findPokemon.findDatafromNumber(number)
	

	


