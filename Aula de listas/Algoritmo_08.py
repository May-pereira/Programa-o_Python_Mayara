import os
import time
os.system('cls')

#Procurar o produto na lista 
lista_compras = ["Arroz", "Feijão", "Açucar", "Leite"]

produto_procurado = "Feijão"

if (produto_procurado in lista_compras):
    print(f"{produto_procurado} está disponivel")

else:
    print(f"{produto_procurado} Não está disponivel ")