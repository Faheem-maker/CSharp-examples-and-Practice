#-------------------------------------------------------------------------------
# Name:        Program testing with python
# Purpose:     This program will test the transportation cipher program to make sure that 
#              everything worked
# Author:      faheem-maker
#
# Created:     29/01/2021
# Copyright:   (c) faheem-maker 2021
# Licence:     GNU
#-------------------------------------------------------------------------------
import math, sys,Transposition-cipher, Transposition-cipher-decrypter, random
def main():
    random.seed(42)
    noOfTests = 20
    for i in range(noOfTests):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print('Test #%s: "%s..."' % (i + 1, message[:50]))
        for key in range(1,int(len(message)/2)):
            encrypted = encrypter.encrypt(key,message)
            decrypted = Automation.decrypt(key,encrypted)
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key,message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
    print('Transposition cipher test passed.')
if __name__ == '__main__':
    main()