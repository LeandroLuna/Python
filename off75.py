ano = int(input('Informe o ano: '))
bi = ano % 4

if bi == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
