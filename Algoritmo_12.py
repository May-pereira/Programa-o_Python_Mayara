import os
os.system('cls')
import math

"""Entrar com um ângulo em graus e imprimir: seno, coseno, tangente, secante,
co-secante e co-tangente deste ângulo."""

graus = int(input("Digite um numero "))
radian = math.radians (graus)

seno = math.sin(radian)
cosseno = math.cos(radian)
tangente = math.tan(radian)

secante = 1/ (radian)
cosecante = 1/ (radian)
cotangente = 1/ (radian)

print(f"seno {seno}")
print(f"cosseno {cosseno}")
print(f"tangente {tangente}")
print(f"secante {secante}")
print(f"co-secante {cosecante}")
print(f"co-tangente {cotangente}")