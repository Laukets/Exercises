xs = [48,117,200,240,160,260,220,-30]

def desenhaBarra(t, altura):
    if altura >= 200:
        t.fillcolor("red")
    elif 100 <= altura < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

    t.begin_fill()
    t.left(90)
    t.forward(altura)
    t.write(" " + str(altura))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()

for a in xs:
    desenhaBarra(alex, a)

if altura >= 200:
    t.fillcolor("red")
elif 100 <= altura < 200:
    t.fillcolor("yellow")
else:
    t.fillcolor("green")