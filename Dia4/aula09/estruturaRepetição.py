
# for variavel in sequencia 

# for numero in range (1,4):
#     nome = input("digite seu nome")
#     idade = int(input("digite sua idade"))
#     print(numero)

# nomes = []

# for i in range(3):
#     idade = int(input("digite sua idade"))
#     nome = input("digite seu nome")
#     nomes.append(nome)
#     print(nomes)

import random

lista = [1,2,3]

for chances in lista:
    aleatorio = random.randint(10,11)
    chute = int(input("chute um numero entre 1 e 10 \n"))
    if aleatorio == chute:
        print("certa resposta")
        break
    else:
        print("errou feio")
        print("você tem mais", 3-chances, "chances")
else:
    print("você perdeu")
    print("o numero era", aleatorio)