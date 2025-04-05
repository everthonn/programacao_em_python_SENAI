idade = int(input("digite a sua idade"))
titulo = input("você possui titulo de eleitor?")
if idade >= 16 and titulo == "sim":
    print("pode votar")
else:
    print("não pode votar")