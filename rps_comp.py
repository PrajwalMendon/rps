# enter your choice: 
# computer plays something random 
# to do this import randint (a module that lets us pick random numbers)
# shoot 
# player 1 // computer wins 
# make it case insensitive as well 

import random  # can say #from random import randint (then you can only say randint and not random.)

# we need these here in order to reference them in the loop
player_wins = 0 
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score: # this makes the game a best 2 out of 3
	print(f"Player Score: {player_wins}\tComputer Score: {computer_wins}")
	choice = input("Please choose rock, paper, or scissors: ")
	p1 = choice.lower()
	p2 = random.randint(0, 2)
	# 0 is rock, 1 is paper, 2 is scissors 
	if p1 == "quit" or p1 == "q": 
		break
	print("Shoot!")
	if p1 == "rock": 
		if p2 == 2:
			print("The computer chose: scissors")
			print("Player wins!")
			player_wins += 1
		elif p2 == 1:
			print("The computer chose: paper")		
			print("Computer wins!")
			computer_wins += 1
		elif p2 == 0: 	
			print("The computer chose: rock")
			print("The game is a tie!")
		else: 
			print("Something went wrong! Please chooose only rock, paper, or scissors")
	elif p1 == "scissors": 
		if p2 == 1:  
			print("The computer chose: paper")
			print("Player wins!")
			player_wins += 1
		elif p2 == 0: 
			print("The computer chose: rock")
			print("Computer wins!")
			computer_wins += 1
		elif p2 == 2: 	# this could be an else: 
			print("The computer chose: scissors")
			print("The game is a tie!")
		else: 
			print("Something went wrong! Please chooose only rock, paper, or scissors")
	elif p1 == "paper":
		if p2 == 0:  
			print("The computer chose: rock")
			print("Player wins!")
			player_wins += 1
		elif p2 == 2:  
			print("The computer chose: scissors")
			print("Computer wins!")
			computer_wins += 1
		elif p2 == 1: 
			print("The computer chose: paper")
			print("The game is a tie!")
		else: 
			print("Something went wrong! Please chooose only rock, paper, or scissors")
	else: 
		print("Something went wrong! Please chooose only rock, paper, or scissors")
print(f"FINAL SCORES... Player: {player_wins}\tComputer {computer_wins}")