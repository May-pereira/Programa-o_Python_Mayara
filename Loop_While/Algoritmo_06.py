import os
os.system('cls')
import time

"""Entrar com vários números positivos e imprimira média dos números digitados."""
cont = 0
acm = 0

numero = int(input("Digite um numero ou 0 para encerrar: "))

while(True):
   if(numero == 0):
    break
  
   acm = acm+numero
   numero = int(input("Digite um numero ou 0 para encerrar: "))

print(f"Programa encerrado e a soma toral foi {acm}")
