#5. Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.

def ehBissexto(ano):
    if(ano % 4 == 0):
        if(ano % 100 != 0):
            return True
        else:
            if(ano % 400 == 0):
                return True
    else:
        return False

ano = int(input("Informe um ano para saber se é bisexto ou não: "))

if(ehBissexto(ano)):
    print("Ano bissexto")
else:
    print("Ano não bissexto")