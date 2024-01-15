# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:11:26 2023

@author: Fabio Zangari
"""

file = open("C:\\Users\\LENOVO\\Desktop\\Git\\Python\\testo.txt","r")
d = {}

for line in file:
    a = []
    a = line.split(" ")
    a.pop()
    
    chiave = ""
    for s in a:
        for c in s:
            if (c.lower() != "a" and c.lower() != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u" and c != "," and c != ";" and c != "."):
                chiave += c
            d[chiave] = a
            

print(d)
