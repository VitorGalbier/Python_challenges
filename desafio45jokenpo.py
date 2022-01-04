import random
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0, 2)
if pc == 0:
    if jogada == 0:
        print('EMPATE! O computador também escolheu {}!' .format(itens[0]))
    elif jogada == 1:
        print('VOCÊ VENCEU! O computador escolheu {}!' .format(itens[0]))
    elif jogada == 2:
        print('VOCÊ PERDEU! O computador escohleu {}!' .format(itens[0]))
    else:
        print('Jogada inválida, tente novamente.')
elif pc == 1:
    if jogada == 0:
        print('VOCÊ PERDEU! O computador escolheu {}!' .format(itens[1]))
    elif jogada == 1:
        print('EMPATE! O computador escolheu {}!' .format(itens[1]))
    elif jogada == 2:
        print('VOCÊ VENCEU! O computador escolheu {}!' .format(itens[1]))
    else:
        print('Jogada inválida, tente novamente.')
elif pc == 2:
    if jogada == 0:
        print('VOCÊ VENCEU! O computador escolheu {}!' .format(itens[2]))
    elif jogada == 1:
        print('VOCÊ PERDEU! O computador escolheu {}!' .format(itens[2]))
    elif jogada == 2:
        print('EMPATE! O Computador escolheu {}!' .format(itens[2]))
    else:
        print('Jogada inválida, tente novamente.')