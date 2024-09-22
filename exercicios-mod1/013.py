salario = float(input('Digite o salário: R$ '))
aumento = float(input('Digite o aumento (%): '))

valorAumento = round(salario * (aumento/100), 2)
novoSalario = salario + valorAumento

print('-' * 35)

print(f'O salário atual é R$ {salario:.2f}.\n'
      f'Aplicando {aumento:.0f}% de aumento, temos:\n\n'
      f'Valor do aumento R$ {valorAumento:.2f}.\n'
      f'Novo salário R$ {novoSalario:.2f}.')

print('-' * 35)