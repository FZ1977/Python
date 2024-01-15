# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:58:26 2023

@author: Fabio Zangari
"""

def funzione(s, k):
    a = []
    s = "".join(s.split(" "))

    for i in range(len(s)-2):
        a.append(s[i:i+k])
        
    #a = sorted(a) #questo metodo non modifica la lista
    a.sort() #questa funzione modifica la lista
    return a

s = "corso di programmazione python e c"
k = 3
print(funzione(s,k))