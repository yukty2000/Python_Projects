# tic tac toe game between 2 players(human-computer)(human-human)(computer-computer) command line version
# This is an AI based model - where we have a genius computer model - based on the minimax algorithm

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


class GeniusComputerPlayer(Player) :
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):

		move = None
		print("Computer's move")
		if game.num_empty_squares() == 9 :
			move = random.choice(game.available_moves())
			return move
		else : 
			move = self.minimax(game, self.letter)

		return move['position']


	# Recursive function
	def minimax(self, state, player) :

		max_player = self.letter
		min_player = 'o' if max_player == 'x' else 'x'

		state.winner()

		# base case - our minimax value
		if state.current_winner == max_player :
			return { 'position' : None ,
						'score' : 1 * (state.num_empty_squares() + 1) 
					}

		elif state.current_winner == min_player :
			return { 'position' : None ,
						'score' : -1 * (state.num_empty_squares() + 1)
					}

		elif state.num_empty_squares() == 0 :
			return { 'position' : None , 
						'score' : 0
					}

		# Not base case 
		best = None
		if player == max_player:
			best = { 'position' : None , 'score' : -math.inf }
		else :
			best = { 'position' : None , 'score' : math.inf }

		for i in state.available_moves() :
			state.board[i] = player
			temp = self.minimax(state,'o' if player == 'x' else 'x')
			state.board[i] = ' '

			if player == max_player :		# maximum of all 
				if temp['score'] > best['score'] :
					best['score'] = temp['score']
					best['position'] = i

			else :   # minimum of all
				if temp['score'] < best['score'] :
					best['score'] = temp['score']
					best['position'] = i

		return best




