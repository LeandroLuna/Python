x = float(input('Informe a primeira nota: '))
y = float(input('Informe a segunda nota: '))
z = float(input('Informe a terceira nota: '))

if x >= 0.00 and y >= 0.00 and z >= 0.00 and x <= 10.00 and y <= 10.00 and z <= 10.00:
    media = (x*2.0+y*3.0+z*5.0)/10.0
    if media <= 2.9:
        print('Aluno reprovado.')
    elif media >= 3.0 and media <= 4.9:
        print('Aluno de exame')
    elif media > 4.9:
        print('Aluno aprovado')
    else:
        pass
else:
    print('Redigite as notas. Elas devem estar entre 0 e 10.')
