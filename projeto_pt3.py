print("Jogando caça ao número!")

dificuldade = int(input("Digite um número que represente o nível de dificuldade, onde- 1 é fácil e da 10 chances; 2 é "
                        "medio e da 6 chances; 3 é difícil e da 3 chances: "))

if dificuldade < 1 or dificuldade > 3:
    print("Opção inválida")
    exit(1)

if dificuldade == 1:
    chances = 10

elif dificuldade == 2:
    chances = 6

else:
    chances = 3

chute = int(input("Dê um palpite de 1 a 100 para tentar acertar o número sorteado pelo computador: "))

import random

numerosecreto = random.randint(1, 100)

contador = 2

while contador <= chances:
    if numerosecreto != chute:
        chute = int(input("Você errou! Dê outro palpite: "))
        contador += 1
    else:
        print("Você acertou! O número secreto era ",numerosecreto,". Fim do jogo.")
        break
else:
    print("Acabaram as chances! Fim de jogo.")
    print("O número secreto era ->",numerosecreto)







