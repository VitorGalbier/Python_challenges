s = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
     cont += 1
     print(x)
     s += x
print(s)