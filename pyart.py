#! /usr/bin/python3

import random
import sys

assets1 = ["|","-","_","=","/","\\","#"," "]
assets2 = ["(",")","{","}","[","]"]
assets3 = ["|","_"," "]

if len(sys.argv) > 1:
    if sys.argv[1] == "1":
        assets = assets1
    elif sys.argv[1] == "2":
        assets = assets2
else:
    assets = assets3

for i in range(25):
    row = ""
    for j in range(50):
        row += assets[random.randrange(0,len(assets))]
    print(row)
