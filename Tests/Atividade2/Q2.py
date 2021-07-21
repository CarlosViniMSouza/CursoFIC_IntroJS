"""
2. Elabore uma função que dada a idade de um nadador classifica-o em uma
das seguintes categorias:

    infantil A = 5 - 7 anos
    infantil B = 8 - 10 anos
    juvenil A = 11 - 13 anos
    juvenil B = 14 - 17 anos
    adulto = maiores de 18 anos
"""

# id = int(input("Qual a sua idade?: "))

def categoria(id):
    # code here:
    if (id >= 5 and id <= 7):
        return "Categoria: infantil A"
    elif (id >= 8 and id <= 10):
        return "Categoria: infantil B"
    elif (id >= 11 and id <= 13):
        return "Categoria: juvenil A"
    elif (id >= 14 and id <= 17):
        return "Categoria: juvenil B"
    else:
        return "Sem categoria! Não pode competir"

# categoria(id)