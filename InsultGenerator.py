"""
Jasmyne Roberts @ GenCyber
6 July 2016
This is a random insult generator
"""

import random

def insult():
    intro = "Welcome to the Insult Generator,"
 
    adj = ["silly", "hairy", "lumpy", "smushy", "smelly", "sickening", "slippery", "bumbling", "artless", "infectious", "saucy", "vain"]
    noun1 = ["couch", "arm", "sag", "cat", "grape", "lemon", "lump", "sauce", "chicken"]
    noun2 = ["face", "bear", "blimp", "pig", "potato", "hat", "bag", "mess", "explosion"]
    
    adj = adj[random.randint(0,len(adj)-1)]
    n1 = noun1[random.randint(0,len(noun1)-1)]
    n2 = noun2[random.randint(0,len(noun2)-1)]
    
    insult = intro + " " + adj + " " + n1 + " " + n2 + "."

    print("")
    print("~" * len(insult))
    print(insult)
    print("~" * len(insult))