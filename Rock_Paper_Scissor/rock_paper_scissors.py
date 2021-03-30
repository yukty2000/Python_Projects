# Rock paper scissor game of 5 rounds 

import random 

def play() :

	user_score = 0
	computer_score = 0

	plays = 5

	while plays > 0 :

		# Our user make a choice
		user_choice = input("Rock(R) Paper(P) Scissors(S) - ")

		# Our computer makes a choice
		computer_choice = random.choice(["R","P","S"])
		print(f"The computer chose {computer_choice} ")

		if user_choice == "R" and computer_choice == "S" :
			user_score += 1

		elif user_choice == "S" and computer_choice == "R" :
			computer_score += 1

		elif user_choice == "P" and computer_choice == "R" :
			user_score += 1

		elif user_choice == "R" and computer_choice == "P" :
			computer_score += 1

		elif user_choice == "S" and computer_choice == "P" :
			user_score += 1

		elif user_choice == "P" and computer_choice == "S" :
			computer_score += 1

		print(f"User's score = {user_score} , Computer's score = {computer_score} ")

		plays -= 1

	if user_score > computer_score :
		print("Congrats! You won")

	elif computer_score > user_score :
		print("Sorry! Computer won")

	else :
		print("It's a tie")



play()



