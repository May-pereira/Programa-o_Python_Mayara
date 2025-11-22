import os
os.system('cls')
import time

numero = int(input("Digite um numero :"))

cont=1

while(cont<=10):
    total = numero*cont
    print(f"{numero} x {cont} : {total}")
    time.sleep (0.6)
    cont+=1
