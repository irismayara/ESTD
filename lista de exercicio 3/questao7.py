#7. Escreva uma função recursiva que receba um número inteiro positivo impar N e 
# retorne o fatorial duplo desse número. O fatorial duplo é definido como o produto
#  de todos os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15

def fatorialDuplo(n):
    if  n == 1:
        return 1
    else: 
        return n * fatorialDuplo(n-2)
    
print(fatorialDuplo(5))