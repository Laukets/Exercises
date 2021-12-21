def distancia(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    d = dx**2 + dy**2
    result = d**0.5
    return result


def area(raio):
    b = 3.1415 * raio**2
    return b


def area2(xc,yc,xp,yp):
    raio = distancia(xc,yc,xp,yp)
    result = area(raio)
    return result

print(area2(1,2,4,6))