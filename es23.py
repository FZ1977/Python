def get_min(d):
    """d è un dict che mappa lettere su int
    restituisce il valore in d associato alla prima chiave
    in ordine alfabetico. Per esempio,
    se d = {x: 11, b: 12}, get_min restituisce 12.
    """
    lista_chiavi=list(d.keys())
    chiave = lista_chiavi[0]
    for i in range(1,len(lista_chiavi)):
        if chiave>lista_chiavi[i]:
            chiave=lista_chiavi[i]

    return d[chiave]

d={'x': 11, 'b': 12, '1': 3, 'G': 78}
print(get_min(d))
