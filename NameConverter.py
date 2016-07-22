# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:20:47 2016

@author: student
"""

def asciihex(name):
    print("Hex Name: ", end="")
    for x in name:
        if x.isalpha() == True:
            x = ord(x)
            x = hex(x)
        print(x, end=" ")
        
n = input("Name: ")
asciihex(n)