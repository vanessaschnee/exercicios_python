import array
import random

meuarray = array.array('i')
meuoutroarray = array.array('i')

for i in range(1,11):
    numero = random.randint(0,100)
    meuarray.append(numero)
    print(meuarray)
    if numero % 2 ==1:
        meuoutroarray.append(numero)

print(f'Meu array {meuarray}')
print(f'Array que só mostra os ímpares {meuoutroarray}')