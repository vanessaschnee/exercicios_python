lista = []
i=0

while i < 10:
    numero = int(input("Digite um número para entrar na lista: "))
    lista.append(numero)
    i +=1

print(min(lista))
