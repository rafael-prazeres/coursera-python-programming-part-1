n = int(input("Digite o valor de n: "))
fat = n

if n == 0:
    fat = 1
else:
    while n > 1:
        fat = fat * (n - 1)
        n = n - 1
print(fat)
