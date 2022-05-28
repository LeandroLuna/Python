n = float(input('Informe a sua nota: '))
f = int(input('Informe seu numero de faltas: '))

if n >= 0.00 and n <= 10.00:
    if n <= 20:
        if n >= 0.00 and n <= 3.90:
            print('Conceito: E')
        elif n >= 4.00 and n <= 4.90:
            print('Conceito: D')
        elif n >= 5.00 and n <= 7.40:
            print('Conceito: C')
        elif n >= 7.50 and n <= 8.90:
            print('Conceito: B')
        else:
            print('Conceito: A')
    else:
        if n >= 0.00 and n <= 3.90:
            print('Conceito: E')
        elif n >= 4.00 and n <= 4.90:
            print('Conceito: E')
        elif n >= 5.00 and n <= 7.40:
            print('Conceito: D')
        elif n >= 7.50 and n <= 8.90:
            print('Conceito: C')
        else:
            print('Conceito: B')
else:
    print('Informe uma nota entre 0 e 10.')
