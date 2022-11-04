def primo(x):
    m = 2
    while x % m != 0 and m <= x/2:
        m = m + 1
    if x % m == 0 and x > 2 or x == 0:
        return False
    else:
        return True

n = 999

while n > 0:
    n = int(input("Digite um número inteiro: "))
    if primo(n):
        print("primo")
    else:
        print("naõ primo")
