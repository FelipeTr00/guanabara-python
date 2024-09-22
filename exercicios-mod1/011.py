largura = float(input('Largura da parede em metros (m): '))
altura = float(input('Altura da parede em metros (m): '))

area = altura * largura
tinta = area / 2

print(f'Sua parede tem {area}m². \n'
      f'São necessários {tinta}l de tinta.')
