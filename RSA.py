# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:19:12 2016

@author: student
"""

def rsae(plain, e, n):
    c = []
    for x in plain:
        if x.isalpha() == True:
            m = ord(x) - 97
            a = (m ** e) % n
            c.append(a)
    print(c)

def rsad(cipher, d, n):
    m = []
    for y in range(len(cipher)):
        b = (cipher[y] ** d)
        #for y in range(0,100):
            #if b % 8 == 1:
        #print(y)
        m.append(chr(b))
    print(m)

#rsae("i am john", 3, 15)
#rsad([2,0,3,9,14,13,7], 11, 15)
rsad([614, 25, 96, 96, 535], 556, 667)

"""
N = 667
E = 6
D = 556
C = 614  25  96  96  535
Megans
"""

c ** d = m % n