# In this game we build a guessing game such that the computer guesses a number and we provide 
# it feedback of whether the guess is too high or low ( the number is our choice)


import random

def guess(x):
	low = 1
	high = x
	while (1 and low != high) :			# if low == high randint() will throw an error

		# Computer tries to guess our number
		guess_number = random.randint(low,high)

		# Computer asks for feedback
		output = input(f'Is {guess_number} too high(H) or too low(L) or correct(C) - ')

		if output == "H" :
			high = guess_number - 1

		elif output =="L" :
			low = guess_number + 1

		else :
			print(f"Computer has guessed {guess_number} correctly! Game ends")
			break;

	if low == high:
		print(f"The answer is {low}. Ran out of choices!")


x = int(input('Enter upper boundary - '))
guess(x)

