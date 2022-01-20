eng2pt = {}
eng2pt['one'] = 'um'
eng2pt['two'] = 'dois'
eng2pt['three'] = 'três'
eng2pt['four'] = '4'
print(eng2pt)
print(eng2pt['one'])
eng2pt['four'] = 'quatro'
print(eng2pt['four'])

print('\n')

# METHODS

a = eng2pt.keys()
print(a)

b = eng2pt.values()
print(b)

c = eng2pt.items()
print(c)

d = eng2pt.get('one')
print(d)

e = eng2pt.get('five',0) # se não encontrado chave na lista retorn zero
print(e)


print('\n')

inventario = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for key in inventario.keys():
    print('Fruta: ', key, '\tQuantidade:', inventario[key])

for k in inventario:
    print('Fruta: ', k)

for (k,v) in inventario.items():
    print('We have ', v, k)

keylist = list(inventario.keys())
keylist.sort()
print(keylist)