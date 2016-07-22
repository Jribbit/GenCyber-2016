# -*- coding: utf-8 -*-
"""
Jasmyne Roberts @ GenCyber

7 July 2016

Pine Tree.py (Parina's Homework)

Write a program that, given an integer n and m, draws a ‘pine tree’ consisting of n
triangles formed by a character of user’s choice, ie., ‘*’,’+’, etc. ‘m’ specifies the number
of spaces this triangle should shift from the left margin.
Your program should consist of three functions:
1) a function that draws a triangle, given an integer,
2) a function that draws the tree given n, m and character to be drawn, and
3)a driver function that interacts with the user, ie., prompts for input of n, m and the
character to be drawn.
"""
## n = number of triangles
## m = space shift from margin
## symbol to draw


def triangle(height, sym, tspace, m):
    for x in range(height - 1):
        lspace = height - x - 1
        space = lspace + tspace + m
        line = x * 2 + 1
        print(" " * space + sym * line)
        
def tree(n, sym, m):
    for x in range(n):
        tspace = n - x - 2
        triangle(3 + x, sym, tspace, m)
    
def begin():
    print()
    print("Welcome to the pine tree maker!")
    n = int(input("How many triangles would you like in your tree? "))
    m = int(input("How many spaces from the left margin should your tree be? "))
    sym = input("What symbol do you want your tree to consist of? ")
    tree(n, sym, m)
    
begin()