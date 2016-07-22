# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:54:08 2016

@author: student
"""
def encode(list):
    for x in range(len(list)):
        index = int(list[x], 2)
        if index <= 25:
            index = chr(index + 65)
        elif index <= 52:
            index = chr(index + 71)
        elif index <= 61:
            index = str(index - 53)
        elif index == 62:
            index = "+"
        else:
            index = "/"
        print(index, end = "")
    


def hex64(string):
    indexlist = []
    num = str(bin(int(string, 16)))
    while not((len(num) - 2) % 6 == 0):
        num = num + "0"
    for x in range(2, len(num) - 2, 6):
        index = num[x:x+5]
        indexlist.append(index)
    encode(indexlist)
 
#hex64("4d616e")   
hex64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")