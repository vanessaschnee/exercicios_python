def funcaoSemParametros():
    print("Eu sou uma função sem parametro e não retorno nada")

def funcaoComParametrosQueRetornaSoma(num1, num2):
    soma = num1 + num2
    return soma

funcaoSemParametros()
meuNovoValor = funcaoComParametrosQueRetornaSoma(2,2)
print(meuNovoValor)