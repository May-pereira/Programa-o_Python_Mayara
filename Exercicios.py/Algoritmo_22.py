import os
os.system('cls')
import math

"""Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a
diagonal."""

a = float(input("Digite um lado a: "))
b = float(input("Digite um lado b: "))
c = float(input("Digite um lado c: "))

diagonal = math.sqrt(math.pow (a,2) + math.pow(b,2) + math.pow(c,2))
print(diagonal)