musica = 'Eduardo e Monica um dia se encontraram sem querer'

a = musica.split() # converte string em lista
print(a)

b = musica.split('se') # o delimitador não aparece
print(b)

c = ' '.join(a) # converte lista em string | a lista não é modificada
print(c)

print('\n')

escritora = 'Carolina Maria de Jesus'
listaNome = escritora.split()
inic = ''
for nome in listaNome:
    inic = inic + nome[0]
print(inic)

print('\n')

d = list('Python')
print(d)

# SPLIT quebra uma str em uma lista de palavras | LIST quebra uma str em uma lista de caracteres

