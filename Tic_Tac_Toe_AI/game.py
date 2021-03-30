
# Interesting list comprehensions here

import tic_tac_toe
import time

class TicTacToe:
	# We need a board
	def __init__(self):
		self.board = [' ' for _ in range(9)]   # single list to represent a 3x3 board
		self.current_winner = None

	# We need to be able to print the board
	def printboard(self) :
		for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
			print('|'+'|'.join(row)+'|')


	@staticmethod			# because we are not accessing the cls or self
	def print_board_nums() :

		# tells us which number corresponds to which box

		number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]	# this comprehension helps in splitting indifferent rows
		for row in number_board :
			print('|'+'|'.join(row)+'|')


	def available_moves(self) :
		# returns all empty boxes 
		moves = [i for i,spot in enumerate(self.board) if spot == ' ']
		return moves

	# if empty squares are there
	def empty_squares(self) :
		return ' ' in self.board

	# number of empty squares
	def num_empty_squares(self) :
		return self.board.count(' ')

	def winner(self) :
		

		# Check all rows for winner
		for row in [self.board[i*3:(i+1)*3] for i in range(3)] :
			el = row[0]
			if el == ' ' : 
				continue
			x = 1
			for j in row[1:] :
				if j == el :
					x += 1
			if x == 3 : 
				self.current_winner = el
				return

		# check winner in all columns
		for column in [self.board[i : : 3] for i in range(3)] :
			el = column[0]
			if el == ' ' : 
				continue
			x = 1
			for j in column[1:] :
				if j == el :
					x += 1
			if x == 3 : 
				self.current_winner = el
				return 

		# check both diagonals
		el = self.board[0]
		x = 0
		for i in self.board[0::4] :
			if i == el :
				x += 1

		if x == 3 and el != ' ':
			self.current_winner = el
			return

		el = self.board[2]
		x = 0
		for i in self.board[2:7:2] :
			if i == el :
				x += 1

		if x == 3 and el != ' ':
			self.current_winner = el
			return

		self.current_winner = None






def play(game, x_player, o_player, print_game = True ):
	if print_game : 
		game.print_board_nums()

	letter = 'x'
	while (game.empty_squares() and game.current_winner == None) :

		time.sleep(2)
		# it is x_player's turn
		if letter == 'x' :
			move = x_player.get_move(game)

			game.board[move] = 'x'

		else :

			move = o_player.get_move(game)

			game.board[move] = 'o'

		# Alternate turns 
		if letter == 'x' :
			letter = 'o'

		else :
			letter = 'x'

		game.printboard()
		game.winner()

	if game.current_winner == None :
		print('Its a tie')

	else : 
		print(f"Winner - {game.current_winner}")


# Playing the game

x = input(" Player x - Human(H) or Computer(C) ")
x_player = None
if x == "H" :
	x_player = tic_tac_toe.HumanPlayer('x')

else : 
	x_player = tic_tac_toe.GeniusComputerPlayer('x')

o = input(" Player o - Human(H) or Computer(C) ")
o_player = None
if o == "H" :
	o_player = tic_tac_toe.HumanPlayer('o')

else : 
	o_player = tic_tac_toe.GeniusComputerPlayer('o')

game = TicTacToe()

play(game, x_player, o_player)










