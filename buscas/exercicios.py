#9. Suponha que você tenha uma lista de strings ordenadas alfabeticamente. 
# Como você adaptaria a busca binária para encontrar uma
# determinada string nessa lista? Forneça um exemplo em Python. 

def busca_binaria_string(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim)//2

        if lista[meio] == alvo:
            return meio
        else:
            if alvo < lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    
    return -1

lista = ['a', 'b', 'c', 'd', 'e', 'f']
alvo = 'f'
#print(busca_binaria_string(lista, alvo))

#11. Apresente uma versão recursiva da busca binária em Python. 
# Explique como a recursão funciona nesse caso. 

def busca_binaria_recursividade(lista, alvo):
    if len(lista) == 0:
        return False

    meio = len(lista)//2

    if lista[meio] == alvo:
        return True
    else:
        if alvo < lista[meio]:
            return busca_binaria_recursividade(lista[:meio], alvo)
        else:
            return busca_binaria_recursividade(lista[meio+1:], alvo)

lista = [10, 20, 30, 40, 50, 60]
print(busca_binaria_recursividade(lista, 55))