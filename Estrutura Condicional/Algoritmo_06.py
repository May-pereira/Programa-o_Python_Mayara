import os
os.system('cls')

"""Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A
(considerar letra minúscula ou maiúscula)."""

nome = input("Digite o nome ")

if nome.startswith('a') or nome.startswith('A'):
    print(f" O nome {nome} começa com a letra 'A' ou 'A'")

else:
     print("Não são letras ")