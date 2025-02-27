# Sequência de Collatz: Escreva uma função recursiva que, dado um número inteiro positivo N, 
# retorne a sequência de Collatz até chegar a 1. A sequência de Collatz é definida da seguinte 
# forma: comece com N, se N é par, divida por 2; se N é ímpar, multiplique por 3 e adicione 1. 
# Repita o processo com o resultado até que N se torne 1.

def sequenciaCollatz(numero):
    print(int(numero), end=' ')
    if numero == 1: return 1
    if numero % 2 == 0: return sequenciaCollatz(numero/2)
    if numero % 2 != 0: return sequenciaCollatz(numero*3+1)

sequenciaCollatz(6)