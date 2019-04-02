# Reverse Word Order

def get_user_string():
	return input("Type in a sentence:\n")

def reverse_string(sentence):
	string = sentence.split(" ")
	reverse = []
	for item in range(0, len(string)):
		reverse.append(string[len(string)-1-item])
		
	return " ".join(reverse)

def reverse_string_simple(sentence):
	
	string = sentence.split(" ")	
	return " ".join(string[::-1])

print(reverse_string(get_user_string()))
print(reverse_string_simple(get_user_string()))