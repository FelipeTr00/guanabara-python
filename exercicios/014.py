# Exercício Python 14: Escreva um programa que converta
# uma temperatura digitando em graus Celsius e converta
# para graus Fahrenheit.

temperatura = float(input('Digite a temperatura em graus Celcius: '))

fahrenheit = ((temperatura * 9) / 5) + 32

print(f'\nA temperatura de {temperatura}°C.\n'
      f'Corresponde a {fahrenheit}°F.')
