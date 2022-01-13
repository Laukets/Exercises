# tuplas são úteis para registros

tupla = ('Fernanda', 'Montenegro', 1929, 'Central do Brasil', 1998, 'Atriz', 'Rio de Janeiro - RJ')
print(tupla[2])
print(tupla[2:6])

a = tupla[:3] + ('Boa Sorte', 2014) + tupla[5:]
print(a)

b = (5,)
print(type(b))
c = (5)
print(type(c))

print('\n')

# Atribuição de Tuplas
(nome, sobrenome, anoNasc, filme, anoFilme, profissao, localNasc) = tupla
print(nome)

print('\n')

def circuloInfo(raio):
    circun = 2 * 3,14159 * raio
    area = 3,14159 * (raio ** 2)
    return (circun, area)

print(circuloInfo(10))