x = int(input('Informe um numero: '))
y = 0

while(x > 0):
    y += x % 10
    x = int(x/10)
print(f"A soma dos algarismos do digito informado é: {(y)}")
