# Reading from File

def read_file(file):

	with open('file.txt', 'r') as open_file:
		all_text = open_file.read()