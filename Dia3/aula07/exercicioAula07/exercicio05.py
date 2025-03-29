#**Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

lista = [1,2,3,4,5,6,7,8,9,10]

print(lista[2])

lista.append(9)
print(lista)

del lista[4]
print(lista)