def maximo(x,y,z):
    if x >= y and y >= z:
        return x
    elif y >= x and x >= z:
        return y
    else:
        return z
