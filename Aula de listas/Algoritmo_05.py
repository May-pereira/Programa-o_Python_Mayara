import os
os.system('cls')

#Inseir o produto na posição desejada 
lista_compras = ["Arroz", "Feijão", "Açucar", "Leite"]

lista_compras.insert(0,"óleo")
print(lista_compras)

lista_compras.insert(3,input("Digite um produto: "))
print(lista_compras)
