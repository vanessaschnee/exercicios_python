dicionario = {}

for i in range (2):
    aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite o valor da nota na prova: '))
    dicionario[aluno] = nota

print(dicionario)
print(f'minimo do dicionário {min(dicionario.values())}')

chave_min = min(dicionario, key=dicionario.get)
print(f'chave min {chave_min}')