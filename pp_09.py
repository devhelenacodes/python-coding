# Guessing Game One

import random
guess = input("Guess a number between 1-9:\n")
count = 0
correct = 0

def guess(guess):
	

while guess != "exit":
	if count > 0:
		guess = input("Guess a number between 1-9:\n")

	try:
		guess = int(guess)
		rand_int = random.randint(1, 9)

		if guess == rand_int:
			print("You guessed it right!")
			correct += 1
		elif guess < rand_int:
			print("Too Low!")
		elif guess > rand_int:
			print("Too High!")
		count += 1
	except ValueError:
		print("You guessed", count, "times! And got it right", correct, "times!")


