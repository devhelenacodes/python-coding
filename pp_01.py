# Character Input
name = input("What is your name?:\n")
age = input("What is your age?:\n")
rep = input("How many times would you like to print the message?:\n")

try:
	age = int(age)
	rep = int(rep)
	
	if age > 0 :
		for num in range(rep):
			print(name, "will turn 100 years old in " + str(100-age+2019) + ".")

except ValueError:
	pass

