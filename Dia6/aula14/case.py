nu =int(27)
match nu % 2:
    case 0:
         print("divisivel")
    
    case 1:
         print("não é divisivel")

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)
escolha = int(input("Escolha um número entre 1 e 10: "))


match escolha:
     case escolha if escolha == numero_aleatorio:
            print("Você acertou!")
     case _:
          print("Você errou!")

