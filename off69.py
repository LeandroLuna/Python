x = float(input('Informe a base maior: '))
y = float(input('Informe a base menor: '))
z = float(input('Informe a altura: '))
if x > 0.00:
    maior = x
else:
    print('Valor da base maior invalido.')
if y > 0.00:
    menor = y
else:
    print('Valor da base menor invalido.')
if z > 0.00:
    h = z
else:
    print('Valor da altura invalido.')

A = ((maior+menor)*h)/2
print(f'A area do trapezio é de: {(A):.2f}')
