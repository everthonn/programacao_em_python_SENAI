inicio = int(input("quantos clientes deseja cadastrar?(maximo de 3)"))

if inicio == 3:

    hotel = {
        "simples":100,
        "duplo":150,
        "luxo":250
    }

    nomeCliente1 = input("nome do cliente 1: ")
    idadeCliente1 = input("idade cliente 1: ")
    diariasCliente1 = float(input("quantos dias deseja permanecer"))
    escolhaSuite1 = input("qual o quarto desejado")
    

    #////////////////////////////////////////////////////

    nomeCliente2 = input("nome do cliente 2: ")
    idadeCliente2 = input("idade cliente 2: ")
    diariasCliente2 = float(input("quantos dias deseja permanecer"))
    escolhaSuite2 = input("qual o quarto desejado")
    

    #//////////////////////////////////////////

    nomeCliente3 = input("nome do cliente 3: ")
    idadeCliente3 = input("idade cliente 3: ")
    diariasCliente3 = float(input("quantos dias deseja permanecer"))
    escolhaSuite3 = input("qual o quarto desejado")



    valor1 = hotel[escolhaSuite1]*diariasCliente1
    valor2 = hotel[escolhaSuite2]*diariasCliente2
    valor3 = hotel[escolhaSuite3]*diariasCliente3


    print("nome:",nomeCliente1,"   suite:",escolhaSuite1,"   diarias:",diariasCliente1,"\n","nome:", nomeCliente2,"   suite:",escolhaSuite2,"   diarias:",diariasCliente2,"\n","nome:",nomeCliente3,"   suite:",escolhaSuite3,"   diarias:",diariasCliente3)
    print("valores \n cliente 1",valor1,"\n cliente 2",valor2,"\n cliente 3",valor3)

elif inicio == 2:
    hotel = {
        "simples":100,
        "duplo":150,
        "luxo":250
    }

    nomeCliente1 = input("nome do cliente 1: ")
    idadeCliente1 = input("idade cliente 1: ")
    diariasCliente1 = float(input("quantos dias deseja permanecer"))
    escolhaSuite1 = input("qual o quarto desejado")
    

    #////////////////////////////////////////////////////

    nomeCliente2 = input("nome do cliente 2: ")
    idadeCliente2 = input("idade cliente 2: ")
    diariasCliente2 = float(input("quantos dias deseja permanecer"))
    escolhaSuite2 = input("qual o quarto desejado")

    valor1 = hotel[escolhaSuite1]*diariasCliente1
    valor2 = hotel[escolhaSuite2]*diariasCliente2

    print("nome:",nomeCliente1,"   suite:",escolhaSuite1,"   diarias:",diariasCliente1,"\n","nome:", nomeCliente2,"   suite:",escolhaSuite2,"   diarias:",diariasCliente2)
    print("valores \n cliente 1",valor1,"\n cliente 2",valor2)

elif inicio == 1:

    
    hotel = {
        "simples":100,
        "duplo":150,
        "luxo":250
    }

    nomeCliente1 = input("nome do cliente 1: ")
    idadeCliente1 = input("idade cliente 1: ")
    diariasCliente1 = float(input("quantos dias deseja permanecer"))
    escolhaSuite1 = input("qual o quarto desejado")

    valor1 = hotel[escolhaSuite1]*diariasCliente1
    print("nome:",nomeCliente1,"   suite:",escolhaSuite1,"   diarias:",diariasCliente1)
    print("valor \n cliente 1",valor1)
else:
    print("impossivel cadastrar mais que 3 pessoas")