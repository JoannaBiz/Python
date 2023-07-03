kulki = [10,13,39,14,41,9,3]
print('Kulek jest łącznie: ', sum(kulki))


def licz_kulki(lista):
    suma_kulek = 0 
    for liczba in lista:
        suma_kulek = suma_kulek + liczba
    return suma_kulek
print('Kulek jest łącznie: ', licz_kulki(kulki))

def oblicz_suma_rekurencyjnie(lista):
    if len(lista) == 0:
        return 0
    else:
        pierwszy = lista[0]
        reszta = lista[1:]
        suma = pierwszy + oblicz_suma_rekurencyjnie(reszta)
        return suma

suma = oblicz_suma_rekurencyjnie(kulki)
print('Kulek jest łącznie: ',suma)

