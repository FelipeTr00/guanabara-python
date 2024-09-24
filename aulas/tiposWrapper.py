#####################
# LISTA

# Criando uma lista
frutas = ['maçã', 'banana', 'laranja']

# Acessando elementos
print(frutas[0])  # 'maçã'

# Modificando elementos
frutas[1] = 'uva'

# Adicionando elementos
frutas.append('morango')

# Removendo elementos
frutas.remove('laranja')

print(frutas)  # ['maçã', 'uva', 'morango']

#####################
# TUPLA

# Criando uma tupla
cores = ('vermelho', 'azul', 'verde')

# Acessando elementos
print(cores[1])  # 'azul'

# Tentativa de modificar um elemento (gera erro)
# cores[1] = 'amarelo'  # TypeError: 'tuple' object does not support item assignment

######################
# SET

# Criando um conjunto
numeros = {1, 2, 3, 4, 4}

# Acessando elementos (não possível por índice, pois não são ordenados)
print(numeros)  # {1, 2, 3, 4}

# Adicionando elementos
numeros.add(5)

# Removendo elementos
numeros.remove(2)

# União de conjuntos
outro_conjunto = {3, 6, 7}
uniao = numeros.union(outro_conjunto)

print(uniao)  # {1, 3, 4, 5, 6, 7}

######################
# DICTIONARY DICT

# Criando um dicionário
aluno = {
    'nome': 'Maria',
    'idade': 22,
    'curso': 'Engenharia'
}

# Acessando valores
print(aluno['nome'])  # 'Maria'

# Modificando valores
aluno['idade'] = 23

# Adicionando novos pares
aluno['matricula'] = '2023001'

# Removendo pares
del aluno['curso']

print(aluno)  # {'nome': 'Maria', 'idade': 23, 'matricula': '2023001'}


######################
# NONE TYPE

resultado = None  # Indica que ainda não há valor definido
print(resultado)  # None
