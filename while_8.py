lista = []
i=0
pares=0

while i < 10:
    ordem = str(i+1)
    numero = int(input("Digite o " + ordem + "° número para entrar na lista: "))
    lista.append(numero)

    if numero % 2 == 0:
        pares +=1

    i +=1

print(pares)