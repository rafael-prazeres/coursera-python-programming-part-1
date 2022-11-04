# Introdução à Ciência da Computação com Python Parte 1 - Semana 5

# Algoritmo para construção do triângulo de pascal

# Autor: Rafael Prazeres - 24/04/2020

# função  principal
def main():
    '''
    Função principal, será a primeira a ser executado e
    será a responsável pela chamada de outras funções que
    por sua vez podem ou não chamar outras funçoes que
    por sua vez ...
    '''
    # corpo da função main

    n = int(input("Digite um número inteiro: ")) # número de linhas do triângulo de pascal
    print()
    print("Triângulo de Pascal:")
    print()
    imprimir_triangulo_pascal(n)
    print()
    print("Sequência de fibonacci obtida a partir das diagonais do Triângulo acima:")
    print()
    imprimir_fibonacci(n)

# Declaração das funções

def imprimir_fibonacci(n):

    # Fonte: http://www.educ.fc.ul.pt/icm/icm99/icm31/pascal.htm
    
    '''(int) -> int
    Recebe um inteiro n e imprime os n primeiros termos da sequência de Fibonacci calculados
    a partir da soma dos números binomiais que formam as diagonais do triângulo de pascal.
    Pre-condicao: supoe que n eh um numero inteiro nao negativo.
    '''

    iterador_avanco_diagonal = 0

    sequencia_fibonacci = ""

    while iterador_avanco_diagonal <= n:

        elemento_seq_fibonacci = 0

        denominador = 1

        diagonal_fibonacci = ""

        while (denominador - 1) <= iterador_avanco_diagonal - (denominador - 1) and iterador_avanco_diagonal - (denominador - 1) >= 0:

            k = denominador - 1

            numerador = iterador_avanco_diagonal - k

            numero_binomial_diagonal = numero_binomial(numerador, k)
            
            elemento_seq_fibonacci = elemento_seq_fibonacci + numero_binomial_diagonal

            diagonal_fibonacci = diagonal_fibonacci + str(numero_binomial_diagonal)

            if numerador - k > 1:

                diagonal_fibonacci = diagonal_fibonacci + " + "

            denominador = denominador + 1

        print(diagonal_fibonacci,"=", elemento_seq_fibonacci)

        sequencia_fibonacci = sequencia_fibonacci + str(elemento_seq_fibonacci) + " "

        iterador_avanco_diagonal = iterador_avanco_diagonal + 1

    print("\nSequência de Fibonacci:",sequencia_fibonacci)

def imprimir_triangulo_pascal(n):

    '''(int) -> int
    Recebe um inteiro n e imprime o triângulo de pascal com n linhas
    Pre-condicao: supoe que n eh um numero inteiro nao negativo.
    '''
    
    iterador_avanco_linha = 0 # indicador de avanço de linha para próxima linha na impressão do triângulo de pascal

    while iterador_avanco_linha <= n:

        iterador_expansao_linha = iterador_avanco_linha # numerador do coeficiente binomial

        coeficientes_linha = "" # armazena os coeficientes binomiais de uma linha do triângulo de pascal
        
        k = 0 # denominador do número binomial

        while k <= iterador_expansao_linha:

            coeficientes_linha = coeficientes_linha + str(numero_binomial(iterador_expansao_linha,k)) + " "
            k = k + 1
        
        print(coeficientes_linha)

        iterador_avanco_linha = iterador_avanco_linha + 1

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
