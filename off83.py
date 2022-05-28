peso = float(input('Informe seu peso: '))
h = float(input('Informe sua altura: '))

if h < 1.20:
    if peso < 60.00:
        print('Classificação: A')
    elif peso >= 60.00 and peso <= 90.00:
        print('Classificação: D')
    else:
        print('Classificação: G')
elif h >= 1.20 and h <= 1.70:
    if peso < 60.00:
        print('Classificação: B')
    elif peso >= 60.00 and peso <= 90.00:
        print('Classificação: E')
    else:
        print('Classificação: H')
else:
    if peso < 60.00:
        print('Classificação: C')
    elif peso >= 60.00 and peso <= 90.00:
        print('Classificação: F')
    else:
        print('Classificação: I')
