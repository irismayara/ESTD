#3. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorPorHora = float(input('Quanto você ganha por hora trabalhada? '))
horasTrabalhadasMes = float(input('Quantas horas você trabalhou no mês? '))

salarioMes = valorPorHora * horasTrabalhadasMes

print('O salário total para o referido mês é de R$', salarioMes)