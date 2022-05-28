idade = int(input('Informe sua idade: '))
trabalho = int(input('Tempo de trabalho: '))

if idade >= 65:
    print('Voce pode se aposentar!')
elif trabalho >= 30:
    print('Voce pode se aposentar!')
elif idade >= 60 and trabalho >= 25:
    print('Voce pode se aposentar!')
else:
    print('Voce nao pode se aposentar.')
