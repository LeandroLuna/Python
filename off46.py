numero = int(input('informe um numero: '))
if numero >= 100 and numero <= 999:
    inv = int(str(numero)[::-1])
    print(f'numero invertido: {inv}')
else:
    print('Numero invalido. Range de 100 a 999')
