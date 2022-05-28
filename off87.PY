import math
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mes: '))
ano = int(input('Informe o ano: '))
inf = math.inf
fev = 2

if ano > 0 and ano < inf:
    bi = ano % 4
else:
    print('Ano invalido.')

if dia > 0 and dia <= 31:
    if mes >= 1 and mes <= 12:
        if mes == 2:
            if bi != 0 and dia > 28:
                print('Dia invalido em ano nao bissexto')
            elif bi == 0 and dia <= 29:
                print('Data digitada corretamente.')
            else:
                print('Dia invalido.')
        else:
            print('Data digitada corretamente.')
    else:
        print('Mes invalido')
else:
    print('Dia invalido')
