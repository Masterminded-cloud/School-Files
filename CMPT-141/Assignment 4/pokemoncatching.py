print("Time to catch some Pokemon!")
print("---")
# Pokemon catching phase
caught = input("Which Pokemon have you caught? ")
pokeList = [caught]
add = input("Would you like to keep catching Pokemon (y/n)? ")

while add == 'y':
	print("So far you've caught: ")
	print(pokeList)
	caught = input("Which new Pokemon have you caught? ")
	pokeList.append(caught)
	add = input("Would you like to keep catching Pokemon (y/n)? ")

print("---")
print("Time to head to the Pokemon Gym!")
print("---")
# gym batle phase
team = []
while len(pokeList) > 0 and len(team) < 6:
	print("Pokemon in your collection: ")
	print(pokeList)
	print("Pokemon on your Gym Team: ")
	print(team)
	on_team = input("What Pokemon will you add to your team? ")
	pokeList.remove(on_team)
	team.append(on_team)
	print("I CHOOSE YOU,", on_team.upper()+"!!")

print("---")
print("Your Pokemon team is ready to hit the gym!")
