def display1(nome):
    print('Olá seja bem vindo', nome)


def carrinho(produtos):
    lista_prod = ['a','b','c']
    meu_carrinho = []
    valores = [10,20,30]
    meu_total = []
    print(produtos)
    p =  input('Deseja fazer o pedido? s/n')
    while p == 's':
        pedido = int(input('Digite seu produto:> '))
        meu_carrinho.append(lista_prod[pedido])
        print(meu_carrinho)
        meu_total.append(valores[pedido])
        soma_total = sum(meu_total) 
        # print('R$', soma_total)
        p =  input('Deseja fazer o pedido? s/n')
        print('Total do pedido  - R$',soma_total )    
    return meu_carrinho







# import statistics


# # soma(obj, obj)
# def soma(a,b):
#     return a + b


# def sub(a,b):
#     return a - b


# def mult(a,b):
#     return a * b


# def div(a,b):
#     return a / b



# def mediana(lista):
#     mediana1 = statistics.median(lista)
#     print(mediana1)  

