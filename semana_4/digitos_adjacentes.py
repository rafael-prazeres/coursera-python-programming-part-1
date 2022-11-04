x = int(input("Digite um número inteiro: "))

digito_referencia = x % 10

x_digitos_restantes = x // 10

proximo_digito = x_digitos_restantes % 10

x_possui_digitos_iguais = False

igualdade_ultimo_passo = False

while x // 10 > 0:
    digito_referencia = x % 10
    x_digitos_restantes = x // 10
    proximo_digito = x_digitos_restantes % 10
    if digito_referencia == proximo_digito and not igualdade_ultimo_passo:
        x_possui_digitos_iguais = True
        igualdade_ultimo_passo = True
        #print("Dígito repetido", proximo_digito)
        #break
    else:
        igualdade_ultimo_passo = False
    x = x_digitos_restantes

if x_possui_digitos_iguais:
    print("sim")
else :
    print("não")
