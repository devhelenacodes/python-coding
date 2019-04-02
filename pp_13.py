# Fibonnaci

def get_input():
	num = input("How many fibonnaci numbers would you like printed out?\n")

	try:
		num = int(num)
		if num > 0:
			fibonnaci(num)
		else:
			return []
	except ValueError:
		return []
		pass

def fibonnaci(num):
	fibonnaci_list = []

	for item in range(0, num):
		if item == 0 or item == 1:
			fibonnaci_list.append(1)
		elif item > 1: 
			new_val = fibonnaci_list[item-2] + fibonnaci_list[item-1]
			fibonnaci_list.append(new_val)

	print(fibonnaci_list)

get_input()