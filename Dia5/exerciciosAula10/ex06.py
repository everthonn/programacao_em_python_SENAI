def copa():
    lista = [1958,1962,1970,1994,2002]
    ano = int(input("Digite um ano: "))
    ano_copa = (ano - 1930) % 4
    if ano in lista:
        print("O Brasil ganhou a copa nesse ano")
    if ano < 1930 or ano > 2022 or ano_copa != 0:
        print("nesse ano não houve copa")
    if ano_copa == 0 and ano not in lista:
        print("O Brasil não ganhou a copa nesse ano") 

copa()
        