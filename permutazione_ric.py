# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:16:28 2023

@author: Fabio Zangari
"""

def  permutazione(s,i):
    if s==[1,3,2]:
        return s
    if len(s)==0:
        return s
    else:
        print(s)
        temp=s[i]
        s[i]=s[i+1]
        s[i+1]=temp
        if i<1:
            permutazione(s,i+1)
        else:
            i=0
            permutazione(s,i)

s=[1,2,3]
print(permutazione(s,0))