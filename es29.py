# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:15:40 2023

@author: Fabio Zangari
"""

import random

def crea_lista_numeri():
    lista=[]
    for i in range(0,20):
        lista.append(random.randrange(0,99,1))

    return lista

def stampa_numeri_pari(lista):
    for i in lista:
        if i%2 == 0:
            print(i,end=" ")
    print()

def stampa_numeri_maggiori_di_70(lista):
    for i in lista:
        if i>70:
            print(i,end=" ")
    print()

def varianza(lista):
    media=0
    somma=0
    n=len(lista)
    for i in lista:
        somma=somma+i
        
    media=somma/n
    
    varianza=0
    somma=0
    for x in lista:
        somma=somma+(x-media)**2
        
    varianza=somma/n
    return varianza

l = crea_lista_numeri()
print(l)
stampa_numeri_pari(l)
stampa_numeri_maggiori_di_70(l)
print("varianza",varianza(l))