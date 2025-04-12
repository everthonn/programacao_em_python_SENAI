import funcoes


def mercado():
    nome = input('Digite seu nome: ')
    funcoes.display1(nome)
    produtos = ['a','b','c']
    m =  funcoes.carrinho(produtos)
    print(m)
mercado()