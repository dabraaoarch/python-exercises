def getNewGame():
	return [["","",""],["","",""],["","",""]]
	
def checkLines(line, to_win=True):
	search_pattern = "O" if to_win else "X"
	
	if line.count(search_pattern) > 1 and line.count("") > 0:
		return line.index("")
	
	return False
		
def checkEndGame(line):
	if line.count("O") == 3 or line.count("X") == 3:
		return True
	return False
	
def getVerticalLine(game, collumn):
	if collumn > len(game) or collumn < 0 or len(game[collumn]) != len(game):
		return False
		
	return_array = []
	positions = []
	for index in range(0, collumn):
		return_array.append(game[index][collumn])
		positions.append((index,collumn))
	return {"line": return_array, "positions": positions}
	
def getDiagonalLine(game, left=True):
	y_size = len(game)
	x_size = len(game[y_size-1])
	if x_size != y_size:
		return False
	return_array = []
	positions = []
	for index in range(0, y_size):
		if left:
			return_array.append(game[index][index])
			positions.append((index, index))
		else:
			return_array.append(game[index][x_size-index-1])
			positions.append((index, x_size-index-1))
	return {"array" : return_array, "positions": positions}

def checkDiagonalLines(game):
	diagonals = [getDiagonalLine(game), getDiagonalLine(game, left=False)]
	for line in diagonals:
		position = checkLines(line["array"]) or checkLines(line["array"], to_win=False)
		if position != False:
			return line["positions"][position]
	return False

def checkHorizontalLines(game):
	for index in range(0, len(game)):
		position = checkLines(game[index]) or checkLines(game[index], to_win=False)
		if position != False:
			return position
	return False
	
def checkVerticalLines(game):
	y_size = len(game)
	x_size = len(game[y_size-1])
	if y_size <= 0 or y_size != x_size:
		return False
	for index in range(0, x_size-1):
		vertical_line = getVerticalLine(game, index)
		position = checkLines(vertfical_line['array']) or checkLines(vertfical_line['array'], to_win=False)
		if position != False:
			return vertical_line['positions'][position]
	return False


if __name__ == "__main__":
	game = getNewGame()
	game[0][2] = "X"
	game[1][1] = "X"
	game[2][0] = ""
	print(checkDiagonal(game))
