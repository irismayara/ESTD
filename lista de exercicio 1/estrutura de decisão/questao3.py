#3. Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def calculaDiaDaSemana(num):
    if(num == 1):
        return "Domingo"
    elif(num == 2):
        return "Segunda"
    elif(num == 3):
        return "Terça"
    elif(num == 4):
        return "Quarta"
    elif(num == 5):
        return "Quinta"
    elif(num == 6):
        return "Sexta"
    elif(num == 7):
        return "Sábado"
    else:
        return "Valor inválido"

num = int(input("Digite um número para saber o dia da semana correspondente: "))
print(calculaDiaDaSemana(num))