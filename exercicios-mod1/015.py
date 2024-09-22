# Exercício Python 15: Escreva um programa que pergunte a
# quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantidade de dias: '))
km = float(input('Quilometros (km) percorridos: '))

precoDias = dias * 60
precoKm = km * 0.15
aluguel = precoDias + precoKm

print(f'O carro ficou alugado por {dias:.0f} dias\n'
      f'Percorreu {km:.0f}Km \n'
      f'O preço do aluguél é R$ {aluguel:.2f}')