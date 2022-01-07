import random

def substituicao(aString):
    changeAtoQ = aString.replace('a', 'q') # substitue a letra A por Q
    changeBtoT = changeAtoQ.replace('b', 't') # substitue a letra B por T
    changedString = changeBtoT.replace('c', 'g') # substitue a letra C por G
    return changedString

def codification(message, mapa):
    '''
    substitue as letras da mensagem por letras aletórias não repetidadas de uma lista 
    '''
    done = []
    i = 0
    text = message
    while i < len(mapa):
        for char in text:
            item = random.choice(mapa)
            if char in mapa:
                if item not in done:
                    done.append(item)
                    i = i + 1
                    change = text.replace(char, item)
                    text = change
        
    return text


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
lyric = '''And i'm praying that we will see something there in between then and there that exceeds all we can dream and all these twisted thoughts I see Jesus there in between'''

print(codification(lyric,alphabet))

