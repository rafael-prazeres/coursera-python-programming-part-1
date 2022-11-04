import math

def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c

def calcular_raiz_v1(a, b, c, opcao_escolhida):
    '''Recebe como argumentos os coeficiêntes da equação
       e uma opção (0 - calcular raíz quando delta vale 0,
       1 - calcular x' e 2 - calcular x'')'''
    opcao_calcular_quando_delta_zero = 0
    opcao_calcular_x_linha = 1
    opcao_calcular_x_duas_linhas = 2
    if opcao_escolhida == opcao_calcular_quando_delta_zero:
        raiz = -b/(2*a)
    elif opcao_escolhida == opcao_calcular_x_linha:
        raiz = (-b + math.sqrt(calcular_delta(a,b,c)))/(2 * a)
    elif opcao_escolhida == opcao_calcular_x_duas_linhas:
        raiz = (-b - math.sqrt(calcular_delta(a,b,c)))/(2 * a)
    return raiz

def calcular_raiz_v2(a, b, c, delta, opcao_escolhida):
    '''Recebe como argumentos os coeficiêntes da equação, o valor de delta
       e uma opção (0 - calcular raíz quando delta vale 0,
       1 - calcular x' e 2 - calcular x'')'''
    opcao_calcular_quando_delta_zero = 0
    opcao_calcular_x_linha = 1
    opcao_calcular_x_duas_linhas = 2
    if opcao_escolhida == opcao_calcular_quando_delta_zero and delta == 0:
        raiz = -b/(2*a)
    elif opcao_escolhida == opcao_calcular_x_linha:
        raiz = (-b + math.sqrt(delta))/(2 * a)
    elif opcao_escolhida == opcao_calcular_x_duas_linhas:
        raiz = (-b - math.sqrt(delta))/(2 * a)
    return raiz

def imprimir_raizes_ordem_crescente(a, b, c):
    delta = calcular_delta(a,b,c)
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        opcao_calcular_quando_delta_zero = 0
        opcao_calcular_x_linha = 1
        opcao_calcular_x_duas_linhas = 2
        if delta == 0:
            #print("a raiz desta equação é", calcular_raiz_v1(a, b, c, opcao_calcular_quando_delta_zero))
            print("a raiz desta equação é", calcular_raiz_v2(a, b, c, delta, opcao_calcular_quando_delta_zero))
        else:
            #r1 = calcular_raiz_v1(a, b, c, opcao_calcular_x_linha)
            r1 = calcular_raiz_v2(a, b, c, delta, opcao_calcular_x_linha)
            #r2 = calcular_raiz_v1(a, b, c, opcao_calcular_x_duas_linhas)
            r2 = calcular_raiz_v2(a, b, c, delta, opcao_calcular_x_duas_linhas)
            if r1 < r2:
                print("as raízes da equação são",r1,"e",r2)
            else:
                print("as raízes da equação são",r2,"e",r1)

def main():
    a_digitado = float(input("Digite o coeficiente quadrático:"))
    b_digitado = float(input("Digite o coeficiente linear:"))
    c_digitado = float(input("Digite o coeficiente constante ou termo livre:"))
    imprimir_raizes_ordem_crescente(a_digitado, b_digitado, c_digitado)

main()
