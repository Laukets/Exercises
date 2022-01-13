def oDobro(lista):
    for position in range(len(lista)):
        lista[position] = 2 * lista[position]

l = [2, 5, 9]

print(l)
oDobro(l)
print(l)

print('\n')

# função pura (não produz side effect)
def dobro(lista):
    novaLista = []
    for i in lista:
        item = 2 * i
        novaLista.append(item)
    return novaLista

print(l)
print(dobro(l))
print(l)

print('\n')