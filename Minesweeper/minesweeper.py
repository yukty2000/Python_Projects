#  This is a bare-bone version of  minesweeper game
# selecting a cell we dig recursively until we reach each cell is next to a bomb - if cell selected has a bomb - Game over! 


# playing the game 

import random

r = [ 1, 1, 1,-1,-1,-1, 0, 0 ]
c = [-1, 0, 1,-1, 0, 1,-1, 1 ]

# to check if a row , column is valid in given dim_size board
def valid(row,column,dim_size):
	if row >= 0 and row < dim_size and column >= 0 and column < dim_size :
		return True
	return False

# To count number od unexpored/undug sites in minesweeper board
def count_undug(undug,dim_size) : 
	x = 0
	for i in range(dim_size) :
		 for j in range(dim_size) :
		 	if undug[i][j] == " ":
		 		x += 1

	return x


# recursive function to dig
def dig(undug , board , row , column , dim_size) :

	# dig till we reach a bomb
	if board[row][column] == -1 :
		return undug

	# if cell has already been dug
	if not (undug[row][column] == " ") :
		return undug

	# reveal number of adjacent bombs to user
	undug[row][column] = str(board[row][column])

	# if it is a cell numbered > 0 we dont dig it further
	if not (undug[row][column] == "0") :
		return undug 

	# recursively dig all adjacent cells(8)
	for k in range(8) :
		row_temp = row + r[k]
		column_temp = column + c[k]

		if(valid(row_temp,column_temp,dim_size)) :

			undug = dig(undug,board,row_temp,column_temp,dim_size)

	return undug


# to print the board
def print_board(undug,dim_size) :
	for row in undug :
		print('|'+'|'.join(row)+'|')


# play the game
def play(dim_size = 10 , num_bombs = 10) :

	# board is dim_size X dim_size
	# We have to plant num_bombs bombs on it

	# initialize board
	board = [[0 for i in range(dim_size)] for j in range(dim_size)]

	# plant bombs randomly
	for _ in range(num_bombs) :
		while (1) :

			row = random.randint(0,dim_size-1)
			column = random.randint(0,dim_size-1)

			if board[row][column] != -1:
				board[row][column] = -1
				break

	# initialise numbered cells
	for row in range(dim_size):
		for column in range(dim_size):
			if board[row][column] != -1 :
				ans = 0
				for k in range(8) :
					row_temp = row + r[k]
					column_temp = column +c[k]
					if(valid(row_temp,column_temp,dim_size)) :
						if(board[row_temp][column_temp] == -1):
							ans += 1

				board[row][column] = ans
		# print(board[row])



	# initialize board to show user
	undug = [[" " for i in range(dim_size)] for j in range(dim_size)]
	lose = False

	# play game
	while (count_undug(undug,dim_size) > num_bombs) and not lose :

		row = int(input(f"Enter row to dig(0-{dim_size-1})- "))
		column = int(input(f"Enter column to dig (0 - {dim_size-1}) - "))

		if not (undug[row][column] == " ") :
			print("Invalid input. Enter again!")
			continue

		if board[row][column] == -1 :
			lose = True
			undug[row][column] = "*"
			continue

		# We dig till we find bombs
		undug = dig(undug , board , row , column , dim_size)
		print_board(undug,dim_size)
		

	if lose :
		# print_board(undug,dim_size)
		print("SORRY! YOU LOST")	
	else :
		print("YOU WON")	


play()










