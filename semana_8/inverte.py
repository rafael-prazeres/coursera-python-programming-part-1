lista = []
n = int(input("Digite um número: "))
while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))
print()
for i in range(len(lista)-1,-1,-1):
    print (lista[i])
