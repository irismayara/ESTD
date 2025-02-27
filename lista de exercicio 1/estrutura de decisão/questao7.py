#7. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

def calculaParOuImpar(num):
    if(num % 2 == 0):
        return "Par"
    else: 
        return "Ímpar"

numero = int(input("Digite um número: "))
print(calculaParOuImpar(numero))