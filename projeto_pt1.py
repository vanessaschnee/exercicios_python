#Crie um programa em python que:

#- logo no seu início imprima a mensagem: jogando caça ao número.
#- solicite ao usuário para digitar um número que represente o nível de dificuldade, onde: 1 é fácil e da 10 chances; 2 é medio e da 6 chances; 3 é difícil e da 3 chances.
#- crie uma variável que inicializa o número a ser descoberto. Você pode iniciar essa variável com o valor 42 e depois mudaremos isso para algo automático.
#- solicite ao usuário um chute e armazene o chute.

print("Jogando caça ao número!")

dificuldade = int(input("Digite um número que represente o nível de dificuldade, onde- 1 é fácil e da 10 chances; 2 é "
                        "medio e da 6 chances; 3 é difícil e da 3 chances: "))
numerosecreto = 42

if dificuldade < 1 or dificuldade > 3:
    print("Opção inválida")
    exit(1)

if dificuldade == 1:
    chances = 10
elif dificuldade == 2:
    chances = 6
else:
    chances = 3

chute = int(input("Agora, dê um palpite para tentar acertar o número sorteado pelo computador: "))



