#Soma de uma Sequência de Números Naturais: Escreva uma função recursiva que calcule a soma 
# dos primeiros N números naturais. Por exemplo, para N = 5, a função deve retornar
#  15 (1 + 2 + 3 + 4 + 5).

def somaNaturais(n):
    if n == 0: return 0
    else:
        return n + somaNaturais(n-1)
    
print(somaNaturais(5))