#! /usr/bin/python3

import random
import sys

chars1 = ["|","-","_","=","/","\\","#"," "]
chars2 = ["(",")","{","}","[","]"]
chars3 = ["|","_"," "]

if len(sys.argv) < 2:
    sys.argv = ['pyart.py',random.randrange(0, 4)]

chars = chars1

print(sys.argv)

if sys.argv[1] == 1:
    chars = chars1
elif sys.argv[1] == 2:
    chars = chars2
elif sys.argv[1] == 3:
    chars = chars3

for i in range(25):
    row = ""
    for j in range(50):
        row += chars[random.randrange(0,len(chars))]
    print(row)
