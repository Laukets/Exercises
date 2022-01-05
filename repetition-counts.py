def count(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount = lettercount + 1
    return lettercount

print(count('accommodations','a'))

def find(aString, aChar):
    '''
    encontra indice do caracter na string
    se não encontrado retorna -1
    '''
    ix = 0
    found = False
    while ix < len(aString) and not found:
        if aString[ix] == aChar:
            found = True
        else:
            ix = ix + 1
    if found:
        return ix
    else:
        return -1

print(find('accommodation', 'x'))

def find2(astring, achar, start):
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix =ix + 1
    if found:
        return ix
    else:
        return -1


print(find2('banana', 'n', 3))

def find3(astring, achar, start=0):
    ix = start
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix =ix + 1
    if found:
        return ix
    else:
        return -1

print(find3('banana', 'a'))

def find4(astring, achar, start=0, end=0):
    ix = start

    if end == None:
        end = len(astring)

    found = False

    while ix < end and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix =ix + 1
    if found:
        return ix
    else:
        return -1

ss = 'Python strings have some interesting methods.'

print(find4(ss, 's', 8, 13))
