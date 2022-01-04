pt = int(input('Digite o primeiro termo: '))
razao = int(input(('Digite a razão: ')))
decimo = pt + (10 - 1) * razao
for x in range(pt, decimo, razao):
    print(x)