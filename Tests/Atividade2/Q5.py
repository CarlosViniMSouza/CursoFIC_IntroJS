"""
5. Escrever uma função que calcule os sucessivos valores de E usando a série
abaixo e considerando primeiro 3 termos, depois 4 termos e, por fim, 5
termos: 

E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / 4!
"""

def fatorial_inv(n):

    if (n > 1):
        fat = 1
        fracao = 0
        soma = 0
        for i in range(1, n + 1):
            fat = fat * i
            fracao += 1/fat

        soma = 1 + fracao
    return print(soma)
        

fatorial_inv(6)