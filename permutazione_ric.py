def permutazione(stringa):
    if len(stringa) < 1:
        return stringa
    elif len(stringa) == 2:
        return [stringa, stringa[1]+stringa[0]]
    lista_permutazioni=[]
    for i in range(len(stringa)):
        carattere_fisso=stringa[i]
        stringa_parziale = stringa[0:i]+stringa[i+1:]
        if len(stringa_parziale) > 2:
            intermedia=permutazione(stringa_parziale)
            for index in range(len(intermedia)):
                intermedia[index]=carattere_fisso+intermedia[index]
            lista_permutazioni += [intermedia]
        else:
            lista_permutazioni += [carattere_fisso + stringa_parziale]
            lista_permutazioni += [carattere_fisso + stringa_parziale[1] + stringa_parziale[0]]
    return lista_permutazioni        
            

stringa="12345"

print(permutazione(stringa))
