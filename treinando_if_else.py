name = input("Digite seu nome para começar: ")
print("Olá ", name)

age = int(input("Digite agora a sua idade: "))
print("Legal, ", name,  ". Parece que você tem ", age, " anos.")

if age >=0 and age <= 15:
    print("Sai da tela e vai brincar")
elif age > 10 and age <= 16:
    print("Você é um pré-adolescente")
elif age > 16 and age <= 21:
    print("Você é um adolescente")
elif age > 21 and age < 25:
    print("Você é um adulto na faculdade")
else:
    print("Você precisa arrumar um emprego")