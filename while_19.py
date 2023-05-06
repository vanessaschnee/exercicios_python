numerousuario = int(input('Digite um número: '))
lista = []

while numerousuario >= 0:
    lista.append(numerousuario)
    numerousuario = int(input('Digite outro número: '))
else:
    media = sum(lista)/len(lista)
    print(f'Soma dos números digitados = {media}')