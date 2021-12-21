import turtle
wn = turtle.Screen()
tess = turtle.Turtle() # chama o construtor da classe Trutle q retorna um objeto turtle
tess.color('hotpink')
alex = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

alex.left(180)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.right(90)
alex.forward(50)
alex.right(90)

lara = turtle.Turtle()
for i in [0,1,2,3]: # são 4 valores quaisquer
    lara.forward(200)
    lara.left(90)

for aColor in ['yellow', 'red', 'purple', 'blue']: # nesse caso muda de cor a cada execução do comando
    alex.color(aColor)
    alex.forward(150)
    alex.left(90)

for i in range(4):
    alex.forward(250)
    alex.left(90)

wn.exitonclick()