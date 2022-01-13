
minhaLista = [1, 2, 3, 4, 5]

quadrado = [item ** 2 for item in minhaLista]

print(quadrado)

print('\n')

def primosAte(n):
    listaPrimos = [num for num in range(2,n) if primo(num)]
    return listaPrimos