numero = str(input("Informe um número: "))
m = numero.zfill(4)
print('O número escolhido foi {}'.format(numero))
print('A unidade é {}: ' .format(m[3]))
print('A dezena é {}: ' .format(m[2]))
print('a centena é {}: ' .format(m[1]))
print('o milhar é {}: ' .format(m[0]))
