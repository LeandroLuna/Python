x = int(input('Escolha um numero conforme o menu: \n1 = Adiçao\n2 = Subtração\n3 = Multiplicação\n4 = Divisão\n'))
if x > 0 and x < 5:
    if x == 1:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A soma é: {(a+b)}')
    elif x == 2:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A subtraçao é: {(a-b)}')
    elif x == 3:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A multiplicação é: {(a*b)}')
    elif x == 4:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A divisão é: {(a/b)}')
    else:
        pass
else:
    print('Opção invalida.')
