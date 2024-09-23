import math

num = float(input('Informe um valor: '))

sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))

print('-'*20)

print(f'Valor: {num:>.2f}:\n'
      f'Seno: {sen:>.2f}\n'
      f'Cosseno: {cos:>.2f}\n'
      f'Tangente: {tan:>.2f}')

print('-'*20)

