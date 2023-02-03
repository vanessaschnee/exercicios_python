idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você não pode entrar")

elif idade == 18:
    print("Esse é o primeiro ano em que você pode entrar")

else:
    print("Você pode entrar")