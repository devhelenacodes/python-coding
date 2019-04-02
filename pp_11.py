# Check Primality Functions

def get_integer():
	try:
		num = int(input("Give me a number:\n"))
		check_prime(num)
		return num
	except ValueError:
		pass

def check_prime(num):
	if num % 2 == 0:
		print("Number is divisible by 2.")
	elif num % 3 == 0:
		print("Number is divisible by 3.")
	elif num % 5 == 0:
		print("Number is divisible by 5.")
	elif num % 7 == 0:
		print("Number is divisible by 7.")
	else:
		print(num, "is a prime number!")


get_integer()