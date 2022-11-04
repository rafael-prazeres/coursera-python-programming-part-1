n = int(input("Digite o valor de n: "))
qtd_impares = 1
i = 0
while qtd_impares <= n:
    if i % 2 != 0:
        print(i)
        qtd_impares = qtd_impares + 1
    i = i + 1
