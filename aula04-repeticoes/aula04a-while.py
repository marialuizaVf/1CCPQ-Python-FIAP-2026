cp = 0
while cp < 3:
    print(f"Produto {cp}")
    cp += 1

# While decrescente de 4 até 1
i=4
while i > 0:
    print(i)
    i-=1

# Nao aparecer um numero (continuar) e break (sair se caso for verdadeiro)
cp = 0
while cp <10:
    cp += 1

    if cp == 3:
        continue

    if cp ==7:
        break

    print(f"Produto {cp}")
