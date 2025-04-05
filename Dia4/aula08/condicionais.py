import random

# numero: random.random()
# numero = random.randint(1,20)

# print(numero)




# if 10 > 2: #true
#     print("10 é amior")
# else:
#     print("10 é menor")

# numero = random.randint(1,20)
# print(numero)
# chute= int(input("chue um numero"))


# if numero == chute:
#     print("certa resposta")
# else:
#     print("erroou")


# cartaMotorista = bool(input("possui CNH?"))
# idade = int(input("digite sua idade"))

# if cartaMotorista== "sim" and idade >=18:
#     print("habilitado")
# else:
#     print("não pode dirigir")




# condimentos = input("possui farinha, açucar, ovos, leite?")
# microondas = input("microondas?")
# ayrFrayer = input("ayr Frayer?")
# forno = input("forno?")

# if condimentos and forno or microondas or ayrFrayer == "sim":
#     print("pode começar a preparar")

# else:
#     "impossivel preparar"


alunos = {
        'Ana':[10,9,8,5.5,3,7,10],
        'Fernanda':[1,2,3,6,5,2,7],
        'Leo':[10,10,10,10,10,10,10]
     }




NOTAS_ANA = alunos['Ana']
maior_nota_ana = max(NOTAS_ANA)
NOTAS_FERNANDA = alunos['Fernanda']
maior_nota_fernanda = max(NOTAS_FERNANDA)
NOTAS_LEO =alunos['Leo']
maior_nota_leo = max(NOTAS_LEO)

# print(f'MAIOR NOTA ANA - {maior_nota_ana}\nMAIOR NOTA FERNANDA - {maior_nota_fernanda}\nMAIOR NOTA LEO - {maior_nota_leo} ' )

media_ana = sum(alunos['Ana'])/len(alunos['Ana'])
media_fernanda = sum(alunos['Fernanda'])/len(alunos['Fernanda'])
media_leo = sum(alunos['Leo'])/len(alunos['Leo'])

medias = [media_ana, media_fernanda,media_leo]
media_total = sum(medias) / len(medias)
# print('MÉDIA GERAL', media_total)


lista_nomes = ['Ana','Fernanda','Leo']
maior = max(medias)
indice = medias.index(maior)
# print(lista_nomes[indice], 'Maior Media', maior)


NOTAS_ANA.sort()
# print(f'mediana  ana- {NOTAS_ANA[3:4]}')
# print(f'amplitude  ana- {max(NOTAS_ANA) - min(NOTAS_ANA)}')
NOTAS_FERNANDA.sort()
# print(f'mediana  fernanda- {NOTAS_FERNANDA[3:4]}')
# print(f'amplitude  fernanda- {max(NOTAS_FERNANDA) - min(NOTAS_FERNANDA)}')
NOTAS_LEO.sort()
# print(f'mediana  leo - {NOTAS_LEO[3:4]}')
# print(f'amplitude  leo- {max(NOTAS_LEO) - min(NOTAS_LEO)}')

modaAna = max(set(NOTAS_ANA), key=NOTAS_ANA.count)
# print('moda ANa', modaAna)

modaFer = max(set(NOTAS_FERNANDA), key=NOTAS_FERNANDA.count)
# print('moda Fernanda', modaFer)

modaLeo = max(set(NOTAS_LEO), key=NOTAS_LEO.count)


 
    
# média de notas soma() / len()
# maior média max()
# maior nota de cada aluno max()
# mediana ordenar a lista - meio  
# amplitude 
# moda 
print("sistema escolar")
print("1-media total ||2- média aluno ||3- moda mediana amplitude ||4- maior nota")
escolha = input("digite o que deseja visualizar")

if escolha == "1":
    print('MÉDIA GERAL', media_total)

elif escolha == "2":
        print("Média alunos:")
        print("Ana", media_ana)
        print("Fernanda", media_fernanda)
        print("Leo", media_leo)
elif escolha =="3":
      print("mode|Mediana|Amplitude")
      print("ANA")
      print(f'mediana  ana- {NOTAS_ANA[3:4]}')
      print(f'amplitude  ana- {max(NOTAS_ANA) - min(NOTAS_ANA)}')
      print('moda ANa', modaAna)
      print("--------------------------------------------------------------------------")
      print("fernanda")
      print(f'mediana  fernanda- {NOTAS_FERNANDA[3:4]}')
      print(f'amplitude  fernanda- {max(NOTAS_FERNANDA) - min(NOTAS_FERNANDA)}')
      print('moda Fernanda', modaFer)
      print("--------------------------------------------------------------------------")
      print("Leo")
      print(f'mediana  leo - {NOTAS_LEO[3:4]}')
      print(f'amplitude  leo- {max(NOTAS_LEO) - min(NOTAS_LEO)}')
      print('moda leo', modaLeo)
elif escolha =="4":
      print(f'MAIOR NOTA ANA - {maior_nota_ana}\nMAIOR NOTA FERNANDA - {maior_nota_fernanda}\nMAIOR NOTA LEO - {maior_nota_leo} ' )