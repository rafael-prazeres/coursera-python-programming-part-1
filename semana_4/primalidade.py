x = int(input("Digite um número inteiro: "))

primo = False

qtd_divisores = 0

divisor = 1

while divisor <= x:
    if x % divisor == 0:
        qtd_divisores = qtd_divisores + 1
    divisor = divisor + 1
    if qtd_divisores > 2:
        break

if qtd_divisores == 2:
    primo = True

if primo:
    print("primo")
else:
    print("não primo")
