def someAte(limite):
    '''retorna o fatorial do limite'''
    soma = 0
    numero = 1
    while numero <= limite:
        soma = soma + numero
        numero = numero + 1
    return soma

print(someAte(4))


import random
def isInScreen(tela, turtle):
    '''determina limites para a tartaruga'''

    leftbound = tela.window_width() / 2       #limite da esquerda
    rightbound = tela.window_width() / 2      #limite da direita
    topbound = tela.window_height() / 2       #limite superior
    bottombound = tela.window_height() / 2    #limite inferior

    turtleX = turtle.xcor()
    turtleY = turtle.ycor()

    itIsInside = True

    if turtleX > rightbound or turtleX > leftbound:
        itIsInside = False
    
    if turtleY > topbound or turtleY > bottombound:
        itIsInside = False
    
    return itIsInside


def outAndAbout(tela, turtle):
    ''' a tartaruga passeia de forma aleatoria pela tela'''
    while isInScreen(tela,turtle):
        n = random.randrange(0,2)
        if n == 0:
            turtle.left(90)
        else:
            turtle.right(90)
        turtle.forward(50)

