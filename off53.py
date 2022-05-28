c = float(input('Comprimento do terreno em metros: '))
l = float(input('Largura do terreno em metros: '))
metro_tela = float(input('Preço do metro da tela: '))
preco = (c*l)*metro_tela
print(f"Custo para cercar o terreno é R${(preco):.2f}")
