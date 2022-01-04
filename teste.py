s = str(input())
b = s.split()
par = []
impar = []
for i in range(len(b)):
    if i % 2 == 0:
        par.append(b)
    else:
        impar.append(b)
print(par)