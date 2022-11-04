def verifica_divisibilidade_por_3(n):
    return n % 3 == 0

def verifica_divisibilidade_por_5(n):
    return n % 5 == 0


def fizzbuzz(n):
    devolve = ""
    if verifica_divisibilidade_por_3(n) and not verifica_divisibilidade_por_5(n):
        devolve = "Fizz"
    elif not verifica_divisibilidade_por_3(n) and verifica_divisibilidade_por_5(n):
        devolve = "Buzz"
    elif verifica_divisibilidade_por_3(n) and verifica_divisibilidade_por_5(n):
        devolve = "FizzBuzz"
    else:
        devolve = n
    return devolve
