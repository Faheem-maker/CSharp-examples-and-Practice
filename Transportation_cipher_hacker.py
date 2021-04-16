import Transportation_cipher_decryptor
import isEnglish


def main():
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh
          na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
          euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain
          one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp
          ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh
          gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
          aBercaeu thllnrshicwsg etriebruaisss  d iorr"""
    decrypted = hackMessage(myMessage)
    if decrypted is None:
        print("Failed to hack")


def hackMessage(message):
    print("Hacking")
    print("Press CTRL + C(Windows) or CTRL + D(MacOs and Linux) to stop the process at any time")
    for key in range(1, len(message)):
        print('Trying key #%s...' % key)
        decrypted = Transportation_cipher_decryptor.decryptMessage(key, message)
        if isEnglish.isEnglish(decrypted):
            print("Possible encryption hack")
            print('Key %s: %s' % (key, decrypted[:100]))
            print('Enter D if done, anything else to continue hacking:')
            response = input()
            if response.upper().startswith("D"):
                return decrypted
    return None
