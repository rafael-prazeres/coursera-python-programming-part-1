import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if (distancia >= 10):
    print("longe")
else:
    print("perto")
