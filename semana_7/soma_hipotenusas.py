def e_hipotenusa_primeira_tentativa(a):
    resposta = False
    b = a - 1
    c = 1
    while b >= 1:
        while c <= a - 1:
            if a**2 == b**2 + c**2:
                resposta = True
                break
            c = c + 1
        if resposta:
            break
        b = b - 1
        c = 1
    return resposta

def soma_hipotenusas(n):
    soma = 0
    hip = 1
    while hip <= n:
        if e_hipotenusa_primeira_tentativa(hip):
            soma = soma + hip
        hip = hip + 1
    return soma
