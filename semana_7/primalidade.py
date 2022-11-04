# Fontes:
# https://www.somatematica.com.br/fundam/primos.php
# https://www.matematica.pt/faq/numero-primo.php

def éPrimo(x):
    fator = 2
    while x % fator != 0 and fator <= x // fator:
    #while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0 and x > 2 or x == 1:
        primo = False
    else:
        primo = True
    return primo

def main():
    n = int(input("Digite um número inteiro: "))
    while n > 0:
        if éPrimo(n):
            print(n, "é primo!")
        else:
            print(n, "naõ é primo :-(")
        n = int(input("Digite um número inteiro: "))

main()
