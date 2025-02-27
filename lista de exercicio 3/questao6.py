#6. Escreva uma função recursiva que calcule o Nésimo 10 termo da sequencia de Fibonacci. 
# A sequência de Fibonacci é 0, 1, 1, 2, 3, 5, 8, 13, 21,...

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))