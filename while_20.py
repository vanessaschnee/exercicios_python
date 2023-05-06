#Crie um programa que peça ao usuário para digitar um número.
# O programa deve imprimir a tabuada desse número até 10 usando um loop while.
# Em seguida, o programa deve pedir ao usuário para digitar outro número, e repetir o processo até que o usuário digite o número zero.

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    numero = int(input('Digite um número para calcularmos a tabuada: '))
    i=0

    while i < len(tabuada):
        resultado = tabuada[i] * numero
        print(resultado)
        i += 1

