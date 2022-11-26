def minmax(numero: int, minimo: int, maximo: int) -> int:
    '''
    "Encierra" un valor entre un mínimo y un máximo.
    '''
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero
