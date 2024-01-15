# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:48:40 2023

@author: Fabio Zangari
"""

def funzione(s, k):
    s = "".join(s.split(" "))

    for i in range(len(s)-2):
        print(s[i:i+k])

s = "corso di programmazione python e c"
k = 3
funzione(s,k)