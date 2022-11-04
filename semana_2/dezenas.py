x = int(input("Digite um número inteiro: "))

dd = x % 100

if dd < 10:
    dd = 0
else:
    dd = dd // 10

print("O dígito das dezenas é", dd)
