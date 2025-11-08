import os
os.system('cls')
import math

"""Entrar com um nome e imprimir:
todo nome:
primeiro caractere:
último caractere:
do primeiro até o terceiro:
quarto caractere:
todos menos o primeiro:
os dois últimos:"""

nome = input (" Digite seu nome ")
print("Primeira caratere " + nome [:1])
print("Ultimo caratere " + nome [-1::])
print("Do peimeiro até o terceiro caratere " + nome [:3])
print("quarto caratere " + nome [3])
print("Todos menos o primeiro " + nome [1::])
print("Os dois ultimos " + nome [-2:])