# Exercicio de Fibonacci
lim = int(input('Qual limite de fibonacci? '))
a = 1
b = 1
for x in range(0, lim, 1):
    c = a + b
    b = a
    a = c
    print(b)
