import sys
import findPokemon
print("")
print("")
print("")
print("******************************************************************")
print("*** Hello!  I'm Dexter!  I can answer your Pokémon questions!  ***")
print("")
print("                                                                  ")
print("  /EEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\                                ")
print("  |EEF````TER( )( )( )EEEEEEEEEEE|                                ")          
print("  |EF  *   EEEEEEEEEEEEEEEEEEEEEE|___________                     ")                                      
print("  |EL      EEEEEEE%%%%%%%%%%%%|__|%%%%%%%%%%%\                    ")
print("  |EEbcccJEEEEEE%%%EEEEEEEEEE%|__|%EEEEEEEEEE%\                   ")
print("  |EEEEEEEEEEE%%%EEEEEEEEEEEE%|__|%EEEEEEEEEEE%\_____________     ")
print("  ||%%%%%%%%%%%EEEEEEEEEEEEEE%|__|%EEEEEEEEEEEEEEEEEEEEEEEEE|\    ")
print("  ||D----------------------EE%|__|%EE---------------------EE||    ")
print("  ||E|  ______o__o______  |EE%|__|%ER|        Hi!        |EE||    ")
print("  ||X|  |               | |EE%|__|%ED|                   |EE||    ")
print("  ||T|  |               | |EE%|__|%EE|        I'm        |EE||    ")
print("  ||E|  |               | |EE%|__|%EE|    D e x t e r    |EE||    ")
print("  ||R|  |               | |EE%|__|%EE---------------------EE||    ")
print("  ||D|  |               | |EE%|__|%EE|---+---+---+---+---|EE||    ")
print("  ||E|  |               | |EE%|__|%EE|___|___|___|___|___|EE||    ")
print("  ||X|  |_______________| |EE%|__|%EE|   |   |   |   |   |EE||    ")
print("  ||T|                    |EE%|__|%EE|___|___|___|___|___|EE||    ")
print("  ||Ee\___________________|EE%|__|%EEE EE EEEEE====EE====EEE||    ")
print("  ||EEEEEEEEEEEEEEEEEEEEEEEEE%|__|%EE.-------.EEEEEEEEEEEEEE||    ")
print("  ||EY  YE-----E-----EEEEEEEE%|__|%EE|   |   |EEEEEEY *  TEE||    ")
print("  ||EL  JEEEEEEEEEEEEEE| |EEE%|__|%EE+---+---+EEEEEEEL  JEEE||    ")
print("  ||EEEEEE+--------++--+ +--+||__|%EEEEEEEEEEEEEEEEEEEEEEEEE||    ")
print("  ||E^E^EE|        |+--+ +--+||__|%EE+--------+E+--------+EE||    ")
print("  ||EEEEEE|________|EEE|_|EEE%|__|%EE|________|E|__v_0.1_|EE||    ")
print("  ||EEEEEEEEEEEEEEEEEEO...EEE%|__|%EEEEEEEEEEEEEEEEEEEEEEEEE||    ")
print("  \%%%%%%%%%%%%%%%%%%%%%%%%%%%|__|%%%%%%%%%%%%%%%%%%%%%%%%%%%/    ")
print("                                                                  ")

#### BEGIN USER CONTROL

#killCommand = False
#while killCommand == False:

# restart = 1
# while restart == 1:
arg1 = input("Enter a Pokémon name or national dex number. >>> ")
if arg1 == "":
	exit()

### Determine if first input (arg1) is number or name
### Assign number and name values

isDexNumber = findPokemon.detectNumber(arg1)
if isDexNumber == True:
	number = int(arg1)
	name = findPokemon.findNamefromNumber(number)
elif isDexNumber == False:
	name = str(arg1)
	number = findPokemon.findNumberfromName(name)
	number = int(number)

print("What would you like to know?")
print("1. Name/Number")
print("2. Moveset")
print("3. Stats")
print("4. Test Feature")
request = input(">>> ")
if request == "":
	exit()

### Process Type of Request 
## Request is Name/Number

if request == "1":
	if isDexNumber == True:
		print("Pokémon #" + str(number) + " is " + name + ".")
	elif isDexNumber == False:
		print(name.capitalize() + "'s number is " + str(number) + ".")

## Request is Moveset

elif request == "2":
	print("1.  Red & Blue")
	print("2.  Yellow")
	print("3.  Gold & Silver")
	print("4.  Crystal")
	print("5.  Ruby & Sapphire")
	print("6.  Emerald")
	print("7.  FireRed & LeafGreen")
	print("8.  Diamond & Pearl")
	print("9.  Platinum")
	print("10. HeartGold & SoulSilver")
	print("11. Black & White")
	print("12. Colosseum")
	print("13. Pokémon XD")
	print("14. Black 2 & White 2")
	print("15. X & Y")
	print("16. OmegaRuby & AlphaSapphire")
	print("17. Sun & Moon")
	print("18. UltraSun & UltraMoon")

	quit = False	
	while quit == False:
		generation = input("Enter a game. >>> ")
		if generation == "":
			exit()
		elif generation.isdigit() == True:
			if (int(generation) > 0) & (int(generation) <= 16):
				findPokemon.findMovesetForGeneration(generation, number, name)
				quit = True
			else:
				print("Not an appropriate number.")
		else: 
			print("Not an appropriate number.")

## Request is Stats

elif request == "3":
	findPokemon.findStats(number, name)

## Request is Test Feature

elif request == "4":
	findPokemon.findStats(number, name)	

else: 
	exit()

print("******************************************************************")