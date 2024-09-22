tabuada = int(input("Informe a tabuada: "))

print(f"{'=' * 12}")

for i in range(1, 11):
    val = tabuada * i
    print(f'{tabuada} x {i:>2} = {val:>2}')

print(f"{'=' * 12}")
