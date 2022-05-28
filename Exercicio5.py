letra = str(input('Informe uma letra: '))


# Condicional se letra é maiuscula. Retorna 'true' or 'false' para o if.
def index(letra):
    if letra.isupper():
        return 'Sua letra é maiuscula!'
    else:
        return 'Sua letra é minuscula!'


print(index(letra))
