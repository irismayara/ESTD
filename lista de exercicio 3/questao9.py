#9. O MDC de dois números inteiros é o maior número inteiro que divide ambos sem deixar resto. 
# O MDC pode ser calculado através do algoritmo de Euclides. 
# Abaixo uma função iterativa que calcula o MDC. Reescreva a função abaixo de forma recursiva.

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
def testMDC():
    assert mdc(48,18) == 6
    assert mdc(101,10) == 1
    assert mdc(56,98) == 14

testMDC()