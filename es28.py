def find_an_even(L):
    """Assume che L sia una lista di interi
    Restituisce il primo numero pari in L
    Solleva ValueError se L non contiene numeri pari.
    """

    try:
        for i in L:
            if i%2 == 0:
                return i
        raise ValueError()
    except ValueError:
        print("Non ci sono numeri pari nella lista.")


lista=[1,3,5,7,9,11,13,15]
res = find_an_even(lista)
print(res)
