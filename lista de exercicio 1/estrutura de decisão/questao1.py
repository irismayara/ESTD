#1. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
# A mensagem “Reprovado”, se a média for menor do que sete;
# A mensagem “Aprovado com Distinção”, se a média for igual a dez.

def calcularMedia(nota1, nota2):
    media = (nota1 + nota2)/2

    if(media == 10):
        return "Aprovado com Distinção"
    elif(media >= 7):
        return "Aprovado"
    elif(media < 7):
        return "Reprovado"

nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))

print(calcularMedia(nota1, nota2))