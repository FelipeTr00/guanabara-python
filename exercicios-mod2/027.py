nome = str(input('Digite seu nome:\n')).strip()

pri_nome = nome[:nome.find(' ')].capitalize()
ult_nome = nome[1 + nome.rfind(' '):].capitalize()

print('Abreviando:')
print(pri_nome, ult_nome)