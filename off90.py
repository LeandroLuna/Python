import math
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
bis = ano % 4
inf = math.inf

if mes > 0 and mes <= 12:
    if ano > 0 and ano < inf:
        if bis == 0:
            if mes == 2:
                if dia > 0 and dia <= 29:
                    print('Data digitada corretamente.')
                else:
                    print('Dia invalido para o mes de fevereiro em ano bissexto.')
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia > 0 and dia <= 30:
                    print('Data digitada corretamente. ')
                else:
                    print('Dia invalido para o mes informado.')
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 12:
                if dia > 0 and dia <= 31:
                    print('Data digitada corretamente.')
                else:
                    print('Dia invalido para o mes informado.')
        else:
            if mes == 2:
                if dia > 0 and dia <= 28:
                    print('Data digitada corretamente.')
                else:
                    print('Dia invalido.')
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia > 0 and dia <= 30:
                    print('Data digitada corretamente. ')
                else:
                    print('Dia invalido para o mes informado.')
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 12:
                if dia > 0 and dia <= 31:
                    print('Data digitada corretamente.')
                else:
                    print('Dia invalido para o mes informado.')
    else:
        print('Ano invalido.')
else:
    print('Mes invalido.')
