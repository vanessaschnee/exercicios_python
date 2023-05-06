def exibirMenu(): 
    print("Selecione uma opção de programa: ")
    print("\n")
    print("1 - Calcular seu IMC")
    print("2 - Calcular seu imposto de renda")
    print("3 - Sair")
    print("\n")

def calcularIMC():
    altura = float(input("Digite sua altura"))
    peso = float(input("Digite o seu peso"))
    imc = round(peso / (altura * altura),2)

    print("\nSeu imc é", imc)
    print("\n")

def calcularImpostoRenda():
    print("Calculei seu imposto de renda")
    print("\n\n")

print("\n---- Bem vindo(a) ao programa da Vanessa ----\n")

exibirMenu()

opcaoSelecionada = input("Digite sua opção")

while opcaoSelecionada != "3":
    if(opcaoSelecionada == "1"):
        calcularIMC()
    elif(opcaoSelecionada == "2"):
        calcularImpostoRenda()
    else: 
        print("Opção invalida")

    print("Voltando ao menu inicial")
    exibirMenu()
    opcaoSelecionada = input("Digite a nova ação")

print("Obrigado por usar o programa da Vanessa")


