# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:43:01 2016

Jasmyne Roberts @ GenCyber

"""
from random import randint

class Pokemon:
    # Pokemon traits
    def __init__(self, name, kind, hp, moves):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.cp = randint(1,600)
        self.moves = moves
        
    def about(self):
        print()
        print("About " + self.name + ": ")
        print("  - Type: " +  self.kind)
        print("  - Hp: " + str(self.hp))
        print("  - Cp:", str(self.cp))
        
    def battle(self, myMove, opponent, opponentMove):
        print("\n" + "BATTLE: " + self.name + " versus " + opponent.name + ":")
        print(self.name + " used " + myMove + "!")
        print(opponent.name + " has " + str(opponent.hp) + " hp left!")
        attackDamage = (self.moves[myMove]) * self.cp
        opponent.hp -= attackDamage
        if opponent.hp <= 0:
            print(opponent.name + " died! You win!")
            return
        print(opponent.name + " used " + opponentMove + "!")
        print(self.name + " has " + str(self.hp) + " hp left!")
        attackDamage = (opponent.moves[opponentMove]) * opponent.cp
        self.hp -= attackDamage
        if self.hp <= 0:
            print(self.name + " died! " + opponent.name + " wins!")
            return
        print("DRAW!")
        
evey_moves = {"Speak": 500, "Charge" : 15}
a = Pokemon("Evey", "Normal", 10, evey_moves)

v_moves = {"Slice": 100, "Speak": 50}
b = Pokemon("V", "Fighting", 100, v_moves)

head_moves = {"Declare War": 50, "Body Guard": 30}
c = Pokemon("Head", "Bossy", 10, head_moves)

a.battle("Charge", b, "Speak")
a.about()
b.about()