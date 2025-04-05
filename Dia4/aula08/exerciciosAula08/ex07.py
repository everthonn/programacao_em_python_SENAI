numero = int(input('digite um numero'))

if numero % 3 == 0 and numero % 5 ==0 :
    print("numero divisivel por 5 e 3")
elif numero % 3 == 0 :
    print("numero divisivel por 3")
elif numero % 5 == 0:
    print("numero divisivel por 5")
else:
    print("numero não é divisivel nem por 3 nem por 5")