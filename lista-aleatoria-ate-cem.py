import random

def listNum():
    '''
    cria uma lista de 100 numeros aleatorios entre 0 e 1000
    '''
    lista = list(range(1001))
    listaFinal = []
    while len(listaFinal) < 100:
        num = random.choice(lista)
        if num not in listaFinal:
            listaFinal.append(num)
    return listaFinal

def media(lista):
    '''
    calcula a media dos valores da lista
    '''
    soma = 0
    for num in lista:
        soma = soma + num
    m = soma / len(lista)
    return m

def maxValor(lista):
    maximo = 0
    for item in lista:
        if item > maximo:
            maximo = item
    return maximo


resultadoMedia = media(listNum())
print(f'A média final é {resultadoMedia}.')

resultadoMax = maxValor(listNum())
print(f'O valor máximo na lista é {resultadoMax}.')

