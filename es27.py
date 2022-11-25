def sum_digits(s):
    """Assume che s sia una stringa
    Restituisce la somma delle cifre decimali in s
    Per esempio, se s e' 'a2b3c', restituisce 5
    """
    somma = 0

    for i in s:
        try:
            if ord(str(i)) <= 57 and ord(str(i)) >= 48:
                somma = somma + int(i)
        except(TypeError):
            print("Ignoro il carattere '"+i+"' non e' un numero.")

    return somma

print(sum_digits('a2b3c'))
