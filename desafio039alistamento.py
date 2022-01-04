from datetime import date
ano = int(input('Em qual ano você nascecu?'))
if date.today().year - ano > 18:
    print('Já passou o tempo de alistamento, você está {} anos atrasado' .format((date.today().year - ano) - 18))
elif date.today().year - ano < 18:
    print('Você ainda não está pronto para se alistar, faltam {} anos' .format(18 - (date.today().year - ano)))
else:
    print('Você deve se alistar este ano!')

