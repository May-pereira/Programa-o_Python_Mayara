import os
os.system('cls')
import math

"""Entrar com o raio de um circulo e imprimir a seguinte saída:
perimetro:
area:"""

raio = float(input("Digitar o raio "))

perimentro = 2*math.pi*raio
area = math.pi*(math.pow(raio,2))

print(perimentro)
print(area)


