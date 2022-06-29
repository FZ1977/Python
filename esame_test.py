# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:06:30 2022

@author: fabio
"""

def sort_by_occurrences(a):
    d = {}
    s = []
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 0
            
    for c,v in d.items():
        s.append(c)
        
    return ''.join(s)


a = ')-:))-'  
x = sort_by_occurrences(a)
print(type(x))  