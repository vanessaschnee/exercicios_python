numerousuario = int(input('Digite um número: '))
count = 1
soma = 0
soma = numerousuario + soma

while soma <= 100:
    numerousuario = int(input('Digite um número: '))
    soma = numerousuario + soma
    count += 1
else:
    print(f'Quantidade de números digitados= {count}')
    print(f'Soma dos números digitados = {soma}')


