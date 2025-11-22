import os
import time
os.system('cls')

#Fazendo um lista com posições, contando.
lista_compras = ["Arroz", "Feijão", "Açucar", "Leite"]

cont =0
for lista in lista_compras:
    print(f"Posição {cont} valor {lista}")
    time.sleep(0.7)
    cont+=1