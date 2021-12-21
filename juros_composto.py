p = 10000
n = 12
r = 0.08
t1 = input("entre com o numero de anos: ")
t = int(t1)

a = p * ((1 + r/n) ** (n*t))

print(f"O juros composto é de {a:.2f}.")