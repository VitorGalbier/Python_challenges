import random
pessoa = int(input('O computador pensou em um número de 1 a 5, escolha o seu: '))
pc = random.randint(1, 5)
if pessoa == pc:
    print('Parabéns, você acertou, o computador pensou em {}!' .format(pc))
else:
    print('Você perdeu!, o número escolhido pelo computador foi {}' .format(pc))
