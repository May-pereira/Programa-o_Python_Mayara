import os
os.system('cls')

"""Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade
da pessoa. Não se esqueça de verificar se o ano de nascimento é um ano
válido."""

anoNascimento = int(input("Digite o anoNascimento "))
anoAtual = int(input("Digite o anoAtual "))

idade = anoAtual - anoNascimento

if (anoNascimento > anoAtual):
    print(f"Erro {idade} ")

else:
    print(f"idade atual é {idade}")