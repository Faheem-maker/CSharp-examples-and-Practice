#-------------------------------------------------------------------------------
#Author:            faheem-maker
#lisence:           GNU GENERAL PUBLIC LICENSE
#purpoes:           this program decrypts the text encrypted with transformation cipher
#                   using your key
#Required:          python3
#Note:              You will have to replace the values of myMessage and myKey with  
#                   your message and your key for the code to function correctly
#--------------------------------------------------------------------------------
import math
def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8
    plainText = decrypt(myKey,myMessage)
    print(plainText+'|')

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

if __name__ == '__main__':
    main()