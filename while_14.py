import random

numero1= random.randint(0,7)
numero2= random.randint(0,7)

resultado = numero1+numero2

while resultado != 7:
    print(f'O valor da soma dos números aleatórios é {resultado} ~diferente de 7~')
    numero1 = random.randint(0, 7)
    numero2 = random.randint(0, 7)
    resultado = numero1 + numero2
else:
    print(f'O valor da soma dos números aleatórios é {resultado}')



