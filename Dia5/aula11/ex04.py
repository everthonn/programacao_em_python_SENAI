def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError as erro:
        print("Erro: Divisão por zero não é permitida.")
        
    except TypeError as erro:
        print("Erro: Tipos de dados inválidos para divisão.")
        
print(divisao(float(input("digite um numero: ")), float(input("Digite um número: "))))
