import os
os.system('cls')
import math


"""Ler dois números inteiros e imprimir o produto."""
numero1 = float(input("Digite um numero"))
numero2 = float(input("Digite um numero "))

dividendo = numero1
divisao = numero2
quociente = dividendo/divisao 
resto = dividendo % divisao 

print(f"Dividendo: {dividendo} \nDivsao: {divisao}\nquociente {quociente}\nResto: {resto}")

