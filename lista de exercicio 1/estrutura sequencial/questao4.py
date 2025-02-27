#4. Faça um Programa que peça a temperatura em graus Farenheit, transforme e
# mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

temperaturaFarenheit = float(input('Digite a temperatura em Farenheit: '))

temperaturaCelsius = (5 * (temperaturaFarenheit - 32))/ 9

print('A temperatura em Celsius é: ', temperaturaCelsius, '°C')