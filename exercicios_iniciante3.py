import unittest
import random

def random_generator(upperBound: int, lowerBound: int) -> int:
    int_type = 1
    if type(upperBound) != type(lowerBound) and type(upperBound) != type(int_type):
        return -1

    if lowerBound >= upperBound and lowerBound >= 0:
        return -1
    
    return random.randint(lowerBound, upperBound)

def ler_entradas(numero: int) -> int:
    try: 
        score = 100
        tentativa = numero - 1
        i = 0
        flag = True
        while flag:
            tentativa = int(input("{}º tentativa: ".format(i+1)))
            if tentativa == numero  or score <= 0:
                flag = False
            else:            
                i = i + 1
                score = score - 10
                tip = "bigger" if (tentativa>numero) else "smaller"
                print ("Your guess is {} than the number!".format(tip))

        return score
    except ValueError:
        print("O valor informado precisa ser um numero inteiro.")

def jogar():
    try:
        numero = -1
        while numero < 0:
            upperBound = int(input("Informe o limite superior (inteiro) :"))
            lowerBound = int(input("Informe o limite inferior (inteiro) :"))
            numero = random_generator(upperBound, lowerBound)

        print("Gerado o numero aleatorio\n\n\n")
        pontos = ler_entradas(numero)
        print("Você fez um total de {} pontos, O número é {}".format(pontos, numero))
    except ValueError:
        print("Os números informados precisam ser um número inteiro")

jogar()