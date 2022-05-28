x = int(input('Informe um numero: '))

a = x % 3
b = x % 5

if a == 0 and b == 0:
    print(f'O numero {x} é divisivel por 3 e por 5.')
else:
    print(f'O numero {x} é divisivel ou por 3 ou por 5.')
