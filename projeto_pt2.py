print("Jogando caça ao número!")

dificuldade = int(input("Digite um número que represente o nível de dificuldade, onde- 1 é fácil e da 10 chances; 2 é "
                        "medio e da 6 chances; 3 é difícil e da 3 chances: "))
numerosecreto = 42

if dificuldade < 1 or dificuldade > 3:
    print("Opção inválida")
    exit(1)

contador = 1

if dificuldade == 1:
    chances = 10
    while contador <= 10:
        chute = int(input("Dê um palpite para tentar acertar o número sorteado pelo computador: "))
        contador += 1
        if chute == numerosecreto:
            print("Você acertou!")
            break
    else:
        print("Acabaram suas chances")
elif dificuldade == 2:
    chances = 6
    while contador <= 6:
        chute = int(input("Dê um palpite para tentar acertar o número sorteado pelo computador: "))
        contador += 1
        if chute == numerosecreto:
            print("Você acertou!")
            break
    else:
        print("Acabaram suas chances")
else:
    chances = 3
    while contador <= 3:
        chute = int(input("Dê um palpite para tentar acertar o número sorteado pelo computador: "))
        contador += 1
        if chute == numerosecreto:
            print("Você acertou!")
            break
    else:
        print("Acabaram suas chances")