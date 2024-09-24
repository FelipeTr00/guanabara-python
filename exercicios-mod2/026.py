frase = str(input('Digite uma frase:\n')).strip()

a = frase.lower().count('a')
prim = 1 + frase.lower().find('a')
ult = 1 + frase.lower().rfind('a')

print(f'A letra "a" aparece: {a}x.\n'
      f'Primeira ocorrência {prim}º letra\n'
      f'Última ocorrência {ult}º letra\n')