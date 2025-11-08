import os
os.system('cls')

"""Entrar com um número e imprimir uma das mensagens: maior do que 20, igual
a 20 ou menor do que 20."""

numero = int(input("Digite um numero "))

if (numero > 20):
    print (f"Maior  {numero} ")

elif(numero == 20 ):
    print (f"igual  {numero} ")

else:
    print(f"menor {numero} ")


