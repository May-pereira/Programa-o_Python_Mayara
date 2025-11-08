import os
os.system('cls')
import math

"""Entrar com o lado de um quadrado e imprimir:
perimetro:
area:
diagonal:"""

lado = float(input("Digite o lado "))

perimetro = 4 * lado
print(perimetro)

area = lado*lado
print(area)

diagonal = lado*math.sqrt(2)
print(diagonal)