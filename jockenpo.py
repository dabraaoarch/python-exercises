import random
import os

options = ['rock', 'scissor', 'paper']
loses_to = {
	'rock' : 'paper',
	'scissor' : 'rock',
	'paper' : 'scissor'
}

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def check_choice(computer_choice, user_choice, scores):
	if loses_to[computer_choice] == user_choice:
		print("You won!")
		scores['wins'] += 1
	elif loses_to[user_choice] == computer_choice:
		print("You lost!")
		scores['losts'] += 1
	else:
		print("Tie")
	input("")
	return True
	
def printScores(scores):
	print("Wins: {} - Losts: {}".format(scores['wins'],scores['losts']))
def start():
	valid_choices = '0123'
	scores = {'wins':0, 'losts':0}
	while True:
		computer_choice = options[random.randint(0,len(options)-1)]
		printScores(scores)
		user_choice = input("[0]-Rock [1]-Scissor [2]-Paper [3]-Leave:")
		
		if len(user_choice) != 1 or valid_choices.find(user_choice) == -1 or user_choice == '3':
			return False
			
		verbal_user_choice = options[int(user_choice)]
		check_choice(computer_choice, verbal_user_choice, scores)
		
		clearScreen()
		
if __name__ == "__main__":
	start()
			
			