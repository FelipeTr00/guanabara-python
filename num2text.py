from num2words import num2words


def numero_por_extenso(valor):
    # Separa reais e centavos
    reais = int(valor)
    centavos = int(round((valor - reais) * 100))

    # Converte os valores para texto
    extenso_reais = num2words(reais, lang='pt_BR')
    extenso_centavos = num2words(centavos, lang='pt_BR')

    # Formata a saída
    if reais == 1:
        texto_reais = f"{extenso_reais} real"
    else:
        texto_reais = f"{extenso_reais} reais"

    if centavos == 1:
        texto_centavos = f"{extenso_centavos} centavo"
    elif centavos > 0:
        texto_centavos = f"{extenso_centavos} centavos"
    else:
        texto_centavos = ""

    # Junta a parte dos reais e centavos
    if centavos > 0:
        return f"{texto_reais} e {texto_centavos}"
    else:
        return texto_reais


# Exemplo de uso
valor = float(input("Digite um valor em reais: "))
print(numero_por_extenso(valor))
