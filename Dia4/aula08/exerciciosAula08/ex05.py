numero = int(input('digite um numero'))

if numero % 5 == 0 and numero % 7 ==0 :
    print("numero multiplo de 5 e 7")
elif numero % 5 == 0 :
    print("numero multiplo de 5")
elif numero % 7 == 0:
    print("numero multiplo de 7")
else:
    print("numero não é multiplo nem de 5 nem de 7")