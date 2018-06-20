#! /usr/bin/python3
# -*- coding: utf-8 -*-

import random
import sys

chars1 = ["|","-","_","=","/","\\","#"," "]
chars2 = ["(",")","{","}","[","]"]
chars3 = ["|","_"," "]
chars6 = ["ᚐ","ᚑ","ᚒ","ᚓ","ᚔ"]
chars7 = ["ᚋ","ᚌ","ᚍ","ᚎ","ᚏ"]
chars8 = ["▖","▗","▘","▙","▚","▛","▜","▝","▞","▟"]

if len(sys.argv) < 2:
    sys.argv = ['pyart.py',random.randrange(0, 9)]

sys.argv[1] = int(sys.argv[1])

if sys.argv[1] == 1:
    chars = chars1
elif sys.argv[1] == 2:
    chars = chars2
elif sys.argv[1] == 4:
    chars = chars4
elif sys.argv[1] == 5:
    chars = chars5
elif sys.argv[1] == 6:
    chars = chars6
elif sys.argv[1] == 7:
    chars = chars7
elif sys.argv[1] == 8:
    chars = chars8
else:
    chars = chars3

for i in range(25):
    row = ""
    for j in range(50):
        row += chars[random.randrange(0,len(chars))]
    print(row)
