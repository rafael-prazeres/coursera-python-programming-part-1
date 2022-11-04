x = int(input("Digite um número inteiro: "))
soma = 0
x_restante = x

while x_restante // 10 > 0 or x_restante % 10 > 0:
    soma = soma + x_restante % 10
    x_restante = x_restante // 10

print(soma)
