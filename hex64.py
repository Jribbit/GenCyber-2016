# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:08:22 2016

Cryptopals Set 1 Challenge 1

This program converts a hexadecimal string into base64.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:54:08 2016

@author: student
"""

def hex64(string):
    """ Converts hex string to binary string """
    num = str(bin(int(string, 16)))
    num = num.replace("b", "")
#    print(num)
    """ Makes string evenly divisible by 6 """
    while not((len(num) - 2) % 6 == 0):
        num = num + "0"
    for x in range(0, len(num) - 2, 6):
        """ Each new character in string will be made up of 3 bits """
        index = num[x:x+6]
#        print(index, end = " ")
        """ Converts binary strings to decimal number"""
        index = int(index, 2)
#        print(index, end = " ")
        """ Decides what character the integer will be """
        if index <= 25:
            index = chr(index + 65)
        elif index <= 52:
            index = chr(index + 71)
        elif index <= 61:
            index = str(index - 52)
        elif index == 62:
            index = "+"
        else:
            index = "/"
        print(index, end = "")
 
  
#hex64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")