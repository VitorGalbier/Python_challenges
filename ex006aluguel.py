d = int(input('Quantos dias permaneceus com o veículo?'))
km = float(input('Quantos Km foram rodados?'))
p = (d*60)+(km*0.15)
print('O total a pagar é de {:.2f} reais' .format(p))
