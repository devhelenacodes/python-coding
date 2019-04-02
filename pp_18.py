# Cows and Bulls

import random
import sys

def get_digits():
	user_num = input("Give me a four-digit number:\n")

	try:
		user_num = int(user_num)

		if user_num > 999 and user_num < 10000:
			return check_digit(user_num, rand_num)
	except ValueError:
		pass

def check_digit(user_num, rand_num):
	user_num = str(user_num)
	rand_num = str(rand_num)
	count_cow = 0
	count_bull = 0

	for item in range(0, 4):
		if user_num[int(item)] == rand_num[int(item)]:
			count_cow += 1

		else:
			count_bull += 1

	print(count_cow, "cows,", count_bull, "bulls")

	return count_cow
	

if __name__=="__main__":
	playing = True
	count_guess = 0
	rand_num = str(random.randint(1000, 9999))

	while playing:
		get_digits()
		count_guess += 1
		if get_digits() == 4:
			print("Awesome! You guessed the number! You won after", count_guess, "guesses.")
			sys.exit()