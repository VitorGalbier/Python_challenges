salario = float(input("Qual o valor do seu salário em reais? "))
if salario > 1250.00:
    novo = salario * 1.10
    print("O valor atualizado é de {}" .format(novo))
else:
    novo = salario * 1.15
    print("O valor atualizado é de {:.2f}" .format(novo))