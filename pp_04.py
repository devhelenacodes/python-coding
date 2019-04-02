#Divisors

num = input("Enter a number:\n")

try:
	num = int(num)
	count = range(2, 11)

	for item in count:
		divisorList.append(num*item)

	print(divisorList)
except ValueError:
	pass