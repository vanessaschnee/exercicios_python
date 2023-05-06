name = input ("Me fala seu nome: ")
print ("Olá, ", name,". Vamos calcular seu IMC.")
preparado = input ("Preparado?")

if preparado == "sim":
    print ("Então vamos lá!")
elif preparado =="não":
    print ("As vezes a verdade dói, eu entendo. Te vejo na próxima")
else :
    print ("digite sim ou não quando chegar nessa pergunta novamente.")

altura = float(input ("Quanto você tem de altura? "))
peso = float(input ("Qual seu peso? "))

imc = round( peso / (altura * altura), 2)
print ("Seu IMC é: ", imc)

if imc < 18.50:
    print("Você está abaixo do Peso")
elif imc >= 18.50 and imc <= 24.90 :
    print ("Você está no peso normal")
elif imc >= 25 and imc <= 29.9 :
    print ("Você está com sobrepeso")
else :
    print ("Você está com obesidade em algum grau")