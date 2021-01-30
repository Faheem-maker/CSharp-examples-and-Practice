UPPER_CASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACES = UPPER_CASE_LETTERS + UPPER_CASE_LETTERS.lower() + '\t\n'

def loadDictionary():
    file = open('dictionary.txt')
    english_words = {}
    for words in file.read().split('\n'):
        english_words[words] = None
    file.close()
    return english_words

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if message == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACES:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message,wordPercentage = 20,letterPercentage = 83):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLetterPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLetterPercentage >= letterPercentage
    return wordsMatch and lettersMatch