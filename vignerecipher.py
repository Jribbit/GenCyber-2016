# -*- coding: utf-8 -*-
"""
Jasmyne Roberts @ GenCyber

8 July 2016

Vignere Cipher: encrypt and decrypt messages by shifting a letter's ASCII number by the keyword
"""

def vignere(text, keyword):
    for x in text:
        if x.isalpha() == True:
                if x.isupper() == True:
                    x = (ord(x) - 65 + (ord(keyword) % len(keyword))) % 25 + 65
                else:
                    x = (ord(x) - 97 + (ord(keyword) % len(keyword))) % 25 + 97
            print(chr(x), end="")
        else:
            print(x, end="")
    print()
            
vignere("revbre cckdcc rev", "gary")