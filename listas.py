num = [17, 123, 87, 34, 66, 8398, 44, 'gato', 'cachorro', [], [10, True], False]

a = num[len(num)-1]

b = num[7].upper()

c = num[7][0] # retorna caracter no indice 0 da string no indice 7 da lista

d = 57 in num # 57 é um item da sublista e nao da lista externa

e = [0]*4
f = num + [3.14, 3.65]

g = id(num)

num[1:3] = ['x', 'y'] # modifica os itens no intervalo indicado
num[1:3] = [] # remove os intes no intervalo indicado
num[4:4] = ['e'] # acrescenta sem substituir nenhum item

del num[1] # deleta item indicado

lista = [81,82,83]
h = lista
'''print(lista is h) # retorna True
h[0] = 5
print(lista) # retorna lista modificada'''

i = lista[:]
'''print(i is lista) # retorna False
i[0] = 4
print(i)
print(lista)'''

j = [num] * 3 # lista de listas, se modificar a lista num interfere na lista j
print(j)

listaOrig = [45, 32, 88]
print(id(listaOrig))

listaOrig = listaOrig + ['gato'] # é necessãrio inserir a str em uma lista para haver a concatenação
print(listaOrig)
print(id(listaOrig)) # são diferentes ids se usamos concatenação


# METHODS

num.append('banana') # add item (o id é o mesmo se usarmos o append)
print(num) 

print(num.count(17))

print(num.index(44))

num.insert(4,5354) # add item no indice indicado em remover item algum
print(num)

print(num.pop()) # remove ultimo item da lista

print(num.pop(9)) # remove item do indice indicado e o retorna

num.remove([])
print(num) 

num.reverse() # inverte ordem dos itens
print(num)

num.clear() # remove todos os itens da lista
print(num)