valor = float(input('\tValor a pagar:'))
print(f'Desconto de 10% a vista: R${(valor*0.9):.2f}\nParcela em 3x: R${(valor/3):.2f}\nComissao vendedor (em venda a vista): R${((valor*0.9)*0.05):.2f}\nComissao vendedor (venda parcelada): R${(valor*0.05):.2f}')
