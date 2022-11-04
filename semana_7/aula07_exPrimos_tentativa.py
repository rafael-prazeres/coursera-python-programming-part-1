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
    
    qtd_primos = 0
    n = int(input("Digite o primeiro número da sequência: "))

    while n != 0:
        if n == 1:
            print("Número inválido. Informe um número maior que um.")
        elif éPrimo(n):
            qtd_primos = qtd_primos + 1
        if qtd_primos == 0:
            n = int(input("Digite o primeiro número da sequência: "))
        else:
            n = int(input("Digite o próximo número da sequência: "))
        
    print(qtd_primos)

main()
