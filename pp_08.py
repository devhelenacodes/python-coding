# Rock Paper Scissors

import sys

p1 = input("Player 1: Rock Paper Scissors?:\n")
p2 = input("Player 2: Rock Paper Scissors?:\n")

if p1 == p2:
	print("It's a draw")
if p1 == "rock":
	if p2 == "scissors":
		print("Player 1 Wins!")
	elif p2 == "paper":
		print("Player 2 Wins!")
elif p1 == "scissors":
	if p2 == "paper":
		print("Player 1 Wins!")
	elif p2 == "rock":
		print("Player 2 Wins!")
elif p1 == "paper":
	if p2 == "rock":
		print("Player 1 Wins!")
	elif p2 == "scissors":
		print("Player 2 Wins!")
else:
	print("Invalid Input!")
	sys.exit()
