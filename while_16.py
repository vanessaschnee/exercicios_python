numerodousuario= int(input('Digite um número:'))
variaveltemporaria=0
soma=0

while numerodousuario != 0:
    variaveltemporaria = numerodousuario
    soma = soma + variaveltemporaria
    numerodousuario= int(input('Digite um número:'))

if numerodousuario == 0:
    print (soma)
