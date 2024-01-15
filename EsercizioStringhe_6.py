# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 18:05:14 2023

@author: Fabio Zangari
"""

file = open("C:\\Users\\LENOVO\\Desktop\\Git\\Python\\testo.txt","r")

conta = 0
c = "a"
lista = []

for line in file:
    line = line.lower()
    a = []
    a = line.split(" ")
    a.pop()
    for s in a:
        if c.lower() not in s:
            conta += 1
            lista.append(s)
            
print("sono state rimosse", conta, " parole")
        