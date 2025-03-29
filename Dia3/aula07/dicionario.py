# pessoa = {

# "nome" : "everthon",
# "idade" : 17,
# "estado" : "São Paulo"


# }
# print(pessoa)
# print(pessoa["nome"])


# pessoa["esportes"] = ["futeball","basquete"]
# print(pessoa["esportes"])

# list - tuple - set - dict 

# dados = dict(a=100,b=200,c=300)
# print(dados['a'])

# print(dados.keys())

# print(dados.items())

# print(dados.values())

nome = input("digite o nome")
idade = input("digite a idade")
endereço = input("digite o endereço")

dadosCadastrados = {}

dadosCadastrados["nome"]=nome
dadosCadastrados["idade"]=idade
dadosCadastrados["endereço"]=endereço


print(dadosCadastrados)