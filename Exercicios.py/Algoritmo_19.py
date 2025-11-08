import os
os.system('cls')
import math

"""Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
peri metro
area
diagonal:"""

altura = int(input("Altura "))
base = int(input("Base "))

perimetro = 2*(base+altura)
print(perimetro)

area = base * altura
print(area)

diagonal = math.sqrt(math.pow(base,2)+math.pow(altura,2))
print(diagonal)