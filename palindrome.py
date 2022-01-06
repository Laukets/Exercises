def reverse(s):
    r = []
    for i in range(len(s) - 1, -1, -1):
        # iteração da direita para esquerda
        r.append(s[i])
    s = ''.join(r)
    return s

def palindrome(s):
    p = reverse(s)
    if p == s:
        return print('Esta palavra é um palíndromo.')
    else:
        return print(p)
    

print(reverse('abacaxi'))
palindrome('abacaxi')