dados = input("Informe as notas:")
n = list(map(float, dados.split()))
t = len(n)
soma = 0

for i in range(0, t):
    soma = soma+n[i]

n.append(soma/t)

if n[t] >= 7:
    print("Aprovado! Média: ", n[t])
elif n[t] >= 3:
    print("Exame! Média: ", n[t])
else:
    print("Reprovado! Média: ", n[t])
