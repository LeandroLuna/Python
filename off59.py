x = int(input('Informe um numero inteiro: '))
y = int(input('Informe outro numero inteiro: '))
z = x - y

if z < 0:
    print(f"Y > X: {(y)}")
elif z == 0:
    print(f'Numeros iguais')
else:
    print(f"X > Y: {(x)}")
