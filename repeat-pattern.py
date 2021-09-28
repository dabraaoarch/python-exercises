import os
def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def readPattern():
	pattern = input("Inform the pattern you wanto to repeat [0]-Quit: ")
	return pattern if pattern != "0" else False
	
def readRepetition():
	try:
		repetitions = int(input("Inform the number of times you want it to repeat [0]-Quit: "))
		return repetitions if repetitions != 0 else False
	except ValueError:
		print("Must be an integer")
		return readRepetition()
	return repetitions
	
def loopPattern(pattern, number_of_times=0):
	if number_of_times == 0:
		print(pattern)
	position = 0
	adding_pattern = ""
	for i in range(0,number_of_times):
		if position == len(pattern):
			position = 0
		adding_pattern += pattern[position]
		print(adding_pattern)
		position += 1
		
def start():
	pattern = readPattern()
	if pattern == False:
		return False
	if pattern == "":
		pattern = "".join(["{}".format(x) for x in range(0,10)])
	number_of_times = readRepetition()
	if number_of_times == False:
		return False
	clearScreen()
	loopPattern(pattern=pattern, number_of_times=number_of_times)
	
if __name__=="__main__":
	start()