# List Ends

# Own Solution
def set_array(orig_list = [5, 10, 15, 20, 25]):
	return orig_list

def get_first_last(array):
	new_list = []

	for item in array:
		if item == array[0]:
			new_list.append(item)
		elif item == array[len(array)-1]:
			new_list.append(item)

	print(new_list)


get_first_last(set_array())

# Learned Solution
def array_ends(orig_list = [5, 10, 15, 20, 25]):
	return [orig_list[0], orig_list[len(orig_list)-1]]

print(array_ends())