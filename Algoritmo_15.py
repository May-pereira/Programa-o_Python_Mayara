import os
os.system('cls')
import math

"""Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima
o novo saldo, considerando o reajuste de 1%."""

saldo = float(input("Digite o saldo"))
novosaldo = saldo + (saldo 0.01)
print(f" O novo saldo com o reajuste 1% é, {novosaldo} ")