#5. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos 
# os números naturais de 0 até N em ordem decrescente.

def imprimeNaturais(n):
    if n < 0: return

    print(n, end=' ')
    imprimeNaturais(n-1)
        
imprimeNaturais(3)