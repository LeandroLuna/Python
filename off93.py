peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso/(pow(altura, 2.0))

if imc >= 0 and imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.6 and imc <= 24.9:
    print('Saudável')
elif imc >= 25.0 and imc <= 29.9:
    print('Peso em excesso')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade Grau 1')
elif imc >= 35.0 and imc <= 39.9:
    print('Saudável')
elif imc >= 40.0:
    print('Obesidade Grau 3 (mórbida).')
else:
    print('Informações incorretas. Reinfome seus dados.')
