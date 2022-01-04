valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista ou dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    print('O valor a ser pago é de {: .2f} reais' .format(valor - (valor * 0.1)))
elif opçao == 2:
    print('O valor a ser pago é de {: .2f} reais' .format(valor - (valor * 0.05)))
elif opçao == 3:
    parcela = valor/2
    print('O valor a ser pago é de {: .2f} reais, pagos em duas parcelas de {: .2f} reais'.format(valor, parcela))
elif opçao == 4:
    parc = int(input('Em quantas parcelas? '))
    parcela = (valor * 1.20) / parc
    print('O valor a ser pago é de {: .2f} reais, pagos em {} parcelas de {: .2f} reais' .format(valor * 1.20, parc, parcela))
else:
    print('Opção inválida de pagamento, tente novamente')

