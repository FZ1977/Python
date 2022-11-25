import calendar

def calcola_giorno(year, month):
    calendario = calendar.TextCalendar()
    mese = calendario.monthdayscalendar(year, month)

    if mese[0][3] != 0:
        giorno_ringraziamento = mese[3][3]
    else:
        giorno_ringraziamento = mese[4][3]

    return giorno_ringraziamento

def shopping_days(year):
    """anno e' un numero >=1941
    restituisce il numero di giorni compresi
    fra il giorno del ringraziamento e natale
    di quell'anno.
    """
    appo = 30 - calcola_giorno(year, 11)
    numero_giorni_a_natale = appo + 25

    return numero_giorni_a_natale

#year=1941
for year in range(1941, 2023):
    print("Nell'anno",year,"il numero di giorni a Natale dal giorno del ringraziamento e' di", shopping_days(year),"giorni.")
