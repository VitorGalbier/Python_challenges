salario = float(input('Qual o seu salário mensal? '))
casa = float(input('Qual o valor do imóvel? '))
tempo = int(input('Em quantos meses pretende pagá-la? '))
if casa/tempo > salario * 0.3:
    print('O empréstimo está negado')
else:
    print ('O emprestimo foi aprovado! O valor da parcela será de {: .2f} reais' .format(casa/tempo))