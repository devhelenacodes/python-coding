# List Overlap

import random

a = []
b = []
common = []

for item in range(random.randint(10,30)):
	a.append(random.randint(1,50))

for item in range(random.randint(10,30)):
	b.append(random.randint(1,50))

for item in a:
	for item in b:
		if item in common:
			pass
		else:
			common.append(item)

print(common)