#5. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
#que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def calculaPesoIdeal(altura):
    pesoIdealHomem = (72.7 * altura) - 58
    pesoIdealMulher = (62.1 * altura) - 44.7

    return ("Se você for homem seu peso ideal é {:.2f} kg. Se for mulher, é {:.2f} kg.".format(pesoIdealHomem, pesoIdealMulher))

altura = float(input("Digite sua altura para calcular seu peso ideal: "))

print(calculaPesoIdeal(altura))