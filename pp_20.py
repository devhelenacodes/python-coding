# Element/Binary Search

# Own Solution
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

def find_item(orig_list, item_to_find):
	if item_to_find in orig_list:
		new_list.append(item_to_find)
		print(item_to_find, "found!")
	else:
		print(item_to_find, "not found!")

find_item(orig_list, 5)

# Learned Solution
def find(ordered_list, item_to_find):
	start_index = 1
	end_index = len(ordered_list) - 1
	search = True

	while search:
		middle_index = int((end_index - start_index) / 2)

		if middle_index < start_index or middle_index > end_index or middle_index < 0:
			search = False
			return False

		middle_element = ordered_list[middle_index]
		if middle_element == item_to_find:
			print(item_to_find, "found!")
			search = False
			return True
		elif middle_element < item_to_find:
			end_index = middle_index
		else:
			start_index = middle_index

if __name__=="__main__":
 	orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 	print(find(orig_list,5))
 	print(find(orig_list,9))
 	print(find(orig_list,2))