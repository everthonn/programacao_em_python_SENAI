notas = {
    "joao" : 0,
    "pedro" : 0,
    "vitoria" : 0
}
n=0
for i in range(1,4):
    login = input("Digite seu login")
    senha = input("Digite sua senha")
    if login == 'thon' and senha == '3435':
        for c,v in notas.items():

            nota1,nota2,nota3 =float(input("Digite a nota1")),float(input("Digite a nota2")),float(input("Digite a nota3"))
            notas[c] = [nota1 , nota2 , nota3]
            media = (sum(notas[c])/len(notas[c]))
            print(c,media)
            
        break
    

    



else:
    print("Conta Bloqueada")

print(notas)
i = input("digite enter para sair: ")