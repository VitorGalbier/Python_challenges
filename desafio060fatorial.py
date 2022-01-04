fatorial = int(input('Digite um valor para calcular seu fatorial: '))
fat = fatorial
m = 1
while fat > 0:
    print('{}' .format(fat), end='')
    print(' x ' if fat > 1 else ' = ', end='')
    m *= fat
    fat -= 1
print(m)

