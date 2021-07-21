"""
3. Tendo como dados de entrada a altura e o sexo de uma pessoa (M-
masculino e F-feminino), faça uma função que calcule seu peso ideal,

utilizando as seguintes fórmulas:

(i) para homens: (72.7*h)-58

(ii) para mulheres: (62.1*h)-44.7.
"""

# genero = input("Qual o seu sexo (M - masculino | F - feminino) ?: ")
# h = float(input("Qual a sua altura?: "))

def peso(genero, h):
    # code here:
    if (genero == "M"):
        peso_M = round((72.7 * h) - 58)
        return peso_M

    elif (genero == "F"):
        peso_F = round((62.1 * h) - 44.7)
        return peso_F

    else:
        return "Erro!"

peso("M", 1.8)
peso("F", 1.8)
