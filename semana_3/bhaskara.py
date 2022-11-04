import math

a = float(input("Digite o coeficiente quadrático:"))
b = float(input("Digite o coeficiente linear:"))
c = float(input("Digite o coeficiente constante ou termo livre:"))

delta = b ** 2 - 4 * a * c
    
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        print("a raiz desta equação é", -b/(2*a))
    else:
        r1 = (-b + math.sqrt(delta))/(2 * a)
        r2 = (-b - math.sqrt(delta))/(2 * a)
        if r1 < r2:
            print("as raízes da equação são",r1,"e",r2)
        else:
            print("as raízes da equação são",r2,"e",r1)
