# File Overlap

def read_file():
	list_happy_num = []
	list_prime_num = []
	list_common_num = []

	with open('happynumbers.txt', 'r') as open_file:
		for line in open_file:
			try:
				line = int(line)
				list_happy_num.append(line)
			except ValueError:
				pass

	with open('primenumbers.txt', 'r') as open_file:
		for line in open_file:
			try:
				line = int(line)
				list_prime_num.append(line)
			except ValueError:
				pass

	for item1 in list_happy_num:
		if item in list_prime_num:
			list_common_num.append(item)

	print(list_common_num)


read_file()