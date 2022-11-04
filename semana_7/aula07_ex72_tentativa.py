# Fonte: https://www.somatematica.com.br/fundam/mdc.php
# Cálculo do M.D.C pelo processo das divisões sucessivas

def func_mdc(a,b):
    if a > b:
        dividendo = a
        divisor = b
    else:
        dividendo = b
        divisor = a
    while dividendo % divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto
    return divisor
    
def main():
    n = int(input("Informe o tamanho da sequencia: "))
    i = 1
    while i <= n:
        termo_atual = input("Informe o "+ str(i) +"o termo da sequencia: ")
        termo_atual = int(termo_atual)
        if i > 1:
            mdc = func_mdc(mdc,termo_atual)
        else:
            mdc = termo_atual
        i = i + 1
    print(mdc)

main()
