import os
os.system('cls')
import time

"""Entrar com números e imprimir o triplo de cada número O algoritmo acaba
quando entrar o número -999"""

while(True):
    numero = int(input("Digite um numero "))

    if (numero == -999):
        break
    
    else:
        numero = numero*3
        print(f"O triplo é {numero}")


    