lado1 = int(input("digite o lado do triangulo"))
lado2 = int(input("digite o lado do triangulo"))
lado3 = int(input("digite o lado do triangulo"))

if lado1 >0 and lado2 > 0 and lado3 > 0 :
    if lado1 == lado2 and lado3 == lado1:
        print("triangulo equilatero")
    elif (lado2 == lado3 and lado2 != lado1) or (lado1 == lado3 and lado1 != lado2) or (lado1 == lado2 and lado1 != lado3) :
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
else:
    print("medidas invalidas")