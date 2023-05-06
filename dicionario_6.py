carros = {'Toyota': 'R$146.890,00','Volkswagen':'R$78.160,00','Hyundai':'R$79.490,00','General Motors':'R$82.490,00','Ford':'R$69.230,00,00'}

carros['Honda'] = 'R$R$75.300,00'

for chave, valor in carros.items():
    print(chave,valor)

del carros['Volkswagen']

for chave, valor in carros.items():
    print()
    print(chave,valor)