# Odd or Even
num = input("Enter a number and I'll guess if it's even or odd:\n")
check = input("Enter a number and I'll check the divisibility of the first number:\n")

try:
	num = int(num)
	check = int(check)

	if num % 4 == 0:
		print("It's a multiple of 4!")
	elif num % 2 == 0:
		print("It's even!")
	else:
		print("It's odd!")

	if num % check > 0:
		print(num, "is not divisible by", check)
	else:
		print(num, "is divisible by", check)

except ValueError:
	pass