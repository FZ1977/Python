# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:53:42 2023

@author: Fabio Zangari
Srivere una funzione che ordina una lista numerica.
"""

def BubbleSort(a):
    n = len(a) # lunghezza della lista
    i = 0 # indice
    
    while n>=2:
        for i in range(len(a[:n-1])):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            
        n -= 1

a=[5,3,8,10,32,4,18,0,1]
print('Lista prima di essere ordinata -> ', a)
BubbleSort(a)
print('Lista dopo essere ordinata -> ', a)