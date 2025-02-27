#1. imprima a soma dos numeros entre 150 e 300

inicio = 150
parada = 300 + 1

soma = 0

for i in range(inicio, parada):
    soma += i

print(soma)