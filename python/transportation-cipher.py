#------------------------------------------------------------------------------
#Author:            faheem-maker
#purpoes            this program uses transportation cipher to turn your simple text 
#                   into an unreadable string which can be only decrypted using the
#                   same key. this program does not use any modules, but you will 
#                   have to change the value of message and key to encrypt your strings
#lisence:           GNU GENERAL PUBLIC LICENSE
#required:          python3
#Note:              Although transportation cipher is much more stronger than ceaser
#                   cipher(an example of ceaser cipher is avalible too) but you
#                   should not use these ciphers to protect your actual files
#-------------------------------------------------------------------------------
def encrypt(key,message):
    cipherText = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex += key
    return  ''.join(cipherText)
def main():
    message = 'Common sense is not so common.'
    key = 8
    translated = encrypt(key,message)
    print(translated+'|')
if __name__ == '__main__':
    main()