import turtle
'''
def desenhaQuadrado(t, tam):
    for tam in range(4):
        t.forward(tam)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
desenhaQuadrado(alex,50)

tess = turtle.Turtle()
for i in range(15):
    desenhaQuadrado(tess, tamanho)
    tamanho = tamanho + 10
    tess.forward(10)
    tess.right(18)
'''


def quadrado(x): # retorna o valor  calculado em return
    return x*x

#quadrado(9)

def square(x): #não returna nada
    y = x*x
    print(y)


aQuadra = 10
'''
resultado = square(aQuadra)
print(resultado) # imprime None pois a função square não retorna nada
'''

def qua(x): # calcula o quadrado de x
    soma = 0
    for count in range(x):
        soma = soma + x
    return soma

#valor = int(input("digite o valor para a multiplicação: "))
#print(qua(valor))


def somaQuadrados(x, y, z):
    a = quadrado(x)
    b = quadrado(y)
    c = quadrado(z)
    return a+b+c

a = 2
b = -45
c = 542

resultado = somaQuadrados(a, b, c)
print(resultado)

def densenhaRetangulo(t, w, h):
    if w == h:
        for i in range(4):
            t.forward(w)
            t.left(90)
    else:
        for i in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)



w = input("entre com a largura: ")
h = input("entre com a altura: ")
larg = int(w)
alt = int(h)

alex = turtle.Turtle()

densenhaRetangulo(alex, larg, alt)

def desenhaPoli(t, numSides, sideLength):
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)

def desenhaTrianguloEqui(t, tam):
	desenhaPoli(t, 3, tam)


def somaAte(n):
	# fatorial
	for i in range(n):
		i = n * (n+1) // 2
	return i

    

def someAte(n):
    j = 0
    for i in range(n+1):
        j = j + i
    return j


def compare(a,b):
    if a > b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

compare(4,5)

def hipotenusa(a,b):
    return 


def inclinacao(x1,y1,x2,y2):
    # retorna o angulo de inclinação da reta
    return (y2-y1)/(x2-x1)

def intersecta(x1,y1,x2,y2):
    coeficiente = inclinacao(x1,y1,x2,y2)
    inter = y1 - (coeficiente * x1)
    return inter


def f2c(t):
    #converte fahrenheit para celsius
    return (t - 32) * (5/9)

def c2f(t):
    # converte celcius para fahrenheit
    return (t * 9/5) + 32
