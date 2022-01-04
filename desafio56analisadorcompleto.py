soma_das_idades = 0
mulheres_menores_de_20_anos = 0
nome_do_homem_mais_velho = ''
idade_do_homem_mais_velho = 0

for x in range(1, 5):
    print('-' * 5, '{} PESSOA' .format(x), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    if sexo != 'M' or sexo != 'F':
        print('Resposta inválida')
        pass

    soma_das_idades += idade

    if sexo == 'F' and idade < 20:
        mulheres_menores_de_20_anos =+ 1

    elif sexo == 'M' and idade > idade_do_homem_mais_velho:
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome

print('A média de idade do grupo é de {} anos.' .format(soma_das_idades/4))
print('O homem mais velho tem {} anos de idade e se chama {}.' .format(idade_do_homem_mais_velho, nome_do_homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos de idade.' .format(mulheres_menores_de_20_anos))

