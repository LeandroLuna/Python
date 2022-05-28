a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

delta = pow((b ^ 2.0)-(4.0*a*c), 0.5)
raiz1 = (-b+delta)/2.0*a
raiz2 = (-b-delta)/2.0*a

if a == 0:
    print('O valor de "a" tem que ser diferente de 0.')
else:
    if delta < 0:
        print('Nao existe raiz')
    elif delta == 0:
        print(f'Raiz unica:\nRaiz+: {(raiz1)}\nRaiz-: {(raiz2)} ')
    elif delta >= 0:
        print(f'As raizes são:\nRaiz+: {(raiz1)}\nRaiz-: {(raiz2)} ')
