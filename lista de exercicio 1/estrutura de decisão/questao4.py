#4. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
#informar se os valores podem ser um triângulo. Indique, caso os lados formem um
#triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def ehTriangulo(lado1, lado2, lado3):
    if((lado1 + lado2) > lado3):
        return True
    elif((lado1 + lado3) > lado2):
        return True
    elif((lado2 + lado3) > lado1):
        return True
    else:
        return False

def calculaTriangulo(lado1, lado2, lado3):
    if(lado1 == lado2 and lado1 == lado3):
        return "Equilátero"
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        return "Escaleno"
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        return "Isósceles"

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if(ehTriangulo(lado1, lado2, lado3)):
    print(calculaTriangulo(lado1, lado2, lado3))
else:
    print("Os lados não formam um triângulo.")