def cumprimentar():
    print('Seja bem vindo ao sistema de horas')


def valorhora():
    carga = float(input('digite hora/mês '))
    salario =  float(input('Salario'))


    calculo_hora = salario/carga
    extra = calculo_hora * 1.5
    quant_hora_extra = float(input('Quantidade hora extra: '))
    Adcional_notuno_quant = int(input('Horas noturnas'))
    hex_n = calculo_hora * 1.2



    print('Horas R$:', round(calculo_hora,2))
    print('Hora extra 50% R$ ', round(extra,2))
    print('Quantidade realizada hora extra:',round(quant_hora_extra,2) )
    print('Hora extra noturna R$',round( hex_n,2))

def calculo_hora(carga, salario):
    return salario/carga

def hora_extra(calculo_hora, quant_hora_extra):
    return calculo_hora * 1.2 * quant_hora_extra
# RETURN X PRINT



def sistema_de_horas():
    cumprimentar()
    # opcoes = ['','Horas'  ]
    escolha = input('Deseja fazer o calculo de horas? s/n')
    if escolha == 's':
        valorhora() 
    else:
        print('Saindo do sistema...')    



sistema_de_horas()