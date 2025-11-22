import os
os.system('cls')

#Inseri a Uva
lista_compras = ["Arroz", "Feijão", "Açucar", "Leite"]
lista_compras.append("Uva")
print(lista_compras)

#removi a Uva
lista_compras.remove("Uva")
print(lista_compras)

#Como remover na posiçao desejada
lista_compras.remove(lista_compras[2])
print(lista_compras)