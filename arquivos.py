def notaMaisQue6():
    ''' abre um arquivo de notas estudantil e imprime o nome dos alunos com mais de 6 notas'''
    ref_arquivo = open(r'C:\Users\gamers\OneDrive\TI\Python\notas_estudante.dat')
    for linha in ref_arquivo:
        lista_linha = linha.split()
        if len(lista_linha) > 7:
            print(lista_linha[0])
    ref_arquivo.close()

def mediaNome():
    ''' abre arquivo e imprime o nome e a media de cada aluno'''
    ref_arquivo = open(r'C:\Users\gamers\OneDrive\TI\Python\notas_estudante.dat')
    for linha in ref_arquivo:
        l_linha = linha.split()
        soma = 0
        for i, v in enumerate(l_linha):
            if i > 0:
                soma = soma + int(v)
        print('Nome: ', l_linha[0], '\tMédia: ', soma)
    ref_arquivo.close()


def notaMinMax():
    ''' abre arquivo, calcula a nota mínima e máxima de cada estudante e imprime'''
    ref_arquivo = open(r'C:\Users\gamers\OneDrive\TI\Python\notas_estudante.dat')
    for linha in ref_arquivo:
        lista_l = linha.split()
        l = []
        for i, v in enumerate(lista_l):
            if i > 0:
                l.append(int(v))
        print('Nome: ', lista_l[0], '\tNota max: ', max(l), '\tNota min: ', min(l))
    ref_arquivo.close()