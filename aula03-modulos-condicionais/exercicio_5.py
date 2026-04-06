valor_1 = int(input("Digite o primeiro número: "))
valor_2 = int(input("Digite o segundo número: "))

valor=valor_1%valor_2

if valor == 0:
    print("São multiplos")
else:
    print("Não são multiplos")