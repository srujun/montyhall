import random

def main():
	cont = 1
	carscore = 0
	goatscore = 0

	swap = input("Swap? (y or n) ")
	
	while cont <= 100000:
		choice = random.randint(0, 2)
		prizes = ["", "", ""]

		prize = random.randint(0, 2)
		for i in range(3):
			if i == prize:
				prizes[i] = "Car"
			else:
				prizes[i] = "Goat"

		small_prize = random.randint(1, 2)
		if choice == 1 and small_prize == 1:
			small_prize = 0
		if choice == 2 and small_prize == 2:
			small_prize = 0

		if swap == "y":
			if choice == 0:
				if small_prize == 1:
					choice = 2
				else:
					choice = 1
			elif choice == 1:
				if small_prize == 0:
					choice = 2
				else:
					choice = 0
			else:
				if small_prize == 0:
					choice = 1
				else:
					choice = 0

		if prizes[choice] == "Car":
			carscore += 1
		else:
			goatscore += 1

		cont += 1

	winpercent = (carscore / 100000) * 100
	print("\nCar Score: {}\nGoat Score: {}\nWin Percent: {}".format(carscore, goatscore, winpercent))

if __name__ == '__main__':
	main()