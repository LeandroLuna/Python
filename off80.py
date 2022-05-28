x = int(input('Informe o primeiro valor: '))
y = int(input('Informe o segundo valor: '))
z = int(input('Informe o terceiro valor: '))
op = input('Agora informe uma letra conforme a tabela:\n(a)Geométrica\n(b)Ponderada\n(c)Harmômica\n(d)Aritmética\n')

if x > 0:
    if y > 0:
        if z > 0:
            if op == 'a':
                geo = pow(x*y*z, 1/3)
                print('A resultante da funçao geometrica: ', geo)
            elif op == 'b':
                pond = x+2*y+3*z
                print('A media ponderada é: ', pond)
            elif op == 'c':
                harm = 1/(1/x+1/y+1/z)
                print('O resultado da função harmonica é: ', harm)
            elif op == 'd':
                arit = (x+y+z)/3
                print('A media aritmética é: ', arit)
            else:
                pass
        else:
            print('Informe o terceiro valor positivo.')
    else:
        print('Informe o segundo valor positivo')
else:
    print('Informe o primeiro valor inteiro positivo.')
