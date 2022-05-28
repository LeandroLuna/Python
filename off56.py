x = float(input('Informe um numero real: '))

if x > 0:
    y = pow(x, 0.5)
    print(f'Raiz quadrada: {(y):.2f}')
else:
    z = pow(x, 2)
    print(f'Elevado ao quadrado: {(z):.2f}')
