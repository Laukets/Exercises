ref_arquivo = open(r"C:\Users\gamers\OneDrive\TI\qbdata.txt")

linha = ref_arquivo.readline()

while linha:
    valores = linha.split()
    print('QB ', valores[0], valores[1], 'obteve a avaliação ', valores[10])
    linha = ref_arquivo.readline()

ref_arquivo.close()