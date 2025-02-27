#Escreva uma função RECURSIVA chamada soma_perfeitos que recebe dois 
# números inteiros a e b como parâmetros e retorna a soma de todos os 
# números perfeitos no intervalo fechado entre a e b . Use a função da questão 1 para 
# verificar se o número é perfeito ou não.
#Caso não haja números perfeitos no intervalo, a função deve retornar 0.

def eh_num_perfeito(num, div=1, soma=0):
    if div == num:
        if soma == num:
            return True
        else:
            return False
    
    if num % div == 0:
        soma += div

    return eh_num_perfeito(num, div+1, soma)

def soma_perfeitos(a, b):
    if a > b:
        return 0
    
    if eh_num_perfeito(a):
        return a + soma_perfeitos(a+1, b)

    return soma_perfeitos(a+1, b)

print(soma_perfeitos(1, 27)) # Saída: 6
print(soma_perfeitos(1, 28)) # Saída: 34 (6 + 28)