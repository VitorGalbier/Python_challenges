frase = str(input('Digite a frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for x in range(len(junto) - 1, -1, -1):
    inverso += junto[x]
print(inverso, junto)
if inverso == junto:
    print('PALÍNDROMO!!')
else:
    print('NÃO É PALÍNDROMO')