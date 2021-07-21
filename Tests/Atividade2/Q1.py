"""
1. Elaborar uma função que recebe dois valores, 'a' e 'b' como parâmetros, e os
escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".
"""

# a = int(input("Digite um numero: "))
# b = int(input("Digite outro numero: "))

def multiplos(a, b):
    # code here:
    if (a % b == 0):
        return True
    else:
        return False

# multiplos(a, b)