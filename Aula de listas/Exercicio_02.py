import os
import time
os.system('cls')

"""Crie um sistema simples de estoque que :
-> Verifique se o produto esta disponivel 
-> Mostrar o primeiro e o ultimo produto da lista
-> adicionar 5 produtos usando for 
-> Verificar a lista e adicionar separado um ultimo item """

lista_produto = ["Vestido", "Camisa", "Calça"]
produto_procurado = ("Vestido")

if (produto_procurado in lista_produto):
    print(f"{produto_procurado} está disponivel ")

else:
    print(f"{produto_procurado} não está disponivel ")
    
#################################################################

primeiro_produto = lista_produto [0]
ultimo_produto = lista_produto [-1]

print(f"Primeiro produto {primeiro_produto} ultimo produto {ultimo_produto} ")
###############################################################
cont=0 

for lista in range(5):
    lista_produto.append(input(" Digite um produto" ))

    print(lista_produto)

###############################################################

lista_produto.append("Brinde ")
print(lista_produto)