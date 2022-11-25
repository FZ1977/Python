"""Scrivere un programma che conservi in un file i primi dieci numeri
di Fibonacci in un file con il nome fib_file. Ogni numero deve essere
su una riga distinta nel file. Il programma poi deve leggere i numeri
dal file e stamparli.
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

mio_file=open('fib_file','w')

for i in range(10):
    mio_file.write(str(fibonacci(i))+'\n')

mio_file.close()

mio_file=open('fib_file','r')

righe = mio_file.readlines()
for i in range(len(righe)):
    print(righe[i],end="")

mio_file.close()

