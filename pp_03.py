#List Less than Ten

max_val = input("Type a random number not more than 89:\n")
a  = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
y = []

for item in a:
	if item < 10:
		x.append(item)

print(x)

try:
	max_val = int(max_val)

	for item in a:
		if item < max_val:
			y.append(item)

	print(y)

except ValueError:
	pass
