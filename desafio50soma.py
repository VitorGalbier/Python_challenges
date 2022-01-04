s = 0
cont = 0
for x in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(s, cont)
