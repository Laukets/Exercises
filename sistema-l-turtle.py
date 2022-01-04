#%%

import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ''
    if ch == 'F':
        newstr = 'F-F++F-F'
    else:
        newstr = ch
    return newstr

def drawLSystem(turtle, string, angle, distance):
    for i in string:
        if i == 'F':
            turtle.forward(distance)
        elif i == 'B':
            turtle.backward(distance)
        elif i == '+':
            turtle.right(angle)
        elif i == '-':
            turtle.left(angle)
        else:
            print('Error: ', i, 'is a unknow command')
        
def main():
    inst = createLSystem(4, 'F')
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLSystem(t,inst,60,5)

    wn.exitonclick()

main()