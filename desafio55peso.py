pes = []
for x in range(1, 6):
    peso = float(input('Peso da {} pessoa: ' .format(x)))
    pes.append(peso)
print('O maior peso lido foi {} kg' .format(max(pes)))
print('O menor peso lido foi {} kg' .format(min(pes)))
