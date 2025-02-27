#Número de Dígitos em um Número: Escreva uma função recursiva que conte o número de dígitos 
# em um número inteiro positivo. Por exemplo, para o número 4567, a função deve retornar 4.

def calculaDigitos(numero):
    return len(str(numero))

print(calculaDigitos(4567))