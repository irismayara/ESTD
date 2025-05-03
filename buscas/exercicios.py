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
#print(busca_binaria_recursividade(lista, 55))

#12. Crie uma função de pesquisa binária que retorne todos os
#  índices de um número em uma lista ordenada que pode conter duplicatas.

def busca_binaria_com_duplicatas(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    indices = []
    
    while inicio <= fim:
        meio = (inicio + fim)//2

        if lista[meio] == alvo:
            indices.append(meio) 
        
            esquerda = meio - 1
            while esquerda >= inicio and lista[esquerda] == alvo:
                indices.append(esquerda)
                esquerda -= 1
            direita = meio + 1
            while direita <= fim and lista[direita] == alvo:
                indices.append(direita)
                direita += 1
            break
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return sorted(indices) 

lista = [1, 2, 2, 3, 4, 4, 4, 5, 6]
alvo = 4
#print(busca_binaria_com_duplicatas(lista, alvo))

#13. Implemente a busca binária usando recursividade sem o operador slice. 
# Você precisará passar o índice dos valores iniciais e finais na sublistas. 

def busca_binaria_sem_slice(lista, alvo, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif alvo < lista[meio]:
        fim = meio - 1
        return busca_binaria_sem_slice(lista, alvo, inicio, fim)
    else:
        inicio = meio + 1
        return busca_binaria_sem_slice(lista, alvo, inicio, fim)
    
lista = [10, 20, 30, 40, 50, 60]
print(busca_binaria_sem_slice(lista, 55))