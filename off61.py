salario = float(input('Seu salario: '))
prest = float(input('Valor da prestaçao: '))
quinto = salario/5

if prest > quinto:
    print('Emprestimo nao concendido.')
else:
    print('Emprestimo concedido')
