rj= []
sp= []
mg= []
es= []

estados = {"Rio de Janeiro":rj,"São Paulo":sp,"Minas Gerais":mg,"Espírito Santo":es}

rj.extend(['São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu', 'Niterói', 'Belford Roxo'])
sp.extend(['São Paulo','Guarulhos','Campinas','São Bernardo do Campo','São José dos Campos','Santo André'])
mg.extend(['Uberlândia','Contagem','Juiz de Fora','Betim','Montes Carlos'])
es.extend(['Serra','Vila Velha','Cariacica','Vitória','Cachoeiro de Itapemirim'])

for estado, cidades in estados.items():
    print(f'ESTADO:{estado}')
    for cidade in cidades:
            print(cidade)
    print(f'\n')