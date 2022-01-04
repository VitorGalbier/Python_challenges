peso = float(input('Qual é o seu peso? (Kg)? '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso/(altura ** 2)
if imc < 18.5:
    print('Abaixo do peso! Seu IMC é de {: .2f}' .format(imc))
elif imc >= 18.5 and imc < 25:
    print('Peso ideal! O seu IMC é de {: .2f}' .format(imc))
elif imc >= 25 and imc < 30:
    print('Sobrepeso! Seu IMC é de {: .2f}' .format(imc))
elif imc >= 30 and imc < 40:
    print('Obesidade! Seu IMC é de {: .2f}' .format(imc))
else:
    print('Obesidade mórbida! Seu IMC é de {: .2f}' .format(imc))