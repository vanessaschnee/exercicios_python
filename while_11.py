numero = int(input('Digite um número: '))
numerofinal = 0

while numero != 0:
    numerofinal = numero + numerofinal
    numero = int(input('Digite outro número: '))
else:
    print(numerofinal)
