# Escreva um programa que crie um dicionário com os nomes e as idades de cinco pessoas.
# Em seguida, exiba o nome da pessoa mais velha.

dicionario = {}

for i in range (5):
    dados_nome = input("Digite um nome: ")
    dados_idade = int(input("Digite uma idade: "))
    dicionario[dados_nome] = dados_idade

print(max(dicionario))

