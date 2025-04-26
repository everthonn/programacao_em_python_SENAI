numero = int(input("digite um numero")) 

match numero:
    case numero if numero < 10:
        print("numero menor que 10")
    case numero if numero == 10:
        print("numero igual a 10")
    case numero if numero > 10:
        print("numero maior que 10")