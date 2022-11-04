def verifica_primalidade(n):
    
    primo = False

    qtd_divisores = 0

    divisor = 1

    while divisor <= n:
        if n % divisor == 0:
            qtd_divisores = qtd_divisores + 1
        divisor = divisor + 1
        if qtd_divisores > 2:
            break

    if qtd_divisores == 2:
        primo = True

    return primo


def maior_primo(n):
    x = n
    while x >= 2:
        if verifica_primalidade(x):
            break
        else:
            x = x -1
    return x
