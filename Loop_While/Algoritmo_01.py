import os
os.system('cls')

cont = 0
acm = 0

numero = int(input("Digite um numero ou 0 para encerrar "))

while (numero!=0):
    acm=acm+numero 
    numero = int(input("digite um numero ou 0 para encerrar "))

print(f"Programa encerrar e a soma total foi {acm}")
