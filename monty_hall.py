import random

def main():
	count = 1
	carscore = 0
	goatscore = 0

	# Set swap for this set of runs
	swap = input("Swap? (y or n) ")
	# Set number of runs
	test_count = int(input("Enter number runs: "))
	
	while count <= test_count:
		# Set random choice
		choice = random.randint(0, 2)
		# Initialize doors list
		doors = ["", "", ""]

		# Set random door that has car prize
		car_prize_door = random.randint(0, 2)
		# Populate doors list
		for i in range(3):
			if i == car_prize_door:
				doors[i] = "Car"
			else:
				doors[i] = "Goat"

		# If player's chosen door has car inside
		if doors[choice] == "Car":
			# Set door that Monty Hall opens to either 1 or 2
			open_door = random.randint(1, 2)

			# Set open_door to 0 if the choice is the same as the random door
			# If they are not the same, the random door definitely has a "Goat"
			if choice == 1 and open_door == 1:
				open_door = 0
			if choice == 2 and open_door == 2:
				open_door = 0
		else:
			# Set open_door to the one that doesn't have "Car"
			# and is not the chosen door
			for i in range(3):
				if doors[i] != "Car" and i != choice:
					open_door = i

		# Swap if set to "y", else do nothing
		if swap == "y":
			if choice == 0:
				if open_door == 1:
					choice = 2
				else:
					choice = 1
			elif choice == 1:
				if open_door == 0:
					choice = 2
				else:
					choice = 0
			else:
				if open_door == 0:
					choice = 1
				else:
					choice = 0

		if doors[choice] == "Car":
			carscore += 1
		else:
			goatscore += 1

		count += 1

	winpercent = (carscore / test_count) * 100
	print("\nCar Score: {}\nGoat Score: {}\nWin Percent: {}".format(carscore, goatscore, winpercent))

if __name__ == '__main__':
	main()