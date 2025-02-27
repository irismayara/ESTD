#3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. 
# Por exemplo, a letra 'u'ocorre 2 vezes em "estrutura"

def contar(letra, palavra):
    if len(palavra) == 0:
        return 0
    
    if(palavra[0] == letra):
        return 1 + contar(letra, palavra[1:])
    else:
        return contar(letra, palavra[1:])
    
def testContar():
    assert contar('u', 'estrutura') == 2
    assert contar('t', 'estrutura') == 2
    assert contar('a', 'estrutura') == 1
    assert contar('x', 'estrutura') == 0
    assert contar('s', '') == 0
    print("Todos os testes em contar() passaram!")

testContar()