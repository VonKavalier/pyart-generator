#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys

chars1 = ["#","|","-","_","=","/","\\"," "]
chars2 = ["(",")","{","}","[","]"]
chars3 = ["|","_"," "]
chars6 = ["ᚐ","ᚑ","ᚒ","ᚓ","ᚔ"]
chars8 = ["▖","▗","▘","▙","▚","▛","▜","▝","▞","▟"]
chars9 = ["⋮","⋰","⋱"]

if len(sys.argv) < 2:
    sys.argv = ['pyart.py',random.randrange(0, 7)]

sys.argv[1] = int(sys.argv[1])

if sys.argv[1] == 1:
    chars = chars1
elif sys.argv[1] == 2:
    chars = chars2
elif sys.argv[1] == 6:
    chars = chars6
elif sys.argv[1] == 8:
    chars = chars8
elif sys.argv[1] == 9:
    chars = chars9
else:
    chars = chars3

for i in range(25):
    row = ""
    for j in range(50):
        row += chars[random.randrange(0,len(chars))]
    print(row)
