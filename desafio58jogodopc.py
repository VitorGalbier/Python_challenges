import random
pc = random.randint(0, 10)
tentativa = 1
print("""Sou seu computador...
Acabei de pensar em um número de 0 a 10.
Será que você consegue advinhar?""")
numero = int(input('Qual é o seu palpite? '))
while pc != numero:
    tentativa += 1
    if pc > numero:
        print('Mais.. tente novamente!')
        numero = int(input('Qual é o seu palpite? '))
    elif pc < numero:
        print('Menos... tente novamente!')
        numero = int(input('Qual é o seu palpite? '))

print('Parabéns!!! Você acertou em {} tentativas, o computador pensou em {}' .format(tentativa, pc))