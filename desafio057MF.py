sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido, tente novamente ')).strip().upper()[0]
print('Sexo {} digitado com sucesso' .format(sexo))