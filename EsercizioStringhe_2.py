# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:26:39 2023

@author: Fabio Zangari
"""

def funzione1(a, k):
    if len(a) == k:
        print(a,end="")
            

f = open("C:\\Users\\LENOVO\\Desktop\\Git\\Python\\testo.txt", "r")


for l in f:
    funzione1(l, 7)
    
print("###########")
f.seek(0)

lista = []    
for l in f:
    lista.append(list(l))

for i in range(len(lista)):
    lista[i].pop()

m = 0
for l in lista:
    if len(l) > m:
        m = len(l)
        
for l in lista:
    print(l)
print("#############")
for pos in range(m):
    d = {}
    for l in lista:
        if  pos < len(l):
            if l[pos] in d:
                d[l[pos]] += 1
            else:
                d[l[pos]] = 1
    
    #print(d)
    m_val = 0
    chiave = 0
    for k,v in d.items():
        if v > m_val:
            m_val = v
            chiave = k
            
    print("pos:" , pos, "lettera:", chiave)

f.close