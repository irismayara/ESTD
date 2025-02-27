#4. Escreva uma função recursiva que receba um número inteiro positivo N e 
# imprima todos os números naturais de 0 até N em ordem crescente.

def imprimeNaturais(n):
    if n < 0: return
   
    imprimeNaturais(n-1)
    print(n, end=' ')

imprimeNaturais(5)