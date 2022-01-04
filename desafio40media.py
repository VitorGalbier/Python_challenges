n1 = float(input('Qual foi a nota da primeira prova? '))
n2 = float(input('Qual foi a nota da segunda prova? '))
m = (n1 + n2) /2
if m < 5:
    print('REPROVADO!')
elif m >= 5 and m < 7:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')