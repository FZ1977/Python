# -*- coding: utf-8 -*-
"""
Spyder Editor
Prende in input un insieme di parole, torna la lista ordinata di 
tutte le parole che è possibile creare fondendo le parole 
nell'insieme di partenza.
"""

from itertools import permutations

a = input("Inserisci le parole: ")
l = a.split(" ")
n = len(l)
p = permutations(l)
for i in p:
    print(" ".join(i))
