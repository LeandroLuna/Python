numero = int(input('Informe um valor de 1000 a 9999: '))
if numero >= 1000 and numero <= 9999:
    M = numero//1000 % 10
    C = numero//100 % 10
    D = numero//10 % 10
    U = numero//1 % 10
    print(f'{M}\n{C}\n{D}\n{U}')
else:
    print("Numero fora dos parametros.")
