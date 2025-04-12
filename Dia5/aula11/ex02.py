try:    
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    print(n1/n2)

except ZeroDivisionError as erro:
    print("erro")
except ValueError as erro:
    print("numero digitado não é inteiro")