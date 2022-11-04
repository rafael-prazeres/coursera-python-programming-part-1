# Fontes:
# https://www.somatematica.com.br/fundam/primos.php
# https://www.matematica.pt/faq/numero-primo.php

def e_primo(x):
    fator = 2
    #while x % fator != 0 and fator <= x/2:
    while x % fator != 0 and fator <= x // fator:
        fator = fator + 1
    if x % fator == 0 and x > 2 or x == 1:
        primo = False
    else:
        primo = True
    return primo

def n_primos(x):
    qtd_primos = 0
    while x >= 2:
        if e_primo(x):
            qtd_primos = qtd_primos + 1
        x = x - 1
    return qtd_primos

def main():
    n = int(input("Digite um número inteiro positivo >= 2: "))
    while n > 0:
        print(n_primos(n))
        n = int(input("Digite um número inteiro: "))

#main()
