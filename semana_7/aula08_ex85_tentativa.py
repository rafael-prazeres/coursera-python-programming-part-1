def main():

    m = int(input("Digite um número inteiro positivo (ou 0 para sair): "))
    n = 0
    
    while n < m and m != 0:
        
        n = n + 1
        soma_impares = 0
        contador_impares = 0
        termo_impar_referencia = 1
        saida = str(n) + "**3 = "
        
        while soma_impares < n**3:

            termo_impar_candidato = termo_impar_referencia
            
            while contador_impares < n:
                
                contador_impares = contador_impares + 1
                soma_impares = soma_impares + termo_impar_candidato
                
                if contador_impares > 1:
                    saida = saida + " + " + str(termo_impar_candidato)
                else:
                    saida = saida + str(termo_impar_candidato)

                termo_impar_candidato = termo_impar_candidato + 2

            if soma_impares < n**3:

                contador_impares = 0
                soma_impares = 0
                termo_impar_referencia = termo_impar_referencia + 2
                saida = str(n) + "**3 = "

        print(saida)
        if n == m:
            m = int(input("Digite um número inteiro positivo (ou 0 para sair): "))
            n = 0

main()
