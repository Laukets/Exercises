def drawSquare (t, sz):
    '''faz a tartaruga desenhar um quadrado de sz'''
    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawTriangle(t, sz):
    '''faz a tartaruga desenhar um triangulo equilatero de sz'''
    for i in range(3):
        t.forward(sz)
        t.left(120)

def drawOctagon (t, sz):
    '''faz a tartaruga desenhar um octogono de sz'''
    for i in range(8):
        t.forward(sz)
        t.left(45)

def drawPolygon(t, sideLength, numSides):
    '''de forma generalizada faz a tartaruga desenhar um poligono'''
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)

import math

def drawCircle(t,r):
    '''a tartaruga faz um circulo'''
    circ = 2 * math.pi * r
    sideL = circ/360
    drawPolygon(t,sideL,360)

def drawCircleCentre(t, r):
    '''a tartaruga faz o circulo centralizado na posição inicial dela'''
    circunf = 2 * math.pi * r
    sideL = circunf / 360
    t.up()
    t.forward(r)
    t.left(90)
    t.down()
    drawPolygon(t, sideL, 360)
    t.up()
    t.left(90)
    t.forward(r)
    t.left(180)

def areaDeCirculo(r):
    area = 2 * math.pi * r
    return area