import os
os.system('cls')

#Entrar com o nome de uma pessoa e só imprimi-lo se o prenome for JOSÉ

nomecompleto = input("Digite o nome ")

prenome = nomecompleto.split()[0].upper()

if prenome == "JOSÉ":
    print(nomecompleto)

else:
    print("O prenome não é JOSÉ. nada a imprimir. ")
