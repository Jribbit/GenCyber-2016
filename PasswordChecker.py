# -*- coding: utf-8 -*-
"""
Jasmyne Roberts @ GenCyber

Created on Thu Jul  7 12:43:27 2016

PasswordChecker.py: Write a method to check whether a password follows these rules:
    - Must be at least 6 characters long
    - Must contain at least one capital letter
    - Must contain at least one lowercase letter
    
If password fulfills all the requirements return a bool.
"""

def pwcheck(pw):
    if len(pw) >= 6:
        for x in pw:
            if x.isupper() == True:
                for y in pw:
                    if y.islower() == True:
                        print("This is a good password!")
                        return True
    print("Please create a better password.")
    return False
        
pw = input("Enter password: ")
pwcheck(pw)