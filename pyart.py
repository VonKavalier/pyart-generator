#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys

chars1 = ["#","|","-","_","=","/","\\"," "]
chars2 = ["(",")","{","}","[","]"]
chars3 = ["|","_"," "]
chars4 = ["ᚐ","ᚑ","ᚒ","ᚓ","ᚔ"]
chars5 = ["▖","▗","▘","▙","▚","▛","▜","▝","▞","▟"]
chars6 = ["⋮","⋰","⋱"]
chars7 = ["-",".", " "]

chars = [chars1, chars2, chars3, chars4, chars5, chars6, chars7]

if len(sys.argv) < 2:
    sys.argv = ['pyart.py',random.randrange(1, len(chars)+1)]

while int(sys.argv[1])>len(chars):
    sys.argv[1] = int(input("Entrez un chiffre entre 1 et " + str(len(chars)) + "\n"))

chars_choice = int(sys.argv[1])-1

for i in range(25):
    row = ""
    for j in range(50):
        row += chars[chars_choice][random.randrange(0,len(chars[chars_choice]))]
    print(row)
