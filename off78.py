km = float(input('Kilometros rodados: '))
gas = float(input('Gasosa consumida: '))

economia = km/gas

if economia <= 8.00:
    print('Venda o carro.')
elif economia >= 8.00 and economia <= 14.00:
    print('Econômico.')
elif economia > 14.00:
    print('Super Econômico.')
else:
    pass
