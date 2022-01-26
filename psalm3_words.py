from itertools import count


def countWords():
    ref_arquivo = open(r'C:\Users\gamers\OneDrive\TI\Python\psalm3.txt')
    arquivo = ref_arquivo.read()
    word_list = arquivo.split()
    word_count = {}
    for word in word_list:
        if word not in word_count:
            conta = word_list.count(word)
            word_count[word] = conta
    ref_arquivo.close()
    for i in word_count.keys():
        print(i,':',word_count[i])

countWords()