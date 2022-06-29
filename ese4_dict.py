# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:27:52 2022

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
            
    for v in sorted(d.values(),reverse=False):
        for c in d.keys():
            if d[c]==v:
                s.append(c)
        
    return ''.join(s)


a = ')-:))-'  
x = sort_by_occurrences(a)
print(x)  