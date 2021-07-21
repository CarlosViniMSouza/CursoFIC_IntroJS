def fatorial(n):
    if (n < 0):
        raise ValueError("Entrada nao pode ser menor que 0.")

    if(type(n) == float):
        raise ValueError("Entrada nao pode ser decimal.")

    if (n > 1):
        fat = 1
        for i in range(1, n+1):
            fat = fat * i
        return fat
    return 1