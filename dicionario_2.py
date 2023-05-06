dicionario = {}
dicionario['Aluno'] = 'Matheus'
notaacumulada = 0

for i in range(5):
    materia = input('Digite o nome da matéria: ')
    nota = float(input('Digite a nota: '))
    notaacumulada = notaacumulada + nota
    dicionario[materia] = nota


print(dicionario)
print(f'nota acumulada  {notaacumulada}')
print(f'tamanho dicionário {len(dicionario)}')
print(notaacumulada/(len(dicionario)-1))
