try :
    lista = [1,2,3]
    dado = int(input("digite o indice"))
    print(lista[dado])
except IndexError as erro:
    print("erro")