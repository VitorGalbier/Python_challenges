# import math
# numero = int(input("Digite um numero "))
# divisores = 0
# usuario = int(math.sqrt(numero))
# for divisor in range(2, usuario):
#     if usuario % divisor == 0:
#         divisores = divisores + 1
#     if divisores > 1:
#         break
#
# if divisores > 1:
#     print("não é primo")
# else:
#     print("é primo")
#
#
# numero = int(input("Digite um numero"))
# divisores = 0
# for divisor in range(1, numero):
#     if numero % divisor == 0:
#         divisores = divisores + 1
#         if divisores > 1:
#           break
# if divisores > 1:
#   print("não é primo")
# else:
#   print("é primo")

# numero = int(input("Digite um numero "))
# divisores = 0
# if numero == 0:
#     print("não é primo")
# else:
#     for divisor in range(2, numero + 1):
#         if numero % divisor == 0:
#             divisores = divisores + 1
#             if divisores > 1:
#                 break
#
# if divisores > 1:
#     print("não é primo")
# else:
#     print("é primo")

numero = int(input("Digite um numero "))
divisores = 0

for divisor in range(1, numero+1):
    if numero % divisor == 0:
        divisores = divisores + 1
if divisores == 2:
    print('É primo')
else:
    print("não é primo")

