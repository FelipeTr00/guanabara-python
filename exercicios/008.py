valor = int(input('Digite os quilometros (km): '))

hm = valor / 0.1
dam = valor / 0.01
mt = valor / 0.001
cm = round(valor / 0.00001)
mm = round(valor / 0.000001)

print(f'\nKm = {valor}\n'
      f'Hectômetros = {hm}\n'
      f'Decâmetro = {dam}\n'
      f'Metros = {mt}\n'
      f'Centímetros = {cm}\n'
      f'Milímetros = {mm}\n')






