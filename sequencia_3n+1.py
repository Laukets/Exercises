def seq3nplus1(n):
    while n!=1:
        print(n)
        if  n%2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)

seq3nplus1(32)

'''
aparentemente qualquer valor inteiro positivo de n termina no valor 1
mas isso ainda nao pode ser afirmado
pois ainda ninguém conseguiu descobrir
se é uma verdade absoluta

se o valor inicial é um potencia de 2
o valor de n será par em todas as iterações do loop
até atingir o valor 1
'''