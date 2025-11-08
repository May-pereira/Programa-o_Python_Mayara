import os
os.system('cls')

"""Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo
feminino e tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA.
Caso contrário, imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou
F.)"""

nome = input("Digite o nome ")
sexo = input("Digite o sexo")
idade = int(input("Digite a idade"))

if (sexo == 'f' or sexo == 'F') and (idade < 25):
    print(f"{nome}: ACEITA ")

else:
    print(f"{nome}: Não ACEITA ")