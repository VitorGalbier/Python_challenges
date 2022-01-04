#Usei import time para ter um contador
import time
#Valores e condições para serem trabalhadas
primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))
condicao = False

while not condicao:
    print(20 * '_')
    opcao = int(input('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIOR DO PROGRAMA
>>>>>>>> Qual é sua opção? '''))
#soma dos valores digitados
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print('A soma dos valores é {}' .format(soma))
        time.sleep(1)
#multiplicação dos valores digitados
    elif opcao == 2:
        multi = primeiro_valor * segundo_valor
        print('A multiplicação entre os valores é {}' .format(multi))
        time.sleep(1)
#maior valor entre os valores
    elif opcao == 3:
        time.sleep(1)
        if primeiro_valor > segundo_valor:
            print('O maior valor é {}' .format(primeiro_valor))
        elif primeiro_valor < segundo_valor:
            print('O maior valor é {}' .format(segundo_valor))
        else:
            print('Os valores são iguais')
#novos valores
    elif opcao == 4:
        primeiro_valor = int(input('Digite um valor: '))
        segundo_valor = int(input('Digite outro valor: '))
        time.sleep(1)
#encerramento
    elif opcao == 5:
        time.sleep(2)
        condicao = True
        print('Finalizando....')
        time.sleep(3)
        print('O programa foi encerrado!!')
#opções diversas das trabalhadas
    else:
        print('Opção inválida, tente novamente!')
        pass