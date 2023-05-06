#Escreva um programa que crie um dicionário com as informações de cinco pessoas (nome, idade, cidade e profissão).
# Em seguida, exiba as informações das pessoas que moram na mesma cidade.


cadastros = []

for i in range(3):
    dicionario1 = {}
    nome = input('Digite um nome:')
    idade = int(input('Digite a idade: '))
    cidade = input('Digite a cidade em que essa pessoa mora: ')
    dicionario1['Nome'] = nome
    dicionario1['Idade'] = idade
    dicionario1['Cidade'] = cidade
    cadastros.append(dicionario1)

cidades = {}

for cadastro in cadastros:
    cidades[cadastro['Cidade']] = []

for cadastro in cadastros:
    cidades[cadastro['Cidade']].append(cadastro['Nome'])

print(cidades)

[p for p in pessoas if p['cidade'] == cidade]

for p in pessoas:
    if(p['cidade'] == cidade):

