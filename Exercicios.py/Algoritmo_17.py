import os
os.system('cls')
import math

"""Antes de o racionamento de energia ser decretado, quase ninguém falava em
quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.

Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
fazer um algoritmo que receba o valor do salário mínimo e a quantidade de
quilowatts gasta por uma residência e calcule. Imprima:
O valor em reais de cada quilowatt
O valor em reais a ser pago
O novo valor a ser pago por essa residência com um desconto de 10%."""

salarioMinimo = float(input("Digite o salario"))
quantidade = int(input("Digite a quantidade de quilowatts"))

umkw = (salarioMinimo/7)/100
kwgasta = quantidade * umkw
kwGastoDesc = kwgasta - (kwgasta*0.10)
print(f"Total a pagar R${kwGastoDesc}")
