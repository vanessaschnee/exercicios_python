peso = float(input("Digite seu peso: "))

if peso <40:
    print("Você está abaixo do peso")

elif peso >= 40 and peso <= 60:
    print("Seu peso é normal")

elif peso>= 61 and peso<=80:
    print("Você está com sobrepeso")

else:
    print("Você está obeso")



