#2. Armazenaem uma lista todos os múltiplos de 3,
# entre 1 e 100. Imprima cada elemento da lista, um por linha.

inicio = 1
parada = 100 + 1

multiplosDe3 = []

for i in range(inicio, parada):
    if( i % 3 == 0):
        print (i)
        multiplosDe3.append(i)