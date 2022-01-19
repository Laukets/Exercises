ref_arquivo = open(r"C:\Users\gamers\OneDrive\TI\qbdata.txt")

linha = ref_arquivo.readline() # 1 linha por vez

arquivo = ref_arquivo.read() # todas as linhas do arquivo, exceto a 1° linha

''' Para abrir o arquivo desde a 1° linha é necessário reabri-lo'''

ref_arquivo = open(r"C:\Users\gamers\OneDrive\TI\qbdata.txt")

linha = ref_arquivo.readline() # 1° linha

linha2 = ref_arquivo.readline() # 2° linha

ref_arquivo.close()