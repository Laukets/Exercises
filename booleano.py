def eDivisivel(x,y):
    if x % y == 0:
        return True
    else:
        return False

if eDivisivel(10,5):
    print('that works!')
else:
    print('those values are not good!')

def nDivisivel(x,y):
    return x % y == 0

#nDivisivel(1,5)

def notaResult(nota):
    if nota >= 90:
        result = "A"
    elif nota >= 80 and nota < 90:
        result = "B"
    elif nota >= 70 and nota < 80:
        result = "C"
    elif nota >=60 and nota < 70:
        result = "D"
    else:
        result = "F"
    return result

xs = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]

for i in xs:
    print(notaResult(i))

def é_par(n):
    if n%2 == 0:
        return True
    else:
        return False

def é_ímpar(n):
    num = é_par(n)
    if num == False:
        return True
    else:
        return False

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        return True
    else:
        return False