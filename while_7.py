lista = []
i=0

while i < 10:
    ordem = str(i+1)
    numero = int(input("Digite o " + ordem + "° número para entrar na lista: "))
    lista.append(numero)
    i +=1

print(max(lista))