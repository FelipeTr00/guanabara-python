nome = str(input('Digite seu nome completo: ')).strip()

upper = nome.upper()
lower = nome.lower()
len = len(nome) - nome.count(' ')
firstname = nome.find(' ')

print(f'\nAnalisando seu nome:\n'
      f'Maiúsculo: {upper}\n'
      f'Minúsculo: {lower}\n'
      f'Quantidade de letras: {len:.0f}\n'
      f'Letras primeiro nome: {firstname:.0f}')
