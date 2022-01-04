print('-' * 15)
print('Sequência de Fibonacci')
print('-' * 15)
primeiro_termo = 1
razao = 0
cont = 0
pergunta = False

while pergunta == False:
    termos = int(input('Quantos termos você quer mostrar? '))

    while cont < termos:
        cont += 1
        if razao <= primeiro_termo:
            print(primeiro_termo)
            razao = primeiro_termo - razao
            primeiro_termo += razao

    if termos < cont and termos != 0:
        print('Esse número de termos já foi mostrado, tente novamente!')
    if termos == 0:
        pergunta = True
print('Terminou!!')





