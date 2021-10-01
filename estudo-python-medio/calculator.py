import tkinter as tk

class Calculator():
	'''
		Do the matemathical operations for the interface
	'''
	def __init__(self):
		self.aOperations = {
			'+' : lambda x,y: x + y,
			'-' : lambda x,y: x - y,
			'*' : lambda x,y: x * y,
			'/' : lambda x,y: x / y,
			'^' : lambda x,y: x ** y,
			'r' : lambda x,y: x ** (1/y)
		}
		self.aValidCharacters = ["{}".format(x) for x in range(0,10)]
		self.aValidCharacters += ["."]
		self.aOperandStack = []
		self.aOperatorStack = [] 
		self.sTemporaryNumber = ''
	
	def doOperation(self, sOperator=None, fOperand1=None, fOperand2=None):
		'''
			Given to valid (float) operands, do the operation between them
		'''
		if sOperator == None and sOperator in self.aOperations.keys():
			return None
		if type(fOperand1) != float or type(fOperand2) != float:
			return False
		return self.aOperations[sOperator](fOperand1, fOperand2)

	def addOperandToStack(self):
		if self.sTemporaryNumber == '':
			return False
		for sLetter in self.sTemporaryNumber:
			if not sLetter in self.aValidCharacters:
				return False
		try:
			self.aOperandStack  += [float(self.sTemporaryNumber)]
		except:
			self.aOperandStack  = [float(self.sTemporaryNumber)]
		self.sTemporaryNumber = ''
		print(self.aOperandStack)
		return self.sTemporaryNumber
		
	def addToTemporaryOperand(self, sKeyPressed):
		if not sKeyPressed in self.aValidCharacters:
			return False
		self.sTemporaryNumber += "{}".format(sKeyPressed)
		return self.sTemporaryNumber
		
	def addOperatorToStack(self, sKeyPressed):
		if not sKeyPressed in self.aOperations.keys():
			return False
		try:
			self.aOperatorStack += [sKeyPressed]
		except:
			self.aOperatorStack = [sKeyPressed]
		return self.aOperatorStack[-1]

	def clearTemporaryNumber(self):
		self.sTemporaryNumber = ""
		return self.sTemporaryNumber
		
	def clearAll(self):
		self.aOperatorStack = []
		self.aOperandStack =[]
		return self.clearTemporaryNumber()

	def getResult(self):
		iLengthStackOperator = len(self.aOperatorStack)
		iLengthStackOperand = len(self.aOperandStack) 
		if iLengthStackOperator < 1 or iLengthStackOperand < 2:
			return False
		if iLengthStackOperand % 2 != 0 or iLengthStackOperand - 1 != iLengthStackOperator:
			return False
		for sOperator in self.aOperatorStack:
			fOperand2 = self.aOperandStack.pop()
			fOperand1 = self.aOperandStack.pop()
			fResultado = self.doOperation(
				sOperator = sOperator,
				fOperand1 = fOperand1, 
				fOperand2 = fOperand2
			)
			self.aOperandStack += [fResultado]
		self.answer = self.aOperandStack[-1]
		self.clearAll()
		return self.answer



class CalculatorInterface(tk.Frame):
	def __init__(self, master=None, calculator=None):
		super().__init__(master)
		self.master = master
		self.calculator = calculator
		self.pack()
		self.calculator.__init__()
		self.oDisplayValue = tk.StringVar()
		self.widgets = []
		self.createButtonsList()
		self.createButtonsPositions()
		self.create_widgets()

	def createButtonsList(self):
		self.aNumbers = {}
		for number in range(0,10):
			self.aNumbers["{}".format(number)] = "{}".format(number)
		self.aOperators = {
			"add": "+",
			"sub": "-",
			"div": "/",
			"mul": "*",
			"pow": "^",
			"rot": "r",
			"dot": ".",
			"clr": "C",
			"cle": "CE",
			"ans": "=",
			"ent": "Enter"		
		}

	def createButtonsPositions(self):
		self.aButtonsPositions = {
			"0": (10,320),
			"1": (10,250),
			"2": (70,250),
			"3": (130,250),
			"4": (10,180),
			"5": (70,180),
			"6": (130,180),
			"7": (10,110),
			"8": (70,110),
			"9": (130,110),
			"add": (190,320),
			"sub": (190,250),
			"div": (190,180),
			"mul": (190,110),
			"pow": (250,320),
			"rot": (250,250),
			"dot": (130,320),
			"clr": (250,180),
			"cle": (250,110),
			"ans": (190,40),
			"ent": (10,40)			
		}

	def createEntry(self):
		self.widgets += [
			tk.Entry(
				self.master,
				font=("Courier New",12,'bold'),
				textvar=self.oDisplayValue,
				width=25,
				bd=5,
				bg='powder blue'
			).pack()
		]
		
	def clickButton(self, sKeyPressed):
		if sKeyPressed in self.aNumbers.keys():
			self.oDisplayValue.set(
				self.calculator.addToTemporaryOperand(sKeyPressed)
			)
			return True
		if sKeyPressed == "Enter":
			self.oDisplayValue.set(
				self.calculator.addOperandToStack()
			)
			return True
		if sKeyPressed == "=":
			self.oDisplayValue.set(
				self.calculator.getResult()
			)
			return True
		if sKeyPressed == "CE":
			self.oDisplayValue.set(
				self.calculator.clearAll()
			)
			return True
		if sKeyPressed == "C":
			self.oDisplayValue.set(
				self.calculator.clearTemporaryNumber()
			)
			return True
		self.oDisplayValue.set(
			self.calculator.addOperatorToStack(sKeyPressed)
		)
		
	def drawButton(self, name, text):
		aButtonPosition = self.getButtonPosition(sButtonName=name)
		aButtonSize = self.getButtonSize(sButtonName=name)
		return tk.Button(
			self.master,
			padx=aButtonSize[0],
			pady=aButtonSize[1],
			bd=4,
			bg='white',
			font=("Courier New", 16, 'bold'),
			name=name,
			text=text,
			command=lambda: self.clickButton(text)		
		).place(x=aButtonPosition[0], y=aButtonPosition[1])
		
	def createButtons(self, itens):
		for key in itens.keys():
			self.widgets += [self.drawButton(name=key, text=itens[key])]
		
	def getButtonPosition(self, sButtonName=None):
		if not sButtonName in self.aButtonsPositions.keys():
			return (0,0)
		return self.aButtonsPositions[sButtonName]
		
	def getButtonSize(self, sButtonName=''):
		if sButtonName == '0':
			return (45,15)
		if sButtonName == 'ent':
			return (45,15)
		if sButtonName in "cleclrrotpow":
			return (30,15)
		return (15,15)
			
	def create_widgets(self):
		self.createEntry()
		self.createButtons(self.aNumbers)
		self.createButtons(self.aOperators)

root = tk.Tk()
root.geometry("360x400")
root.title("Calculator")
app = CalculatorInterface(master=root, calculator=Calculator())
app.mainloop()