p = float(input('Informe o preço antigo: '))

if p < 50.00:
    pn = p*1.05
    print(f'Preço com aumento de 5%: {(pn):.2f}')
elif p >= 50.00 and p <= 100.00:
    pn = p*1.10
    print(f'Preço com aumento de 10%: {(pn):.2f}')
else:
    pn = p*1.15
    print(f'Preço com aumento de 15%: {(pn):.2f}')

if pn < 80.00:
    print('Barato')
elif pn >= 80.00 and pn <= 120:
    print('Normal')
elif pn > 120.00 and pn <= 200:
    print('Normal')
else:
    print('Muito caro')
