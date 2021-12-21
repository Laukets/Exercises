#print(16-2*5//3+1) # ele calcula assim: 16-((2*5)//3)+1
#print(2**2**3*3) # ele calcula assim: (2**(2**3))*3
#print(0%7)

#print(6*1-2)
#rint(6*(1-2))

import math
#print(math.pi)
#print(math.e)
#print(math.sqrt(2))
#print(math.sin(math.radians(90))) # seno de 90

#print(max(3*11, 5**3, 512-9, 1024**0)) # retorna o maior valor da lista

def infosCirculo(r):
    """ (numero) -> (float,float)
    Recebe um número r e retorna a circunferência
    e a área do círculo de raio r.
    """
    circunferencia = 2 * math.pi * r
    area = math.pi * r * r
    return circunferencia

print(infosCirculo(10))
