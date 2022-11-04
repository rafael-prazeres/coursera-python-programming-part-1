n = int(input("Digite o primeiro número inteiro (ou zero para sair): "))
sair = 0
sequencia = []
while n != sair:
    sequencia.append(n)
    n = int(input("Digite o próximo número inteiro (ou zero para sair): "))

indice = len(sequencia) -1
while indice > -1:
    print(sequencia[indice],end=' ')
    indice = indice - 1
