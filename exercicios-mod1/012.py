valor = float(input('Digite o valor do produto: R$ '))
desc = float(input('Digite o desconto (%): '))

desconto = round(valor * ((desc/100)), 2)
liquido = valor - desconto

print(f'O preço do produto é R$ {valor:.2f}.\n'
      f'Aplicando {desc:.0f}% de desconto, temos:\n\n'
      f'Valor do desconto R$ {desconto:.2f}.\n'
      f'Valor líquido R$ {liquido:.2f}.')