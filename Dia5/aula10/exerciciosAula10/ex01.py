#CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def comparar_par_impar(num1, num2):
    if num1 % 2 == 0:
        status1 = "par"
    else:
        status1 = "ímpar"

    if num2 % 2 == 0:
        status2 = "par"
    else:
        status2 = "ímpar"

    return f"O número {num1} é {status1} e o número {num2} é {status2}."

resultado = comparar_par_impar(int(input("digite um numero\n")), int(input("\ndigite outro numero\n")))
print(f"{resultado}")