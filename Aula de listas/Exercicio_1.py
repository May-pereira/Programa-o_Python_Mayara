import os
import time
os.system('cls')

"""crie um programa para gerenciar uma lista de compras. O programa deve: 
-> Iniciar com 3 produtos 
-> Adicionar 2 ovos 
-> Remover um produto 
-> Mostrar a lista atualizada no final """

lista = ["Abacate", "Mamão", "Banana"]
print(lista)

lista.append("2 ovos")
print(lista)

lista.remove("Banana")
print(lista)

