import numpy
matriz1 = [(2, 4), (5, 8)]
matriz2 = [(9, 10), (1, 7)]
soma = []
soma2 = []

for n in range(2):
    soma.append(matriz1[0][n]+matriz2[0][n])
    soma2.append(matriz1[1][n]+matriz2[1][n])
print(f'Soma das matrizes:\n{soma}\n{soma2}\n')

subt = numpy.subtract(matriz1, matriz2)
print(f'Subtração das matrizes:\n{subt}\n')

transposta1 = numpy.transpose(matriz1)
print(f'Transposta da matriz 1:\n {transposta1}')
transposta2 = numpy.transpose(matriz2)
print(f'Transposta da matriz 2:\n {transposta2}')
mult = []
mult2 = []

for n in range(2):
    mult.append(matriz1[0][n]*matriz2[0][n])
    mult2.append(matriz1[1][n]*matriz2[1][n])
print(f'\nMultiplicação das matrizes:\n{mult}\n{mult2}\n')
