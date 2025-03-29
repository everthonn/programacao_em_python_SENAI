ecommerce = {

    "fones" : ["jbl","qcy","samsung"],
    "valoresFones" : [10,15,25],
    "computadores" : ["mac","dell","lg"],
    "valoresComputadores" : [10,15,25]
}

# 1 comprar 
carrinho = []
valores = []

escolha_tipo = input("digite o item")
carrinho.append([ecommerce[escolha_tipo][int(input("0,1,2"))]])
escolha_tipo2 = input("digite o item")
carrinho.append([ecommerce[escolha_tipo2][int(input("0,1,2"))]])


valorItem = input("digite valores e o item desejado ex: valoresFones")
valor = int(input("0,1,2"))
valores.append(([ecommerce[valorItem][int(valor)]]))
valorItem2 = input("digite valores e o item desejado ex: valoresFones")
valor2 = int(input("0,1,2"))
valores.append([ecommerce[valorItem2][int(valor2)]])

soma=sum(valores)
print(soma)
print(valores)
print(carrinho)
# itens = sum(carrinho)


# print(itens)