s = " hello world!"

sc = s.capitalize() # torna o 1° caracter maiúsculo e os outros minúsculos
print(f'capitalize: {sc}')

sce = s.center(10) # add espaços centralizando a string
print(f'center: *{sce}*')

sco = s.count('o') # retorna o n° de ocorrencias do item
print(f'count: {sco}')

senc = s.encode('UTF-8', 'strict') # Return an encoded version of the string as a bytes object. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
print(f'encode: {senc}')

ses = s.endswith('!') # Return True if the string ends with the specified suffix, otherwise return False
print(f'endswith: {ses}')

set = s.expandtabs(4) # Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size
print(f'.\texpandtabs: {set}\t.')

sf = s.find('l') # retorna o indice da 1° ocorrencia do item (busca no sentido crescente)
print(f'find: {sf}')

si = s.index('w') # igual ao find, mas causa erro caso o item nao seja encontrado
print(f'index: {si}')

slen = len(s) # retorna o n° de caracteres da string
print(f'len: {slen}')

slj = s.ljust(10) # add espaços na frente (esquerda) da string
print(f'ljust: *{slj}*')

sl = s.lower() # torna os caracteres minúsculos
print(f'lower: {sl}')

sls = s.lstrip() # remove espaços no inicio da string
print(f'lstrip: {sls}')

sr = s.replace('e','a') # substitui todas as ocorrencias de um caracter por outro
print(f'replace: {sr}')

srf = s.rfind('l') # retorna o indice da ultima ocorrencia do item (busca no sentido decrescente)
print(f'rfind: {srf}')

sri = s.rindex('w') # igual ao rfind, mas causa erro caso o item nao seja encontrado
print(f'rindex: {sri}')

srj = s.rjust(10) # add espaços no fim (direita) da string
print(f'rjust: *{srj}*')

srs = s.rstrip() # remove espaços no fim da string
print(f'rstrip: {srs}')

ss = s.strip() # remove os espaços no começo e no fim
print(f'strip: {ss}')

su = s.upper() # torna os caracteres maiúsculos
print(f'upper: {su}')

last = s[slen-1] 
print(f'ultimo caracter da string: {last}')

lastch = s[len(s)-1]
print(f'last character: {lastch}')

singers = 'Peter, Paul, Mary'
print(singers[0:5])
print(singers[7:11])
print(singers[13:17]) # é exclusivo
print(singers[:3])
print(singers[3:])

print('apple' == 'Apple')
print('apple' < 'Apple')
print(ord('A'))
print(ord('a'))

print('\n')

for um_char in 'python':
    #iteração por item
    print(um_char)

print('\n')

fruta = 'apple'
for idx in range(5):
    currentChar = fruta[idx]
    print(currentChar)

print('\n')

for i in range(len(fruta)):
    print(fruta[i])

print('\n')

for i in range(len(fruta) - 1, -1, -1):
    # iteração da direita para esquerda
    print(fruta[i])

print('\n')

s = 'python rocks'
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])

print('\n')

fruta = 'abacaxi'
position = 0
while position <len(fruta):
    # iteração por item
    # o ultimo caracter acessado é o de indice len(fruta)-1
    print(fruta[position])
    position = position + 1

print('\n')

print('p' in 'apple')
print('i' in 'apple')
print('' in 'a') # o vazio é um substring de qualquer outro string
print('a' not in 'apple') # retorna o valor inverso de in

print("\n")

def removeVogal(s):
    vogal = 'aeiouAEIOU'
    sSemVogal = ''
    for cadaCar in s:
        if cadaCar not in vogal:
            sSemVogal = sSemVogal + cadaCar
    return sSemVogal

print(removeVogal('abacaxi'))

print('\n')

s = 'ball'
r = ''
for item in s:
    # concaternação feita pela esquerda
    r = item.upper() + r
print(r)

print('\n')

