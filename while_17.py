nomeusuario = input('Digite um nome: ')
lista =[]

while nomeusuario != 'fim':
    lista.append(nomeusuario)
    nomeusuario = input('Digite outro nome: ')
else:
    print(f'Quantidade de nomes digitados ={len(lista)}')
    listaordenada = sorted(lista)
    print(f'Nomes em ordem alfabética: {listaordenada}')