#-------------------------------------------------------------------------------
# Name:        File encrypter/decrypter
# Purpose:     this program is same as the transportation-cipher program
#              but this one could encrypt/decrypt whole files! not only
#              a string. change the values of input file(the file which
#              contains the data to be encrypted/decrypted) and outfile(
#              the file to write to) in order for it to function correctly.
# Author:      faheem-maker
#
# Created:     29/01/2021
# Copyright:   (c) faheem-maker 2021
# Licence:     GNU
#-------------------------------------------------------------------------------
import time, os, sys, math
def encrypt(key,message):
    cipherText = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key
    return  ''.join(cipherText)

def decrypt(key,message):
    numOfColumns = int(math.ceil(len(message)/ float(key)))
    noOfRows = key
    noOfShadedBoxes = (numOfColumns * noOfRows) - len(message)
    plainText = [''] * numOfColumns
    columns = 0
    rows = 0
    for symbol in message:
        plainText[columns] += symbol
        columns += 1
        if (columns == numOfColumns) or (columns == numOfColumns -1 and rows >= noOfRows - noOfShadedBoxes):
            columns = 0
            rows += 1
    return ''.join(plainText)

def main():
    inputFileName = 'encrypted.txt'
    outputFileName = 'secret.txt'
    myKey = 12
    myMode = 'decrypt'
    if not os.path.exists(inputFileName):
        print("Input file not found! Quitting...")
        sys.exit()
    elif os.path.exists(outputFileName):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %(outputFileName))
        x = input().lower()
        if x.startswith('q'):
            sys.exit()
    fileObj = open(inputFileName,'r')
    content = fileObj.read()
    fileObj.close()
    print('%sing...' % (myMode.title()))
    startTime = time.time()
    if myMode =='encrypt':
        translated = encrypt(myKey,content)
        totalTime = round(time.time() - startTime,2)
        print('%sion time: %s seconds' % (myMode.title(), totalTime))
        fileObj = open(outputFileName,'w')
        fileObj.write(translated)
        fileObj.close()
    elif myMode == 'decrypt':
        translated = decrypt(myKey, content)
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (myMode.title(), totalTime))
        fileObj = open(outputFileName, 'w')
        fileObj.write(translated)
        fileObj.close()

if __name__ == '__main__':
    main()