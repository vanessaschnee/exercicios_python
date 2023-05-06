#adivinhação

import random

numero_aleatorio =(random.randint(1,10))

palpite =int(input("Jogo de Adivinhação! Digite um palpite: "))
tentativa =1

while palpite != numero_aleatorio:
    if palpite > numero_aleatorio:
        palpite = int(input("Você errou! Dica: O número que procura é menor que o seu palpite anterior. Tente novamente: "))
        tentativa +=1
    else:
        palpite = int(input("Você errou! Dica: O número que procura é maior que o seu palpite anterior. Tente novamente: "))
        tentativa +=1

if palpite == numero_aleatorio:
    print(f"Você acertou em {tentativa} tentativas")



