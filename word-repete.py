def wordOccurence(text):
    stringList = text.split()
    repeatedWord = []
    for item in stringList:
        count = stringList.count(item)
        if count > 1:
            repeatedWord.append(item)
    return print(f'Palavras repetidas: {repeatedWord}')

lyric = '''And I'm praying that we will see something there in between then and there that exceeds all we can dream and all these twisted thoughts I see Jesus there in between'''

wordOccurence(lyric)