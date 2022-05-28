est = input('Informe seu estado: ')
valor = float(input('Valor do produto: '))

if est == 'MG':
    print(f'Valor do produto com imposto: {(valor*1.07):.2f}')
elif est == 'SP':
    print(f'Valor do produto com imposto: {(valor*1.12):.2f}')
elif est == 'RJ':
    print(f'Valor do produto com imposto: {(valor*1.15):.2f}')
elif est == 'MS':
    print(f'Valor do produto com imposto: {(valor*1.08):.2f}')
else:
    print('Estado não registrado. Escolha entre: MG, SP, RJ e MS.')
