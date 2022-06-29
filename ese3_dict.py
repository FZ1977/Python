# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:46:57 2022

@author: fabio
"""

def crea_tabella_ascii(a):
    d = {}
    for x in a:
        d[x] = chr(x)
        
    return d
    
a = []
for i in range(128):
    a.append(i)
    
d = crea_tabella_ascii(a)
for c,v in d.items():
    print(c,'-',v, end='\t')