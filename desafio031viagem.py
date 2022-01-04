distancia = float(input("Qual a distância da sua viagem em Km: "))
if distancia > 200:
    custo = distancia * 0.45
else:
    custo = distancia * 0.50
print("O valor da passagem será de {}" .format(custo))
