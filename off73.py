x = int(input('Escolha um numero conforme o menu: \n1 = Soma de 2 numeros\n2 = Diferença entre 2 numeros (maior pelo menor) \n3 = Produto entre 2 numeros\n4 = Divisão entre 2 numeros (denominador não pode ser zero)\n'))
if x > 0 and x < 5:
    if x == 1:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A soma é: {(a+b)}')
    elif x == 2:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        if a > b:
            print(f'A subtraçao é: {(a-b)}')
        else:
            print(f'A subtraçao é: {(b-a)}')
    elif x == 3:
        a = float(input('Informe o primeiro valor: '))
        b = float(input('Informe o segundo valor: '))
        print(f'A multiplicação é: {(a*b)}')
    elif x == 4:
        a = float(input('Informe o numero a ser dividido: '))
        b = float(input('Informe o denominador: '))
        if b == 0:
            print('Informe um denominador diferente de 0.')
        else:
            print(f'A divisão é: {(a/b)}')
    else:
        pass
else:
    print('Opção invalida.')
