def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial*n
        n = n -1
    return fatorial

    
def main():
    n = n = int(input("Digite um número inteiro positivo: "))
    while (n >= 0):
        print(fatorial(n))
        n = int(input("Digite um número inteiro positivo: "))

main()
