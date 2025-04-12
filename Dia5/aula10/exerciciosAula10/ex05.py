from datetime import datetime

def descobrir_idade():
    ano = int(input("Ano de nascimento: "))
    mes = int(input("Mês de nascimento: "))
    dia = int(input("Dia de nascimento: "))
    data_nascimento = datetime(ano, mes, dia)
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade   


print(f"Idade: {descobrir_idade()} anos.")

input("Pressione Enter para fechar...")

