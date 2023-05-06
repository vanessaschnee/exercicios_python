resposta = input("Deseja calcular IMC?")
quantidadesCalculadas = 0

while resposta == "sim":
    quantidadesCalculadas += 1
    print("Fingindo que calculei a", quantidadesCalculadas, "° vez")
    resposta = input("Deseja calcular o IMC de novo?")

print("Obrigado por usar nosso programa")
