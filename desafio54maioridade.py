from datetime import date
menor = []
maior = []
for x in range(1, 8):
    idade = int(input('Em que ano a {} pessoa nasceu? ' .format(x)))
    if date.today().year - idade < 18:
        menor.append(idade)
    else:
        maior.append(idade)
print('Tem {} pessoas maior de idade e {} pessoas menores de idade' .format(len(maior), len(menor)))
print(maior, menor)