ecommerce = {

    "fones" : ["jbl","qcy","samsung"],
    "valoresFones" : [10.0,15.0,25.0],
    "computadores" : ["mac","dell","lg"],
    "valoresComputadores" : [10.0,15.0,25.0]
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
valores += (([ecommerce[valorItem][int(valor)]]))
valorItem2 = input("digite valores e o item desejado ex: valoresFones")
valor2 = int(input("0,1,2"))
valores += ([ecommerce[valorItem2][int(valor2)]])

soma = sum(valores)
print("os itens selecionados serão exibidos abaixo juntamente com seus respectivos valores")
print(carrinho)
print(valores)

print("Valor total de R$ ",soma)

# itens = sum(carrinho)


# print(itens)
