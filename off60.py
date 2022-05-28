NotaA = float(input("Informe a primeira nota: "))
NotaB = float(input("Informe a segunda nota: "))

if NotaA >= 0.00 and NotaA <= 10.00 and NotaB >= 0.00 and NotaB <= 10.00:
    media = (NotaA+NotaB)/2
    print(f'Sua media é: {(media)}')
else:
    print('Algumas das notas tem valor invalido.')
