lista_frutas = ["Banana", "Maça", "Melancia"]

#lista_frutas[0] = "Banana"
#lista_frutas[1] = "Maça"
#lista_frutas[2] = "Melancia"
print(lista_frutas[1])

lista_frutas.append("Laranja") #append - add no final da lista
print(lista_frutas[3])
print()


for i in range(len(lista_frutas)):
    #print(i) #quantidade de itens
    print(lista_frutas[i]) #mostra os itens

    print()

    for fruta in lista_frutas:
        print(fruta)