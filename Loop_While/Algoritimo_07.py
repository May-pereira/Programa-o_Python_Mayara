import os
os.system('cls')
import time

soma = 0
cont = 0

nota = float(input("Digite a nota "))

while(nota>0):
    soma=soma+nota
    cont+=1
    nnota = float(input("Digite a nota "))

media = soma/cont

print(f"Media {media}")