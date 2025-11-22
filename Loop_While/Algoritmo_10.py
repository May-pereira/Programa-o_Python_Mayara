import os
os.system('cls')
import time

       
""""Ler vários números e informar quantos números entre 100 e 200 foram
digitados. Quando o valor 0 (zero) for lido, o algoritmo deverá cessar sua
execução."""

cont = 0

while(True):

    numero = int(input("Digite o numero "))

    if numero == 0:
        break

    if numero>= 100 and numero<=200:
        cont+=1

print(f"Total de numeros entre 100 e 200 é {cont} ")

       