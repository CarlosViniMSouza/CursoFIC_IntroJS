"""
3. Tendo como dados de entrada a altura e o sexo de uma pessoa (M-
masculino e F-feminino), faça uma função que calcule seu peso ideal,

utilizando as seguintes fórmulas: 

(i) para homens: (72.7*h)-58

(ii) para mulheres: (62.1*h)-44.7.
"""

genero = input("Qual o seu sexo (M - masculino | F - feminino) ?: ")
h = float(input("Qual a sua altura?: "))

def peso(genero, h):
    # code here:
    peso_homens = round((72.7 * h) - 58)
    peso_mulheres = round((62.1 * h) - 44.7)

    if (genero == "M"):
        print(peso_homens)

    elif (genero == "F"):
        print(peso_mulheres)
    
    else:
        return "Erro!"

peso(genero, h)