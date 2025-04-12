pares = []
def somaNumerosPares():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0 or numero % 2 != 0:
        print("numero negativo ou impar")
    for i in range(0, numero +1 , 2):
        print(i)
        pares.append(i)
    print(pares,sum(pares),numero)

somaNumerosPares()

