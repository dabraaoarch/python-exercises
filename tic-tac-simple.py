import unittest
import random
import os

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def getNewGame():
	return "_"*9

def generateMove(game):
	empty_places = game.count("_")
	if empty_places == 0:
		return False
	moves = random.randint(1, empty_places)
	for index in range(0, len(game)):
		if game[index] == "_":
			moves-=1
		if moves == 0:
			return index
	
	return False
	
def getUserMove(game):
	while True:
		move = int(input("Enter a move [1-9] - [0]-quit:"))
		if move == 0:
			return False
		if move < 10 and move >= 0 and game[move-1] == "_":
			return move - 1

def drawGame(game):
	break_line = 1
	pipes = [1, 4, 7]
	lines = ""
	for index in range(0, len(game)):
		if index in pipes:		
			lines += "|" + game[index] + "|"
		else:
			lines += game[index]
		if break_line == 3:
			break_line = 0
			lines += "\n"
		break_line += 1
	print(lines)
	
def makeMove(game, move, user=True):
	type_of_move = "X" if user else "O"
	if move >= len(game) or move < 0:
		return False
	return game[:move] + type_of_move + game[move+1:]

def getLine(game, line):
	lines = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6]
	]
	if line >= len(lines) or line < 0:
		return False
	game_line = ""
	for item in lines[line]:
		game_line += game[item]
	return game_line
	
def checkWinner(game):
	user_move = "X"
	computer_move = "O"
	for i in range(0, 8):
		line = getLine(game=game,line=i)
		if line.count(user_move) == 3:
			return "user"
		if line.count(computer_move) == 3:
			return "computer"
	return False
	
def start():
	game = getNewGame()
	while True:
		drawGame(game)
		user_move = getUserMove(game=game)
		game = makeMove(game=game, move=user_move)
		computer_move = generateMove(game)
		game = makeMove(game=game, move=computer_move, user=False)
		winner = checkWinner(game=game)
		if winner != False :
			drawGame(game)
			print("{} won".format(winner))
			return True
		
		
class testTicTacGame(unittest.TestCase):
	def setUp(self):
		self.game=getNewGame()
		
	def test_generates_new_game(self):
		'''
		A new game must consist of 9 underscore
		'''
		empty_game="_"*9
		self.assertEqual(self.game, empty_game, 'The game starts with 9 empty spaces')
		
	def test_chose_a_move_all_empty_game(self):
		'''
		For more than one space left, an integer must be returned
		'''
		int_type=1
		position=generateMove(self.game)
		self.assertEqual(type(position), type(int_type), 'Must return an integer')
	
	def test_chose_a_move_last_space_left(self):
		'''
			When only one space left, the generateMove function must return the position
			of the space (first index: 0)
		'''
		end_empty_position = ("X" * 8) + "_"
		end_position = generateMove(end_empty_position)
		self.assertEqual(end_position, len(end_empty_position)-1, "Only the end space must be empty")
		
	def test_chose_a_fist_last_space_left(self):
		'''
			When only one space left, the generateMove function must return the position
			of the space (first index: 0)
		'''
		begin_empty_position = "_" + ("X" * 8)
		begin_position = generateMove(begin_empty_position)
		self.assertEqual(begin_position, 0, "Only the first space must be empty")
		
	def test_chose_a_move_no_space_left(self):
		'''
		If there are no space left, the function must return False
		'''
		full_game = "X" * 9
		position = generateMove(full_game)
		self.assertFalse(position)
	
if __name__ == "__main__":
	#unittest.main()
	start()
	
	