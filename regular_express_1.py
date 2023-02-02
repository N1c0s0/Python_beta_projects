##LICENSE.txt
import re

name = input("Enter File: ")
hand = open(name)
adress = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^From 23([^]*))', line)
    if len(stuff) != 1:
        continue
    adress.append(stuff)
print(adress)    
