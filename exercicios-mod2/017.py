from math import hypot

co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

#hi = (co ** 2 + ca ** 2) ** 0.5
hi = hypot(co, ca)

print(f'\nA hipotenusa mede {hi:.2f}.')