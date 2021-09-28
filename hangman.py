import random
import os


words = {
	'broke' : ['Into pieces','Said about someone with no money','State of something fragile after falling on the ground'],
	'train' : ['Type of vehicle that runs on rails','Mass transportation system','Can be used to carry cargo'],
	'brain' : ['Human organ','Where the thoughts come from','Humans are known for have the most evolved one'],
	'building' : ['Kind of construction','Place where many companies do their activities','Big citties are full of'],
	'fruits' : ['Healthy kind of food','Apples and oranges belongs to this group','One famous way for trees to spread their seeds'],
	'barricade' : ['Commonly used to protect soldiers','Made of sand bags','Needs to be massive to be effective'],
	'travel' : ['People like to do that on vacations','The act to visit another city, state os country','Executives do this a lot'],
	'marble' : ['A kind of rock','Commonly used as a building material','Many sculptures are made out of this material'],
	'fail' : ['Is said about a system that can`t accomplish a task','When a student can`t achieve a minimun score at an exam','When a machine don`t work'],
	'snail' : ['Carry his own house','Moves very slowly','Commonly found in gardens'],
	'pipe' : ['Used to delivery water trhu a house or building','Long and circular plastic tube','Is also the name for an object use to smoke tabaco '],
	'trouble' : ['Problem','When things goes very wrong','Dificult to solve a situation'],
	'bankruptcy' : ['When a person or company can`t pay his debts','Usualy impose by a court order','A legal process used to resolve debts problems']
}

hangman = ["_O_\n/|\\\n | \n/ \\"]
hangman += ["\n/|\\\n | \n/ \\"]
hangman += ["\n |\\\n | \n/ \\"]
hangman += ["\n  \\\n | \n/ \\"]
hangman += ["\n   \n | \n/ \\"]
hangman += ["\n   \n   \n/ \\"]
hangman += ["\n   \n   \n  \\"]
hangman += ["\n   \n   \n   "]

def getWord():
	num = random.randint(0, len(words)-1)
	i = 0
	for key in words:
		if num == i:
			return key
		i = i + 1		
	return False
	
def readKeys():
	letters = "abcdefghijklmnopqrstuvwxyz1"
	while True:
		key = input('Enter a letter [0]-exit [1]-tip : ')
		if key == "0":
			return False
			
		if len(key) == 1 and letters.find(key.lower()) != -1:
			return key
		return " "
		
def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def drawScreen(word, keys, tries):
	clearScreen()

	if tries > 0:
		print("\n\n")
		spaces = ""
		for letter in word:
			if letter in keys:
			   spaces += letter + " "
			else:
				spaces += "_ "
		
		if spaces.find("_") == -1:
			print("You won!")
			return True				
			
		print(spaces)
		print("\n You have {} tries left. letters you tries{}".format(tries, keys))
	else:
		print("You lost, the word was {}".format(word))
	print(hangman[tries])
	return False
	
'''def mapWord(word):
	mapped_word = {}
	for i in range(0,len(word)):
		if word[i] in mapped_word.keys():
			mapped_word[word[i]] += [i]
		else:
			mapped_word[word[i]] = [i]
	return mapped_word
'''
def start():
	word = getWord()
	keys = []
	tries = 7
	won = False
	if word != False:
		drawScreen(word, keys, tries)
		while not won and tries > 0:
			key = readKeys()
			if key == False:
				return False
			if key == '1':
				print("Tip: {}".format(words[word][random.randint(0,2)]))
			else:
				keys = keys + [key]
				if word.find(key.lower()) == -1:
					tries = tries - 1
				won = drawScreen(word, keys, tries)
					
			
if __name__ == "__main__":
	start()
	