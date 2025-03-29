# lista = [1,2,3,6,5,5,6]

# ////////adicionar///////
# add 1 dado | apenas no final da lista

# lista.append(50)
# print(lista)

#//////insert///////
# precisa de um valor de indice(onde ira ficar), e do valor

# lista.insert(0,200)
# print(lista)

# += é uma tupla | ou lista

# lista += (10.2030,30,20,30,20,20)
# print(lista)

# lista.extend([1,0,10,0,20,50])
# print(lista)

#///// deletar//////

# lista = [1,2,3,7,8,8]
# print(lista)
# lista.pop()
# print(lista)

# lista = [1,2,3,7,8,8]
# lista.pop(2)
# print(lista)

# lista = [1,2,3,7,8,8]
# lista.remove(7)
# print(lista)

# lista = [1,2,3,7,8,8]
# del lista[-2]
# print(lista)

# lista = [1,[2,3],7,8,8]
# del lista[1][1]
# print(lista)

# lista = [12,[31,[34,32],32,3,2],13,13,23,23]
# del lista[1][1][0]
# print(lista)

#////Verificar a lista//////

# lista = [1,2,3,7,8,8]
# soma = sum(lista)
# print(soma)

# lista = [1,2,3,7,8,8]
# tamanho = len(lista)
# print(tamanho)

# lista = [1,20,30,70,80,800]
# menor = min(lista)
# print(menor)

# lista = [1,2,3,7,800,8]
# maior = max(lista)
# print(maior)

# lista = [1,2,3,7,800,8,8,8,7,6,5]
# print(lista)

# i = lista.index(800)
# print(i)

#//tambem é possivel usar direto do print()//
#print(lista.index(600))

# lista = [1,2,3,7,800,8]
# print(lista)
# lista.sort(reverse=True)
# print(lista)

# lista = [1,2,3,7,800,8]
# print(lista)
# lista.reverse()
# print(lista)

# lista = [1,2,3,7,800,8]
# print(lista)
# lista.sort(reverse=False)
# print(lista)


n = ["13","22","34","45"]
d = "-"
x = d.join(n)
print(x)

print(20,10,10,30, sep="=>")