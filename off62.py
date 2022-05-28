sexo = input('Qual seu sexo? Homem ou Mulher: ')
altura = float(input('Qual altura? '))

if sexo == 'Homem':
    h1 = (72.7*altura)-58.00
    print('Seu peso ideal é: ', h1)
elif sexo == 'Mulher':
    h2 = (62.1*altura)-44.70
    print('Seu peso ideal é: ', h2)
else:
    print("Opcao invalida.")
