def compra(dindin, preco):
    qtdBombons = dindin//preco
    troco = dindin % preco
    return qtdBombons, troco


res = compra(qtdBombons, troco)

dindin = float(input("Quantos trocados Joãozinho tem?"))
preco = float(input("Quanto custa cada bombom?"))

print(f"Joaozin pode comprar {res[0]:.0f} bombons")
print(f"E sobrará R${res[1]} de troco")
