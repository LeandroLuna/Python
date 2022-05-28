valor = float(input('Informe o valor da venda (sem os pontos): '))

if valor >= 100.000:
    c = 700.00 + valor*0.16
    print(f'Sua comissão é de {(c):.2f}')
elif valor < 100.000 and valor >= 80.000:
    c = 650.00 + valor*0.14
    print(f'Sua comissão é de {(c):.2f}')
elif valor < 80.000 and valor >= 60.000:
    c = 600.00 + valor*0.14
    print(f'Sua comissão é de {(c):.2f}')
elif valor < 60.000 and valor >= 40.000:
    c = 550.00 + valor*0.14
    print(f'Sua comissão é de {(c):.2f}')
elif valor < 40.000 and valor >= 20.000:
    c = 500.00 + valor*0.14
    print(f'Sua comissão é de {(c):.2f}')
else:
    c = 400.00 + valor*0.14
    print(f'Sua comissão é de {(c):.2f}')
