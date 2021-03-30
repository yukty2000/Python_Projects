# tic tac toe game between 2 players(human-computer)(human-human)(computer-computer) command line version
# This is not an AI based model where the computer will try to maximize it's chances of winning
# Choices are made randomly by the computer player

import math
import random

class Player :
	def __init__(self,letter) :
		# letter will be x or o
		self.letter = letter

	def get_move(self,game):
		pass

# We will build our human and computer players on top of this
class HumanPlayer(Player) :
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		# get a valid input from a human user
		moves = game.available_moves()
		move = None

		while(1) :
			move = int(input(f"Enter valid move. Player {self.letter} - "))
			# try except block
			try:
				move = int(move)  # Will raise an error if move is a letter 
				if move not in moves :
					raise ValueError
				break			# We break out of the loop if the above tests are successful

			except ValueError:
				print('Not valid move')

		return move


class ComputerPlayer(Player) :
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		# get random valid spot for the computer
		print("Computer's move")
		move = random.choice(game.available_moves())

		return move