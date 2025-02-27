#Produto de uma Sequência de Números Naturais: Escreva uma função recursiva que calcule o produto
#  dos primeiros N números naturais. Por exemplo, para N = 4, a função deve
#  retornar 24 (1 * 2 * 3 * 4).

def produtoNaturais(n):
    if n == 1: return 1
    return n * produtoNaturais(n-1)

print(produtoNaturais(4))