#Soma dos Dígitos de um Número: Escreva uma função recursiva que calcule a soma dos dígitos 
# de um número inteiro positivo. Por exemplo, para o número 123, a função deve retornar 6 (1 + 2 + 3).

def somarDigitos(numero):
    if len(str(numero)) == 0:
        return 0
    else:
        return int(str(numero)[0]) + somarDigitos(str(numero)[1:])

print(somarDigitos(123))