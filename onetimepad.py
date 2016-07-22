# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:13:22 2016

@author: student
"""

def onetimepad(text, pad):
    convertedText = ""
    i = 0
    for letter in text:
        convertedText += chr(ord(pad[i])^ord(text[i])
        i = i + 1
        if i > len(text):
            break
    return convertedText