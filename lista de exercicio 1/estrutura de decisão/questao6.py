# 6. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.

def validarData(data):
    valida = False
    for chave, valor in data:
        if chave in [0,1]:
            if valor in range(0,9):
                valida = True
            else:
                valida = False
        elif chave in [2, 5]:
            if valor == '/':
                valida = True
            else:
                valida = False
        elif chave in [3]:
            if valor in range(0,1):
                valida = True
            else:
                valida = False
        elif chave in [4]:
            if valor in range(0,9):
                valida = True
            else:
                valida = False
        elif chave in [6,7,8,9]:
            if valor in range(0,9):
                valida = True
            else:
                valida = False
    return valida


data = input("Digite uma data no formato dd/mm/aaaa: ")

print(validarData(data))
