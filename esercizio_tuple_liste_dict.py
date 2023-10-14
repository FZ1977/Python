def f(n,c):
    lista=[]
    for i in range(len(n)):
        d={}
        d['cognome']=c[i]
        d['nome']=n[i]
        lista.append(d)

    return lista

nomi=('Numa','Tullo','Anco')
cognomi=('Pompilio','Ostilio','Marzio')

print(f(nomi,cognomi))
