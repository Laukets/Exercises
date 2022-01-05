def eightDucks():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    middlefield = 'u'

    for p in prefixes:
        if p == 'O' or p == 'Q':
            print(p + middlefield + suffix)
        else:
            print(p + suffix)


lyric = '''And I'm praying that we will see something there in between then and there that exceeds all we can dream and all these twisted thoughts I see Jesus there in between'''

def find(text, char):
    lista = text.split()
    newList = []
    for ix in lista:
        st = 0
        string = ix
        found = False
        while st < len(string) and not found:
            if string[st] == char:
                found = True
            else:
                st = st + 1
        if not found:
            newList.append(string)
    return print('Seu texto contém ', len(lista), ' palavras, das quais ', len(lista) - len(newList), ' contém a letra ', char, '.')

find(lyric, 'e')