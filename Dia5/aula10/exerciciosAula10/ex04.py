from rich import *
def dezoito():
    idade = int(input("digite sua idade\n"))
    if idade == 18:
        print("[blue][italic]Você tem 18 anos[/blue][/italic]")
    else:
        print(idade,"anos de idade")

dezoito()