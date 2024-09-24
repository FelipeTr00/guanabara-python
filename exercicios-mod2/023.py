num = int(input('Digite um núm. de 0 à 9999:\n'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\nAnalisando o número {num}:')
if m != 0:
    print(f'Milhar: {m}')
if c != 0:
    print(f'Centena: {c}')
if d != 0:
    print(f'Dezena: {d}')
if u != 0:
    print(f'Unidade: {u}')


