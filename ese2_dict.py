# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:32:20 2022

@author: fabio
"""

def crea_dizionario(a):
    d = {}
    for i in range(len(a)):
        d[i] = a[i]
        
    return d

a = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']
diz = crea_dizionario(a)
for c,v in diz.items():
    print('Chiave:',c,' Valore:',v)

print()
print('Stampo solo i valori pari del dizionario')
for c,v in diz.items():
    if(c%2==0):
        print('Chiave:',c,' Valore:',v)