import array
import random

meuarray = array.array('i')
print(meuarray)

for i in range(1,11):
    numero = random.randint(0,100)
    meuarray.append(numero)
    print(meuarray)