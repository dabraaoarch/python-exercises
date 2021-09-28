import os
import random

def clearScreen():
	os.system('cls' if os.name=="nt" else 'clear')

bankQuestion = ( 
	 {
		"Question" : "In what year was Brazil discovered?",
		"Options" : {
			"A" : "1988",
			"B" : "1500",
			"C" : "1930",
			"D" : "1718"
			},
		"Correct": "B"
		},
		{
		"Question" : "When the new brazilian constitution was declared?",
		"Options" : {
			"A" : "1988",
			"B" : "1934",
			"C" : "1918",
			"D" : "1900"
			},
		"Correct": "A"
		},
		{
		"Question" : "Hoje é segunda-feira, daqui a 61 dias será?",
		"Options" : {
			"A" : "Terça-feira",
			"B" : "Quinta-feira",
			"C" : "Sábado",
			"D" : "Domingo"	
			},
		"Correct": "C"
		},
		{
		"Question" : "Se uma girafa tem 2 olhos, um macaco tem 2 olhos e um elefante tem 2 olhos, quanto olhos nós temos?",
		"Options" : {
			"A" : "6",
			"B" : "2",
			"C" : "1",
			"D" : "4"
			},
		"Correct": "D"
		},
		{
		"Question" : "Se um determinado preço dobra, o lucro triplica: qual o percentual de lucro?",
		"Options" : {
			"A" : "100%",
			"B" : "200%",
			"C" : "300%",
			"D" : "400%"
			},
		"Correct": "A"
		},
		{
		"Question" : "Se 20% de a = b, então b% de 20 é o mesmo que?",
		"Options" : {
			"A" : "4% de a",
			"B" : "8% de a",
			"C" : "6% de a",
			"D" : "10% de a"
			},
		"Correct": "A"
		},
		{
		"Question" : "Qual o resultado para a equação: 5 + 3 x (15 - 3²)",
		"Options" : {
			"A" : "84",
			"B" : "32",
			"C" : "48",
			"D" : "23"
			},
		"Correct": "D"
		},
		{
		"Question" : "Quantos estados existem no Brasil incluindo o Distrito Federal?",
		"Options" : {
			"A" : "55",
			"B" : "30",
			"C" : "27",
			"D" : "25"
			},
		"Correct": "C"
		},
		{
		"Question" : "Qual destes paises não faz fronteira com o Brasil?",
		"Options" : {
			"A" : "Bolivia",
			"B" : "Chile",
			"C" : "Suriname",
			"D" : "Argentina"
			},
		"Correct": "B"
		},
		{
		"Question" : "Quantos estados possui a região sudeste",
		"Options" : {
			"A" : "3",
			"B" : "7",
			"C" : "4",
			"D" : "2"
			},
		"Correct": "C"
		}
)

def getQuestion(questions, questions_asked):
	while True:
		question = random.randint(0, len(questions)-1)
		if question not in questions_asked:
			return question
			
def askQuestion(question):
	clearScreen()
	print(question["Question"])
	for key in question["Options"].keys():
		print("{} - {}".format(key, question["Options"][key]))
	answer = input("Your answer [0]-Quit:")
	if answer == "0":
		return False
	return answer
	
def start():
	score = 0
	questions_asked = []
	for i in range(0, len(bankQuestion)):
		question = getQuestion(bankQuestion, questions_asked)
		answer = askQuestion(bankQuestion[question])
		if answer == False:
			return False
		if answer.upper() == bankQuestion[question]["Correct"]:
			score += 10	
		questions_asked += [question]
	
	print("Your score: {}".format(score))
		
if __name__ == "__main__":
	start()
	
	