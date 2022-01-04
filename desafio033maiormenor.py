primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
if primeiro > segundo and primeiro > terceiro:
    print("O maior valor digitado foi {}" .format(primeiro))
if segundo > primeiro and segundo > terceiro:
    print("O maior valor digitado foi {}".format(segundo))
if terceiro > primeiro and terceiro > segundo:
    print("O maior valor digitado foi {}".format(terceiro))
if primeiro < segundo and primeiro < terceiro:
    print("O menor valor foi {}" .format(primeiro))
if segundo < primeiro and segundo < terceiro:
    print("O menor valor foi {}" .format(segundo))
if terceiro < primeiro and terceiro < segundo:
    print("O menor valor foi {}" .format(terceiro))
