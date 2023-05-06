def exibirMenu():
    print("Selecione uma opção de programa: ")
    print("\n")
    print("1 - Calcular sua Nota Final da Matéria")
    print("2 - Verificar se há débitos de mensalidade")
    print("3 - Sair")
    print("\n")


def calcularNotaFinal ():
    notaQuizz = float( input ("Digite nota do Quizz"))
    notaRedacao = float(input ("Digite nota da Redação"))
    notaProva = float(input ("Digite Nota da sua Prova"))
    notaFinal = round(((notaQuizz + notaRedacao + notaProva)/3),2)

    print("\n")
    print("\n")
    print("Sua nota é", notaFinal)
    print("\n")


def consultarDebito ():
    dataDeHoje = int (input ("Digite que dia é hoje"))
    dataNovaMensalidade = 5
    if (dataDeHoje >= 5 and dataDeHoje <= 15):
        print("\n")
        print("Você pode ter um novo débito. Acesse www.débito.com para visualizar")
    elif (dataDeHoje < 5 or dataDeHoje >15 or dataDeHoje <=30): 
        print("\n")
        print("Você provavelmente não tem novos débitos. Se deseja segunda via de boletos anteriores acesse o portal do aluno")
    else:
        print("\n")
        print("Essa data não é válida. Retorne ao Menu e digite novamente")

    print("\n")
    print("Voltando ao menu inicial")
    exibirMenu()

print("\n---- Bem vindo(a) ao programa da Faculdade ----\n")
 
exibirMenu()

opcaoSelecionada = input("Digite sua opção")

while opcaoSelecionada != "3":
    if (opcaoSelecionada == "1"):
        calcularNotaFinal()
    elif(opcaoSelecionada == "2"):
        consultarDebito()
    else: 
        print("Opção invalida")
        
    print("Voltando ao menu inicial")
    exibirMenu()
    opcaoSelecionada = input("Digite a nova ação")