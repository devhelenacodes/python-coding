# File Overlap

# TODO: Finish this exercise

def read_file(file):

	with open('happynumbers.txt', 'r') as open_file:
		line = open_file.readline()
		test_list = []
		while line:
			test_list.append(line)
		print(test_list)


	with open('primenumbers.txt', 'r') as open_file:
		all_text = open_file.read()


with open('happynumbers.txt', 'r') as open_file:
	line = open_file.readline()
	test_list = []
	while line:
		test_list.append(line)
	print(test_list)