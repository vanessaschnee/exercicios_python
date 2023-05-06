import random

lista = []
listamaiorquemedia = []

for i in range (1,11):
    numero = random.randint(0,100)
    lista.append(numero)

media = sum(lista) / len(lista)
print(lista)
print(media)

for i in lista:
    if i > media:
        numero2 = i
        listamaiorquemedia.append(numero2)

print(listamaiorquemedia)