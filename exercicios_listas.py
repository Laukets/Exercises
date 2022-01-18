def somaQaudrados(xs):
    soma = 0
    for item in range(len(xs)):
        xs[item] = 2 * xs[item]
        soma = soma + xs[item]
    return soma

lista = [2,3,4]
print(somaQaudrados(lista))


def numImpar(l):
    impares = []
    for i in range(len(l)):
        if l[i] % 2 != 0:
            impares.append(l[i])
    if len(impares) == 0:
        return 'Não há números ímpares desta lista.'
    else:
        return impares

print(numImpar(lista))

lista = [2,3,4]
print(numImpar(lista))

def numPar(l):
    pares = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            pares.append(l[i])
    if len(pares) == 0:
        return 'Não há números pares nesta lista.'
    else:
        return pares

print(numPar(lista))
lista = [1,3,5]
print(numPar(lista))

def numNegative(l):
    negativos = []
    for i in range(len(l)):
        if l[i] < 0:
            negativos.append(l[i])
    if len(negativos) == 0:
        return 'Não há números negativos nesta lista.'
    else:
        return negativos

print(numNegative(lista))
lista = [-1,0,2]
print(numNegative(lista))

def strComprimentoCinco(l):
    num = 0
    for i in range(len(l)):
        if len(l[i]) == 5:
            num = num + 1
    if num == 0:
        return print('Não há palavras com 5 letras nesta lista.')
    else:
        return print(f'Há {num} palavras com 5 letras nesta lista.')

strings = ['alfabeto', 'palavra', 'termo', 'afeto', 'transição']

strComprimentoCinco(strings)

def soma(l):
    ''' recebe uma lista de inteiros e soma todos os itens excluindo a 1° numero par'''
    ix = 0
    some = 0
    found = False
    while ix < len(l) and found == False:
        if l[ix] % 2 == 0:
            exclui = ix
            found = True
        else:
            ix = ix + 1
    for i in range(len(l)):
        if i != exclui:
            some = some + l[i]
    return some

lista = [1,2,3,4]
print(soma(lista))