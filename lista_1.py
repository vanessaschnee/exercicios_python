lista = [1,2,3,4,5]

lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(10)

print(lista)
print(lista[6],lista[8])

lista.remove(3)
print(lista)

convidados = ['Vitor', 'Vanessa', 'Marcelo', 'Carol']
if 'Vitor' in convidados:
    print('Pode entrar.')
else:
    print('Não é um convidado.')

valores = [1,2,3,4,'Vanessa','True','Vitor','False']
print(len(valores))

rj= []
sp= []
mg= []
es= []

estados = [rj,sp,mg,es]

rj.extend(['São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu', 'Niterói', 'Belford Roxo'])
sp.extend(['São Paulo','Guarulhos','Campinas','São Bernardo do Campo','São José dos Campos','Santo André'])
mg.extend(['Uberlândia','Contagem','Juiz de Fora','Betim','Montes Carlos'])
es.extend(['Serra','Vila Velha','Cariacica','Vitória','Cachoeiro de Itapemirim'])

print(f'ESTADO: Rio de Janeiro\n',
      f'{estados[0]}',
      f'\nESTADO: São Paulo\n',
      f'{estados[1]}',
      f'\nESTADO: Minas Gerais\n',
      f'{estados[2]}',
      f'\nESTADO: Espírito Santo\n',
      f'{estados[3]}')

