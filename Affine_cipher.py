# How Affine cipher works?
# Affine cipher has two keys, key a and b
# The following steps are followed to encrypt to Affine cipher
# 1) Multiply the index of the letter with key a
# 2) Add key b to the product
# 3) mod the result by the length of all symbols

import random, sys

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def main():
    translated = ""
    myMessage = """""5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRL
QQQQQQQQQQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN\"
QQQQQQQQQQ-5!1RQP36ARu
"""  # Message that will be encrypted/decrypted
    myKey = 2894  # key tp use while encrypting/decrypting
    myMode = 'decrypt'  # set to either encrypt or decrypt
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % myKey)
    print('%sed text:' % (myMode.title()))
    print(translated)


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def checkKey(keyA, keyB, mode):
    if (keyA == 1 or keyB == 0) and mode == "encrypt":
        sys.exit("Cipher is weak, Choose a different key")
    if keyA < 0 or keyB < 0 or keyB > (len(SYMBOLS) - 1):
        sys.exit("Key A must be greater than 0 and Key B must be between 0 and %s." % (len(SYMBOLS) - 1))
    if gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (
            keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKey(keyA, keyB, 'encrypt')
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol
    return cipherText


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKey(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plainText += symbol
    return plainText


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, keyB) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == "__main__":
    main()
