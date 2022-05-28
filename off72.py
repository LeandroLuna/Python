a = float(input('Informe o primeiro lado: '))
b = float(input('Informe o segundo lado: '))
c = float(input('Informe o terceiro lado: '))
x = b + c
y = a + c
z = a + b
if a < x and b < y and c < z:
    if a == b and b == c:
        print('Triangulo Equilatero!')
    elif a != b and b != c and a != c:
        print('Triangulo Escaleno!')
    else:
        print('Triangulo Isoceles!')
else:
    print('Não é triangulo.')
