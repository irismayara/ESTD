#Contar Caracteres em uma String: Escreva uma função recursiva que conte o número de 
# ocorrências de um determinado caractere em uma string. Por exemplo, para a string 
# "recursividade" e o caractere 'i', a função deve retornar 3.

def contarCaracteres(caractere, string):
    if len(string) == 0: return 0
    else:
        if string[0] == caractere:
            return 1 + contarCaracteres(caractere, string[1:])
        else:
            return contarCaracteres(caractere, string[1:])


def testContarCaracteres():
    assert contarCaracteres('i', 'recursividade') == 2
    assert contarCaracteres('a', 'arara') == 3
    print('todos os testes em contarCaracteres() passaram')

testContarCaracteres()