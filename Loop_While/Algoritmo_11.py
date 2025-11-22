import os
os.system('cls')
import time

"""Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro
caractere de cada nome."""

while True:
     
    nome = input("Digite um nome ou fim para sair ")

    if nome == "fim":
         break
        
    if len(nome) >0 :
        print(f"Primeira caracter de {nome} é {nome[0]}")

    else:
        print("Nome vazio, não valido")

       
import os
os.system('cls')
import time

"""Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro
caractere de cada nome."""

while True:
     
    nome = input("Digite um nome ou fim para sair")

    if nome == "fim":
        break
        
    if len(nome) >0 :
        print(f"Primeira caracter de {nome} é {nome[0]}")

    else:
        print("Nome vazio, não valido")

