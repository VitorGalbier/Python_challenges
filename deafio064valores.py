soma = 0
numero = 0
condiçao = False
while condiçao == False:

    soma += numero
    numero = int(input('Digite um valor [999 para parar] '))

    if numero == 999:
        print(soma)
        break