def remove_repetidos(lista):
    lista_sem_numeros_repetidos = []
    for num in lista:
        if num not in lista_sem_numeros_repetidos:
            lista_sem_numeros_repetidos.append(num)
    return sorted(lista_sem_numeros_repetidos)
