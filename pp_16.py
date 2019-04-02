# Password Generator

import random
import string
import sys

def mix_list():
	return "".join(random.choice(string.ascii_letters + string.digits) for x in range(8))

def special_list():
	return "".join(random.choice("?!&$*%@") for x in range(2))

def feedback():
	answer = input("Are you happy with this password? (Y/N):\n")

	if answer.upper() == "Y":
		sys.exit
	elif answer.upper() == "N":
		main()
	else:
		print("Invalid Input")
		sys.exit()

def main():

	list_keys = mix_list()
	specials = special_list()

	password = set()
	password.add(list_keys)
	password.add(specials)

	difficulty = input("Would you like a weak or strong password?:\n")

	if difficulty.lower() == "weak":
		password = list(password)
		text = "".join(random.sample(password, len(password[0:4])))
		print(text)

		feedback()
	elif difficulty.lower() == "strong":
		text = "".join(random.sample(password, len(password)))
		print(text)

		feedback()
	else:
		print("Invalid Input")
		sys.exit()

main()