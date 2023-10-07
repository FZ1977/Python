# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:14:07 2023

@author: Fabio Zangari
"""

def stampa_tabella(tabella):
    print(f"{'nome':<15}|{'cognome':<20}|{'eta':^5}")
    print(f"{'---------------|--------------------|--------':^0}")
    for t in tabella:
        print(f"{t['nome']:<15}|{t['cognome']:<20}|{t['eta']:^5}")

def modifica_tabella(tabella,colonna,valore):
    i=0
    while i<len(tabella):
        if tabella[i][colonna]!=valore:
            tabella.pop(i)
        else:
            i=i+1       
        
    return tabella

def rimuovi_colonna(tabella,colonna):
    for t in tabella:
        t.pop(colonna)
    
    return tabella        

tabella=[{'nome':'fabio', 'cognome':'zangari', 'eta':46},
         {'nome':'elisa', 'cognome':'zangari', 'eta':10},
         {'nome':'paola', 'cognome':'brusco', 'eta':45},
         {'nome':'antonio', 'cognome':'rossi', 'eta':64},
         {'nome':'maria', 'cognome':'proietti', 'eta':30}]


print("prima della modifica")
stampa_tabella(tabella)
print("dopo la modifica")
t_mod=modifica_tabella(tabella,'nome','fabio')
stampa_tabella(t_mod)
print('stampo senza la colonna')
print(rimuovi_colonna(t_mod,'nome'))
