x = float(input('Informe um numero positivo: '))

if x > 0:
    print(f'Ao quadrado: {(pow(x, 2.0))}')
    print(f'Raiz quadrada: {(pow(x, 0.5)):.2f}')
else:
    print('Numero invalido.')
