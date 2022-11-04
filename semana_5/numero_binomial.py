#Fontes:
        # https://www.cin.ufpe.br/~gdcc/matdis/aulas/binomial
        # somatematica.com.br/emedio/binomio/binomio1.php
        # https://pt.wikipedia.org/wiki/Coeficiente_binomial
        # https://www.youtube.com/watch?v=2-ctEASuKSY (NUMEROS BINOMIAIS TRIANGULO PASCAL-PROF.CHUCK)

def fatorial(n):
    fat = n
    if n == 0:
        fat = 1
    else:
        while n > 1:
            fat = fat * (n - 1)
            n = n - 1
    return fat

def numero_binomial(n,k):
    return fatorial(n)//(fatorial(k)*fatorial(n-k))

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

       
def testa_numero_binomial(n,k):

    if validar_numerador_denominador_coeficiente_binomial(n,k):
        
        if validar_propriedade_coeficientes_binomiais_complementares(n,k):
            print("Passou no teste de coeficientes binomiais complementares, uma vez que numero_binomial(",n,",",k,") == numero_binomial(",n,",",n-k,") == ", numero_binomial(n,k))
        else:
            print("Não passou no teste de coeficientes binomiais complementares")

        if validar_relacao_stifel(n,k):
            
            if k > 0 and k != n:
                print("Passou no teste da Relação de Stifel, uma vez que numero_binomial(",n,",",k,") == numero_binomial(",n-1,",",k-1,") + numero_binomial(",n-1,",",k,") == ", numero_binomial(n,k))
            elif k == n == 0:
                print("Passou no teste da Relação de Stifel, pois não existem coeficientes binomiais acima do coeficiente binomial informado, uma vez que o mesmo está na primeira linha do Triângulo de Pascal")
            elif k == 0:
                print("Passou no teste da Relação de Stifel, pois o primeiro coeficiente binomial de uma linha do Triângulo de Pascal possui apenas um coeficiente binomial acima dele (do lado direito), que é o número", numero_binomial(n-1,k))
            elif k == n:
                print("Passou no teste da Relação de Stifel, pois o último coeficiente binomial de uma linha do Triângulo de Pascal possui apenas um coeficiente binomial acima dele (do lado esquerdo), que é o número", numero_binomial(n-1,k-1))
            
        else:
            print("Não passou no teste da Relação de Stifel")

        if n == k:
            print("Teste da Regra da Diagonal do Triângulo de Pascal não se aplica quando o numerador e o denominador do coeficiente binomial são iguais")
        elif validar_regra_diagonal_triangulo_pascal(n,k):
            print("Passou no teste da Regra da Diagonal do Triângulo de Pascal")
        else:
            print("Não passou no teste da Regra da Diagonal do Triângulo de Pascal")

        if validar_soma_coeficientes_binomiais_mesma_linha(n):
            print("Passou no teste da soma dos coeficientes binomiais da n-ésima linha do Triângulo de pascal")
        else:
            print("Não passou no teste da soma dos coeficientes binomiais da n-ésima linha do Triângulo de pascal")

    else:

        print("Não passou no teste. Número binomial inválido. n e k devem ser números naturais e n deve ser maior ou igual a k.")


def validar_relacao_stifel(n,k):
    if k > 0 and k != n:
        return numero_binomial(n,k) == numero_binomial(n-1,k-1) + numero_binomial(n-1,k)
    elif k == n == 0:
        return True #Não existem linhas acima no Triângulo de Pascal
    elif k == 0:
        return numero_binomial(n,k) == 0 + numero_binomial(n-1,k) # Não existe coeficiente binomial na linha acima à esquerda
    elif k == n:
        return numero_binomial(n,k) == numero_binomial(n-1,k-1) + 0 # Não existe coeficiente binomial na linha acima à direita
        
def validar_numerador_denominador_coeficiente_binomial(n,k):
    return n >= k and n >= 0 and k >= 0

def validar_propriedade_coeficientes_binomiais_complementares(n,k):
    return numero_binomial(n,k) == numero_binomial(n,n-k)

def validar_regra_diagonal_triangulo_pascal(n,k):

    resultado = False
    soma_diagonal = 0
    numerador = n
    denominador = k
    
    while denominador >= 0:
        numerador = numerador - 1
        soma_diagonal = soma_diagonal + numero_binomial(numerador,denominador)
        #print("numero_binomial(",numerador,",",denominador,")")
        denominador = denominador - 1

    #print(soma_diagonal)
    
    if numero_binomial(n,k) == soma_diagonal:
        resultado = True
    
    return resultado

def validar_soma_coeficientes_binomiais_mesma_linha(n):

    k = 0
    soma_coeficientes_binomiais = 0
    resultado = False

    while k <= n:
        soma_coeficientes_binomiais = soma_coeficientes_binomiais + numero_binomial(n,k)
        k = k + 1

    #print(soma_coeficientes_binomiais)
    
    if soma_coeficientes_binomiais == (2 ** n):
        resultado = True

    return resultado
