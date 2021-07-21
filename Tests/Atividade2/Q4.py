"""
4. Escrever uma função que recebe um conjunto de 4 valores, i, a, b, c, onde i é
um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva.
A seguir:

a) Se i=1 escrever os três valores a, b, c em ordem crescente.

b) Se i=2 escrever os três valores a, b, c em ordem decrescente.

c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c
fique dentre os dois.
"""

i = int(input("Digite um num inteiro: "))
a = float(input("Digite um num real: "))
b = float(input("Digite um num real: "))
c = float(input("Digite um num real: "))

lista = [a, b, c]

def conj(i, lista):
    #code here:
    if (i == 1):
        lista.sort()
        print(f"A ordem eh = {lista}")

    elif (i == 2):
        lista.reverse()
        print(f"A ordem eh = {lista}")

    elif (i == 3):
        if (lista[0] > lista[1] and lista[0] > lista[2]):
            print(f"A ordem eh = {lista[1], lista[0], lista[2]}")

        elif (lista[1] > lista[0] and lista[1] > lista[2]):
            print(f"A ordem eh = {lista[0], lista[1], lista[2]}]")

        else:
            print(f"A ordem eh = {lista[0], lista[2], lista[1]}")
    
    else:
        print("erro!")

conj(i, lista)
