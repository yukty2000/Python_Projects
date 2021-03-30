# In this game our computer generates a random number in a specified range and theuser tries to guess it
# The computer provides output such as - Too high , Too low , Correct , etc.(if applicable)

import random

def guess(x):

	# To get a random number 1<=N<=x
	random_number = random.randint(1,x)

	# We need to make guesses until we guess correctly
	while (1) :
		guess_number = int(input(f'Make a guess between 1 and {x}- '))

		if guess_number > random_number :
			print('Too high')

		elif guess_number < random_number : 
			print('Too low')

		else :
			print('Spot on! Your guess is correct')
			break


x = int(input('Enter upper border - '))

guess(x)
