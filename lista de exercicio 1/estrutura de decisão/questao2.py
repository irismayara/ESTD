#2. Faça um Programa que leia três números e mostre o maior e o menor deles.

def calculaMaior(numero1, numero2, numero3):
    if(numero1 >= numero2):
        if(numero1 >= numero3):
            return numero1
        else:
            return numero3
    else:
        if(numero2 >= numero3):
            return numero2
        else:
            return numero3
        
def calculaMenor(numero1, numero2, numero3):
    if(numero1 <= numero2):
        if(numero1 <= numero3):
            return numero1
        else:
            return numero3
    else:
        if(numero2 <= numero3):
            return numero2
        else:
            return numero3

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

print("O maior número é o", calculaMaior(numero1, numero2, numero3))
print("O menor número é o", calculaMenor(numero1, numero2, numero3))