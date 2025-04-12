try :
    n1 = int(input("Digite um número: "))

    print(n1)

except ValueError as erro:
    print("numero digitado não é inteiro")