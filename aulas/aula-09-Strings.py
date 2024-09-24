# String de exemplo
frase = "  Python é uma linguagem de programação poderosa e versátil.  "

# 1. Fatiamento de String
print("Fatiamento:")
print(frase[0:6])  # 'Python'
print(frase[:6])   # 'Python' (do início até o índice 6)
print(frase[7:])   # 'é uma linguagem de programação poderosa e versátil.  ' (do índice 7 até o final)
print(frase[-9:])  # 'versátil.  ' (últimos 9 caracteres)
print(frase[::2])  # 'Ptoéualnugmd rgamçãpdrsaevrái. ' (pula de 2 em 2)

# 2. Análise com len(), count(), find()
print("\nAnálise:")
print(len(frase))               # Comprimento da string (caracteres totais)
print(frase.count("a"))         # Conta quantas vezes a letra 'a' aparece
print(frase.count("a", 10, 30)) # Conta quantas vezes a letra 'a' aparece entre os índices 10 e 30
print(frase.find("linguagem"))  # Encontra a posição da substring 'linguagem' (retorna -1 se não encontrar)
print(frase.find("python"))     # Retorna -1 (não encontra pois é case-sensitive)

# 3. Transformações com replace(), upper(), lower(), capitalize(), title(), strip()
print("\nTransformações:")
nova_frase = frase.replace("Python", "Java")  # Substitui 'Python' por 'Java'
print(nova_frase)

print(frase.upper())         # Transforma a string em letras maiúsculas
print(frase.lower())         # Transforma a string em letras minúsculas
print(frase.capitalize())    # Capitaliza a string (primeira letra maiúscula)
print(frase.title())         # Capitaliza cada palavra

print(frase.strip())         # Remove espaços em branco no início e no final
print(frase.rstrip())        # Remove espaços em branco somente à direita
print(frase.lstrip())        # Remove espaços em branco somente à esquerda

# 4. Junção com join()
print("\nJunção:")
palavras = frase.split()     # Divide a string em uma lista de palavras
print(palavras)
frase_junta = "-".join(palavras)  # Junta as palavras com '-' como separador
print(frase_junta)
