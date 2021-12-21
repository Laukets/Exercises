def desenhaEstrelaImpar(t, numPontas, tamLado):
    # a tartaruga faz apena estrelas com numero de pontas impar
    angulo = 180 - (180/numPontas)
	for i in range(numPontas):
		t.forward(tamLado)
		t.left(angulo)

#def desenhaEstrelaPar(t, numPontas, tamLado):
#    angulo = 360 - numPontas
#	num = numPontas + 1
#	for i in range(num):
#		t.forward(tamLado)
#		t.left(angulo)
#!!!!!!!!ESTA ERRADO!!!!!!!!!

def estrelaSeisPontas(t, tam):
    for i in range(7):
        t.forward(tam)
        t.left(103)