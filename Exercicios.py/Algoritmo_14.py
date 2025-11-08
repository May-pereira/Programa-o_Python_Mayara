import os
os.system('cls')
import math

"""Entrar com o número e a base em que se deseja calcular o logaritmo desse
número e imprimi-lo."""

numero = float(input("Digite um numero "))
base = float(input("Digite um numero"))

resultado = math.log(numero,base)

print (f" O logaritmo de {numero} na {base} é {resultado} ")