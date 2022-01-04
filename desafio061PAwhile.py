print('GERADOR DE PA')
print(20 * '-=-')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
vezes = 1
while vezes < 11:
    pa = primeiro_termo + (vezes - 1) * razao
    vezes += 1
    print(pa, end=', ')

print(vezes - 1)