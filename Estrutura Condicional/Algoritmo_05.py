import os
os.system('cls')

"""Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
carioca
paulista
mineiro
outros estados"""

estado = input("Digite a sigla de estado ")

if estado == "SP" or estado == "sp":
    print("Paulista ")

elif estado == "RJ" or estado == "rj":
    print("Carioca ")

elif estado == "MG" or estado == "mg":
    print("Mineiro ")

else:
    print("outros estados ")