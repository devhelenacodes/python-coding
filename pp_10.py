# List Overlap Comprehensions

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(100), 11)
b = random.sample(range(100), 8)
overlap = [item1 for item1 in a for item2 in b if item1 == item2]

print(overlap)