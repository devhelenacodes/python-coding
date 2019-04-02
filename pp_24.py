# Draw a Game Board

def board_size():
	user_input = input("What size game board you want to draw?")

	try:
		user_input = int(user_input)
	except ValueError
		pass

# Own Solution
def create_board(size):
	size = 3
	top = " ---"
	side = "|   "
	box = ""

	for item in range(0, size):
		for item in range(0, size):
			box += top

			if item == size-1:
				box += "\n"
		
		for item in range(0, size):
			box += side

			if item == size-1:
				box += side
				box += "\n"
				
	for item in range(0, size):
		box += top

	print(box)

# Learned Solution
def learned_create_board(size):
	size = 3
	top = " ---" * size
	side = "|   " * (size + 1)

	for index in range(size):
		print(top)
		print(side)
	print(top)