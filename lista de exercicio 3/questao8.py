#8. Escreva uma função recursiva que informa se uma String é palíndroma ou não. 
# Um palíndromo é uma string que é lida da mesma maneira da esquerda para a direita 
# e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
#papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

def ehPalindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    
    return ehPalindromo(palavra[1:-1])


def testeEhPalindromo():
    assert ehPalindromo('arara') == True
    assert ehPalindromo('python') == False
    assert ehPalindromo('') == True
    assert ehPalindromo('a') == True

testeEhPalindromo()
