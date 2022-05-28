import math
x = int(input("Informe um numero inteiro: "))

if x < 0:
    print('Numero invalido: Informe um numero positivo.')
else:
    print(f'Logaritmo natural é {(math.log(x))}')
