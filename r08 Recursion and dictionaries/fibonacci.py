import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(20,30,5):
    poczatek = time.time()
    wynik = fibonacci(i)
    koniec = time.time()
    czas = koniec - poczatek
    print(i, wynik, czas)
    
