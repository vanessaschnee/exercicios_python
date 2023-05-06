import array
import random

array = array.array('i')

for i in range(1,11):
    numero = random.randint(1,100)
    array.append(numero)

print(array)
print(array[4])