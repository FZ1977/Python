# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=[1,2,3,1.1,2.2,3.3,"uno","due","tre"]

def f(a):
    x=[]
    y=[]
    z=[]
    for i in a:
        if type(i) == type(0):
            x.append(i)
        
        if type(i) == type(1.1):
            y.append(i)
            
        if type(i) == type("ciao"):
            z.append(i)
            
    for j in range(len(x)):
        print(x[j], " - ",y[j]," - ",z[j])
        
f(a)