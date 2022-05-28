num = int(input('Informe um número inteiro e positivo: '))


def par_ou_impar(num):
    test = num % 2
    return test


if par_ou_impar(num) == 0:
    print('Numero par!')
else:
    print('Numero impar!')
