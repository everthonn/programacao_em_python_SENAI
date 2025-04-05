nomes = []
 
n= 0
while n < 10:
     nome = input("digite um nome:")
     nomes.append(nome)
     n += 1

print("Nomes digitados:")
print(nomes)
print("Nomes digitados em ordem inversa:")
print(nomes[::-1])
print("Nomes digitados em ordem alfabética:")
nomes.sort()
print(nomes)