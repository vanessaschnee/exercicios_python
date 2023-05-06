import random

lista = []

for i in range(1,11):
    numero = random.randint(1,100)
    lista.append(numero)

lista.sort()
print(lista)