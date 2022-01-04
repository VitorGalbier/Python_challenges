frase = str(input('Digite uma frase: ')).upper()
fr = frase[::-1]
if frase == fr:
    print('É um Palíndromo!!!')
else:
    print('Não é um palíndromo!!')