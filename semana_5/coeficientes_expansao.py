#https://panda.ime.usp.br/aulasPython/static/aulasPython/aula06.html

# Exercício 6.4
# Usando as funções dos exercícios 6.2 (fatorial )e 6.3 (numero_binomial),
# escreva um programa que lê um inteiro n, n >= 0 e imprime os coeficientes
# da expansão de (x+y) elevado a n.

# função  principal
def main():
    '''
    Função principal, será a primeira a ser executado e
    será a responsável pela chamada de outras funções que
    por sua vez podem ou não chamar outras funçoes que
    por sua vez ...
    '''
    # corpo da função main

    n = int(input("Digite um número inteiro:")) # numerador do número binomial

    k = 0 # denominador do número binomial

    iterador_expansao = n

    while iterador_expansao >= 0:

        print("O",k+1,"º coeficiente da expansão é", numero_binomial(n,k))
        iterador_expansao = iterador_expansao - 1
        k = k + 1

# Declaração das funções

def fatorial(n):
    '''(int) -> int
    Recebe um inteiro n e retorna o valor de n!
    Pre-condicao: supoe que n eh um numero inteiro nao negativo.
    '''
    # corpo da função fatorial
    fat = n
    if n == 0:
        fat = 1
    else:
        while n > 1:
            fat = fat * (n - 1)
            n = n - 1
    return fat

def numero_binomial(n,k):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''
    # corpo da função numero_binomial
    return fatorial(n)//(fatorial(k)*fatorial(n-k))

# início da execução do programa
main() # chamada da função main
