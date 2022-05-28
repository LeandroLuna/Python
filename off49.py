from datetime import datetime, timedelta

inicio = input(
    'Informe o horario de inicio do experimento (formato Horas:Minutos:Segundos): ')
# transforma a string em data
data_inicio = datetime.strptime(inicio, "%H:%M:%S")

duracao = input(
    'Quanto tempo durara o experimento (formato Horas:Minutos:Segundos): ')
horas, minutos, segundos = map(int, duracao.split(':'))
# transforma a string em timedelta
duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)

# soma a data à duração
termino = data_inicio + duracao

# formata o resultado
print(termino.strftime('%H:%M:%S'))
