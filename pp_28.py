# Max of Three

def max_num(num):
	try:

		current_high = 0
		for item in range(0,len(num)):
			num[item] = int(num[item])

		for num_check in range(0,len(num)-1):
			new_high = check_high_num(num[num_check], num[num_check+1])
			if new_high > current_high:
				current_high = check_high_num(num[num_check], num[num_check+1])

		print(current_high)

	except ValueError:
		pass

def check_high_num(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

num_list = []

for item in range(0,3):
	num_list.append(input("Give me a number:\n"))

max_num(num_list)