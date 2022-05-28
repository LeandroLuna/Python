a = float(input('Apostador 1: '))
b = float(input('Apostador 2: '))
c = float(input('Apostador 3: '))
premio = float(input("Valor do premio: "))
apostas_total = a+b+c
fatia1 = premio*(a/apostas_total)
fatia2 = premio*(b/apostas_total)
fatia3 = premio*(c/apostas_total)
print(
    f'O valor será repartido da seguinte maneira:\nApostador 1: R${(fatia1)}\nApostador 2: R${(fatia2)}\nApostador 3: R${(fatia3)}')
