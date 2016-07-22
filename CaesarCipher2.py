# -*- coding: utf-8 -*-
"""
Jasmyne Roberts @ GenCyber

8 July 2016

Caesar Cipher: encrypt and decrypt messages by shifting a letter's ASCII number by the key
"""

def encrypt(text, key):
    for x in text:
        if x.isalpha() == True:
            if x.isupper() == True:
                x = (ord(x) - 65 + key) % 25 + 65
            else:
                x = (ord(x) - 97 + key) % 25 + 97
            print(chr(x), end="")
        else:
            print(x, end="")
    print()
            
#text = input("Enter text: ")
#key = int(input("Enter key: "))
#state = int(input("Would you like to 1 (encrypt) or 2 (decrypt)? "))

#if state == 2:
#    key = key * -1
for x in range(25):
    print(str(x) + ": ", end="")
    encrypt("GNINEIGNOLRJNRGKn", x)
    #encrypt("znk lujk oy utk totk zcu yod.", x)
    #encrypt("rku corr tkbkx lotj noy vxkiouay uyigx gy o ngbk nojjkt oz ot znk rgyz vrgik nk cuarj kbkx ruuq! Tkoznkx corr nk xkgrofk oz oy sk lux o ngbk joyvuykj ul gte kbojktik gmgotyz sk gngngngng -S", x)
