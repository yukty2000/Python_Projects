# This program solves a valid sudoku puzzle using backtracking

# Our puzzle is a 9X9 - we will use 9 lists and -1 to indicate empty space

def next_empty_space(puzzle) :

	for i,row in enumerate(puzzle) :
		for j,el in enumerate(row) :
			if el == -1 :
				return i,j

	return -1,-1

def valid_state(puzzle) :
	# no doubles in any row or column or block

	for row in puzzle : 
		temp = set()
		for el in row : 
			if el in temp and el != -1:
				return False

			temp.add(el)

	# check columns
	for column in range(9) : 
		temp = set()
		for row in range(9) :
			el = puzzle[row][column]
			if el in temp and el != -1:
				return False

			temp.add(el)

	# check eack block
	for i in range(0,9,3):
		temp = set()
		v = 0
		while (v < 9) :
			temp = set()
			for j in range(i,i+3):
				for k in range(v,v+3):
					el = puzzle[k][j]
					if el in temp and el != -1:
						return False

					temp.add(el)

			v += 3

	return True


def solve(puzzle) :
	# We start by finding a valid empty cell 
	row, column = next_empty_space(puzzle)

	# if no empty space is found our puzzle has been solved
	if row == -1 and column == -1 :
		return True , puzzle

	temp = None
	valid = False
	for i in range(1,10) :
		
		puzzle[row][column] = i

		# Check if the changes we made are valid 
		val = valid_state(puzzle)
		if not val :
			puzzle[row][column] = -1
		else :

			# solve the next empty cell
			valid, temp = solve(puzzle)
			if valid == True :
				break
			else :
				puzzle[row][column] = -1

	if not valid :
		return valid, puzzle
	else :
		return valid , temp


# puzzle = []
# for i in range(1,10):
# 	print(f"Enter elements in row {i} - ")
# 	row = []
# 	for j in range(9) :
# 		el = int(input("Enter between 1-9"))
# 		row.append(el)

# 	puzzle.append(row)

# _ , puzzle = solve(puzzle)

# for row in puzzle :
# 	print(row)

puzzle = [[-1,5,1,-1,-1,6,4,-1,-1],
			[-1,2,9,-1,-1,5,-1,-1,-1],
			[-1,-1,-1,-1,-1,4,-1,-1,3],
			[-1,6,-1,-1,2,-1,8,-1,-1],
			[-1,9,-1,-1,-1,-1,-1,3,-1],
			[-1,-1,7,-1,3,-1,-1,2,-1],
			[2,-1,-1,8,-1,-1,-1,-1,-1],
			[-1,-1,-1,9,-1,-1,2,8,-1],
			[-1,-1,8,5,-1,-1,7,4,-1]]


valid , puzzle = solve(puzzle)

# if given puzzle was valid or not
print(valid)

# Print the answer
for row in puzzle :
	print(row)