#-------------------------------------------------------------------------------
# Name:        Ceaser cipher with python
# Purpose:     Ceaser cipher turns simple text into an unreadable string and then turn it back
#              using the same key
# Author:      faheem-maker
#
# Created:     29/01/2021
# Copyright:   (c) faheem-maker 2021
# Licence:     GNU
#-------------------------------------------------------------------------------
#Note:
#this project uses a third party module called "pyinputplus"
#install it before you run the program
#to install it, enter the command in command prompt "pip install pyinputplus"
import pyinputplus as pyip
message = pyip.inputStr("Enter the message to encrypt/decrypt\n")
SYMBOLS =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
key = pyip.inputInt("Enter your key, max 65:",max=65, min=1)
mode = pyip.inputChoice(['e','d'],"Enter the mode\ne --> encrypt/translate to secret code\nd --> decrypt/translate to text\n")
translated = ""
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'e':
            translatedIndex = symbolIndex + key
        else:
            translatedIndex = symbolIndex - key
        if translatedIndex > len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print("The encrypted/decrypted text is :\""+translated+"\" with key#",key)