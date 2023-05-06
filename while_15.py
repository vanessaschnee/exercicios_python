import random

while True:
    numero1= random.randint(0,7)
    numero2= random.randint(0,7)
    resultado = numero1+numero2

    if resultado ==7:
        print(f'O valor da soma dos números aleatórios é {resultado}')
        break
    else:
        print(f'O valor da soma dos números aleatórios é {resultado}')
