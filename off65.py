x = float(input('Informe a primeira nota: '))
y = float(input('Informe a segunda nota: '))
z = float(input('Informe a terceira nota: '))
pond = (x*1.0+y*1.0+z*2.0)/4.0

if pond >= 60.00:
    print(f"Voce foi aprovado.")
else:
    print("Voce foi reprovado.")
