def soma():
    try:
        n1 = input(">")
        n2 = input(">")
        print(soma)
        d = n1/n2
        print(d)
        lista = [1,2,3]
        dado = int(input("digite o indice"))
        print(lista[dado])

    except TypeError as erro:
        print("dado não pode ser somado")
    except ValueError as erro:
        print("erro") 
    except ZeroDivisionError as erro:
        print("erro")
    except IndexError as erro:
        print("erro")

    finally:
        print("fim do carregamento")
soma()









# print(nome)
# print(10/0)
# n = int(input('digite algo'))
# n1 = "10"
# n2 = "20"
# print(n1 + n2)
