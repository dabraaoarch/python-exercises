import random
import os

matrix = "_" * 9
critical_patterns = {
	'*_*': ([0, 2, 3, 4, 6],[1, 6, 4, 2, 7]),
	'**_': ([0, 3, 6],[2,5,8]),
	'_**': ([0, 3, 6],[0,3,6]),
	'*_______*' : ([0],[4]),
	'*___*' : ([0, 2],[8, 4])
	}
	
win_patterns = {
	'***' : [0,3,6],
	'*_*_*' : [0,2]
}

def check_winner():
	global matrix
	without_computer_moves = matrix.replace("O","_",9)
	without_person_moves = matrix.replace("X","_",9)
	for key in win_patterns.keys():
		to_win = key.replace("*","O",9)
		to_lose = key.replace("*","X",9)  
		position_to_win = validate_pattern(to_win, win_patterns[key], without_person_moves)
		position_to_lose = validate_pattern(to_lose, win_patterns[key], without_compputer_moves)
		if position_to_win != False:
			return position_to_win
		position = position_to_lose or position
	return position
	

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def computer_choice():
	global matrix
	choice = check_obvious_choice(matrix)
	if choice == False:
		flag = True
		while flag:
			choice = random.randint(0,8)
			if matrix[choice] == "_":
				flag=False
	return choice

def check_obvious_choice(current_game):
	move = horizontal_patterns(current_game)
	if move != False:
		return move
	return vertical_patters(current_game)
	
def horizontal_patterns(current_game):
	if len(current_game) != 9:
		return False
	
	position = False
	for key in critical_patterns.keys():
		to_win = key.replace("*","O",2)
		to_lose = key.replace("*","X",2)  
		position_to_win = validate_pattern(to_win, critical_patterns[key], current_game)
		position_to_lose = validate_pattern(to_lose, critical_patterns[key], current_game)
		if position_to_win != False:
			return position_to_win
		position = position_to_lose or position
	return position

def validate_pattern(pattern, positions, current_game):
	position = current_game.find(pattern)
	if position == -1:
		return False
	if position in positions[0]:
		index = positions[0].index(position)
		return positions[1][index]

def transverse(current_game):
	if len(current_game) != 9:
		return False
	transversed = ""
	transversed_indexes = []
	for i in range(0,3):
		transversed += current_game[i] + current_game[i+3] + current_game[i+6]
		transversed_indexes += [i, i+3, i+6]
	return [transversed, transversed_indexes]
	
def vertical_patters(current_game):
	tranversion = transverse(current_game)		
	position = horizontal_patterns(transversion[0])
	if position != False:
		return transversion[1][position]
	return False

def drawScreen():
	global matrix
	print(len(matrix))
	print("{}|{}|{}\n".format(matrix[0],matrix[1],matrix[2]))
	print("{}|{}|{}\n".format(matrix[3],matrix[4],matrix[5]))
	print("{}|{}|{}\n".format(matrix[6],matrix[7],matrix[8]))

def apply_choice(position, value):
	global matrix
	if matrix[position] != "_":
		return False
	matrix = matrix[:position] + value + matrix[position+1:]
	return True
	
def read_user_choice():
	options = "0123456789"
	while True:
		user_choice = input("Enter a position [1-9] - [0]-quit:")
		if len(user_choice) == 1 and user_choice in options and user_choice != '0':
			if apply_choice(int(user_choice)-1,"X"):
				return True
		if user_choice == '0':
			return False

def start():
	while True:
		clearScreen()
		drawScreen()
		if not read_user_choice():
			return False
		computer = int(computer_choice())
		apply_choice(computer, "0")
		
if __name__ == "__main__":
	start()
		
		
		