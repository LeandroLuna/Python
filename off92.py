fabrica = float(input('Informe o custo de fábrica: '))

if fabrica < 12.000:
    dist = fabrica*0.05
    imp = 'isento'
    print(
        f'Comissão do distribuidor é: {(dist):.2f}\nE os impostos são: {(imp)}')
elif fabrica >= 12.000 and fabrica <= 25.000:
    dist = fabrica*0.10
    imp = fabrica*0.15
    print(
        f'Comissão do distribuidor é: {(dist):.2f}\nE os impostos são: {(imp):.2f}')
elif fabrica > 25.000:
    dist = fabrica*0.15
    imp = fabrica*0.20
    print(
        f'Comissão do distribuidor é: {(dist):.2f}\nE os impostos são: {(imp):.2f}')
