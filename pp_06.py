# String Lists

# Own Answer
string = input("Give me a word:\n")
start_count = 0
end_count = len(string) - 1

for letter in string:
	if string[start_count] == string[end_count]:
		start_count += 1
		end_count -= 1
		result = "This is a palindrome"
	else:
		result = "This is not a palindrome"


print(result)


# Learned def reverse, more effective way
def reverse(word):
	x = ''
	for position in range(len(word)):
		x += word[len(word)-1-position]
	return x

word = input('Give me a word:\n')
wordReversed = reverse(word)

if wordReversed == word:
	print('This is a palindrome')
else:
	print('This is not a palindrome')
