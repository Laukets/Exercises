# imprime cada frase com um determinado mes da lista
meses = ["janeiro", 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
for item in meses:
    print(f"Um dos meses do ano é {item}.")

# imprime a frase 3 vezes
for i in range(3):
    print("eu gosto da tartarugas do Python!")

# imprime cada item da lista em uma linha
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)
# imprime o quadrado de cada item da lista
for item in xs:
    print(item**2)

# desenha um triangulo equilatero com a tartaruga
import turtle
wn = turtle.Screen()
alex = turtle.Title()
for i in range(3):
    alex.forward(80)
    alex.left(120)

for i in range(4):
    alex.forward(50)
    alex.left(90)

for i in range(6):
    alex.forward(50)
    alex.left(60)

for i in range(8):
    alex.forward(50)
    alex.left(45)

angulos = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for item in angulos:
    alex.forward(100)
    alex.left(item)

for i in range(12):
	alex.forward(5)
	alex.up()
	alex.forward(45)
	alex.down()
	alex.forward(10)
	alex.left(180)
	alex.up()
	alex.forward(60)
	alex.right(150)
	alex.down()



def desenhaQuad(t, tam):
	for tam in range(4):
		t.forward(tam)
		t.left(90)


for q in range(5):
    # faz a tartaruta desenhar 5 quadrados um ao lado do outro
	desenhaQuad(alex,20)
	alex.up()
	alex.forward(30)
	alex.down()

import math
t = 20
d = math.pow(200,1/2)

#for i in range(5):
	# a tartaruga desenha um quadrado dentro do outro
#	desenhaQuadrado(geo,t)
#	geo.up()
#	geo.right(135)
#	geo.forward(d)
#	geo.left(135)
#	geo.down()
#	t = t + 20


f = 2
for i in range(20):
	# cria uma espiral quadrada
	alex.right(90)
	alex.forward(f)
	f = f + 2

for i in range(150):
	#desenha espiral quadrada com linhas de perseguição
	turtle.right(90.5)
	turtle.forward(f)
	f = f + 2

for i in range(20):
	geo.right(90)
	geo.forward(f)
	f = f + 2

def desenhaQ(t, tam):
	#faz um quadrado
	for q in range(4):
		t.left(90)
		t.forward(tam)

for j in range(5):
	#faz uma estrela de quadrados
	for i in range(4):
		desenhaQ(alex, 60)
		alex.right(90)

	alex.left(18)
