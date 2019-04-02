# List Remove Duplicates

names = ["Klarisse", "Hector", "Klarisse", "Mary", "Daniel", "Mary", "Klarisse", "John", "John"]

def get_list(list_names):

	common_list = []

	for item in list_names:
		if item not in common_list:
			common_list.append(item)

	return common_list

def get_set(set_names):
	
	return set(set_names)

print(get_list(names))
print(get_set(names))