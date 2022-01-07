def wordOccurence(text):
    stringList = text.split()
    repeatedWord = []
    for item in stringList:
        count = stringList.count(item)
        if count > 1:
            repeatedWord.append(item)
    return repeatedWord

lyric = '''And I'm praying that we will see something there in between then and there that exceeds all we can dream and all these twisted thoughts I see Jesus there in between'''

print(wordOccurence(lyric))

def removeRepeatedWords(text):
    stringList = text.split()
    for item in stringList:
        count = stringList.count(item)
        if count > 1:
            while item in stringList:
                stringList.remove(item)
    newString = ' '.join(stringList)
    return newString

print(removeRepeatedWords(lyric))    
