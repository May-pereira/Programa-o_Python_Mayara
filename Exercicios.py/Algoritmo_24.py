import os
os.system('cls')

#Faça uma sequencia de condicoes com if , else !

idade = int(input("Digite a idade " ))

if (idade >= 0 and idade <= 11):
    print ("Infantil")

elif (idade >= 12 and idade <= 17):
    print ("Adolescente")

elif (idade >= 18 and idade <= 24):
    print ("jovem")

else:
     print ("Adulto")
     
