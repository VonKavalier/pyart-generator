#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys

set1 = ["#","|","-","_","=","/","\\"," "]
set2 = ["(",")","{","}","[","]"]
set3 = ["|","_"," "]
set4 = ["ᚐ","ᚑ","ᚒ","ᚓ","ᚔ"]
set5 = ["▖","▗","▘","▙","▚","▛","▜","▝","▞","▟"]
set6 = ["⋮","⋰","⋱"]
set7 = ["-",".", " "]

sets = [set1, set2, set3, set4, set5, set6, set7]

if len(sys.argv) < 2:
    sys.argv = ['pyart.py',random.randrange(1, len(sets)+1)]

while int(sys.argv[1])>len(sets):
    sys.argv[1] = int(input("Entrez un chiffre entre 1 et " + str(len(sets)) + "\n"))

set_choice = int(sys.argv[1])-1

for i in range(25):
    row = ""
    for j in range(50):
        row += sets[set_choice][random.randrange(0,len(sets[set_choice]))]
    print(row)
