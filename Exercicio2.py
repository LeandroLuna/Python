# Calculo de fatorial
num = int(input('Informe o numero a ser fatorado: '))

if num == 0:
    y = 1
else:
    y = num
while num > 1:
    y = num*y
    num = num - 1
print(f'Fatorial é: {y}')
