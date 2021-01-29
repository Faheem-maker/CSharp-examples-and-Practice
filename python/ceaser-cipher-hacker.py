#--------------------------------------------------------------------------------------
#Name:              Ceaser cipher hacker
#Purpose:           this program breaks ceaser cipher using brute force
#lisence:           GNU lisence(lisence turms can be found in lisence.txt)
#Required modules:  pyinputplus(install using "pip install pyinputplus)
#howToUse:          this program can creak codes encrypted with ceaser cipher without 
#                   knowing the key, the program will display every possible
#                   key combination
#--------------------------------------------------------------------------------------
import pyinputplus as pyip
message = pyip.inputStr("Enter the text to be cracked")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex > len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print('Key #%s: %s' % (key, translated))