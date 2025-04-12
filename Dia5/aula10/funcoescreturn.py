# Com parametro e return


def calculo_hora(carga,salario):
    return salario/carga


def calculo_extra_50(hora):
    return hora * 1.5


def calculo_hora_noturna(hora):
    return hora * 1.2    


def cumprim(nome):
    print('Olá', nome)     


def sistema_de_horas():
    nome = input('Nome: ')
    cumprim(nome)
    escolha = int(input('Valor/hora - 1 Extra 50% - 2 Adicional noturno 20% - 3'))
    if escolha == 1:
       carga = float(input('Carga de trabalho mês: '))
       salario =  float(input('Digite o salario: ')) 
       print('R$', round(calculo_hora(carga,salario),2))
    elif escolha == 2:
         carga = float(input('Carga de trabalho mês: '))
         salario =  float(input('Digite o salario: ')) 
         valor_hora  =  calculo_hora(carga,salario)
         print('extra 50%:',round(calculo_extra_50(valor_hora),2))  
    elif escolha == 3:
         carga = float(input('Carga de trabalho mês: '))
         salario =  float(input('Digite o salario: ')) 
         valor_hora  =  calculo_hora(carga,salario)
         print('adicional noturno extra 20%:',round(calculo_hora_noturna(valor_hora),2))   



    else:
        print('Digite algo valido')    



sistema_de_horas()