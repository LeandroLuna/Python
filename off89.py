hora_chegada, min_chegada = [int(x) for x in input(
    "Digite a hora e minuto de chegada (** **  e ** **): ").split()]
hora_partida, min_partida = [int(x) for x in input(
    "Digite a hora e minuto de saída (** **  e ** **): ").split()]

# Define horario:
if hora_chegada > hora_partida:
    hora_partida = hora_partida + 24
if min_chegada > min_partida:
    min_partida = min_partida + 60
    hora_partida = hora_partida - 1

min_final = min_partida - min_chegada
hora_final = hora_partida - hora_chegada

if hora_final >= 1:
    if min_final > 1:
        print("O carro ficou estacionado durante %d horas e %d minutos." %
              (hora_final, min_final))
    else:
        print("O carro ficou estacionado durante %d horas." % (hora_final))
else:
    print("O carro ficou estacionado durante %d minutos." % (min_final))

# Define valores:
min_total = int((hora_final * 60) + min_final)

if min_total <= 120:
    if min_total <= 60:
        preco = 1.00
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2
        print("Preço total: R$%.2f." % (preco))
elif min_total <= 240:
    if min_total <= 180:
        preco = 2 + 1.40
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2 + (1.40 * 2)
        print("Preço total: R$%.2f." % (preco))
else:
    hora_total = int(min_total // 60)
    preco = 4.40 + ((hora_total - 4) * 2)
    print("Preço total: R$%.2f." % (preco))
