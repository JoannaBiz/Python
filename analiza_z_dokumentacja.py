
"""Moduł analyze analizuje tekst na podstawie wzoru na obliczanie indeksu
    czytelności Flescha i zwraca odpowiedni wynik. Wynik zostaje następnie
    przekonwertowany na kategorię czytelności, wskazującą wykształcenie odpowiadające
    poziomowi trudności tekstu.

"""
def policz_sylaby(slowa):
    """ Ta funkcja pobiera listę słów i zwraca łączną liczbę sylab
        wszystkich słów z listy.
    """
    liczba = 0
    for slowo in slowa:
        liczba_sylab = policz_sylaby_w_slowie(slowo)
        liczba = liczba + liczba_sylab
    return liczba

def policz_sylaby_w_slowie(slowo):
    """Ta funkcja pobiera słowo w formie łańcucha
        i zwraca liczbę sylab. Zauważ, że jest to heurystyka i
        może nie zwracać stuprocentowo dokładnego wyniku.
    """
    liczba = 0

    koncowki = '.,;!?:'
    ostatni_znak = slowo[-1]
    
    if ostatni_znak in koncowki:
        przetworzone_slowo = slowo[0:-1]
    else:
        przetworzone_slowo = slowo
        
    if len(przetworzone_slowo) <= 3:
        return 1

    if przetworzone_slowo[-1] in 'eE':
        przetworzone_slowo= przetworzone_slowo[0:-1]

    samogloski = "aeiouAEIOU"
    poprzedni_znak_byl_samogloska = False
    
    for znak in przetworzone_slowo:
        if znak in samogloski:
            if not poprzedni_znak_byl_samogloska:
                liczba = liczba + 1
            poprzedni_znak_byl_samogloska = True
        else:
            poprzedni_znak_byl_samogloska = False
            
    if przetworzone_slowo[-1] in 'yY':
        liczba = liczba + 1
                          
    return liczba

def policz_zdania(tekst):
    """Ta funkcja liczy zdania w łańcuchu tekstowym,
        używając kropek, średników, znaków zapytania i
        wykrzykników jako znaków końcowych.
    """
    liczba = 0
    koncowe = '.?!'     
    for znak in tekst:
        if znak in koncowe:
            liczba = liczba + 1
    return liczba

def zwroc_wynik(wynik):
       """Ta funckja pobiera wyniki czytelności Flescha i wyświetla odpowiadający
       poziom trudności.
       """
       if wynik >= 90.0:
            print('5 klasa podstawówki')
       elif wynik >= 80.0:
            print('6 klasa podstawówki')
       elif wynik >= 70.0:
            print('7 klasa podstawówki')
       elif wynik >= 60.0:
            print('8 klasa podstawówki, 1 klasa liceum')
       elif wynik >= 50.0:
            print('2-4 klasa liceum')
       elif wynik >= 30.0:
            print('Studia licencjackie')
       else:
            print('Studia magisterskie')



def oblicz_czytelnosc(tekst):
    liczba_slow = 0
    liczba_zdan = 0
    liczba_sylab = 0
    wynik = 0
    
    slowa = tekst.split()
    liczba_slow = len(slowa)
    liczba_zdan = policz_zdania(tekst)
    liczba_sylab = policz_sylaby(slowa)
    wynik = (206.835 - 1.015 * (liczba_slow / liczba_zdan) - 84.6 * (liczba_sylab /liczba_slow))

    
        
    print(liczba_slow, 'słów')
    print(liczba_zdan, 'zdań')
    print(liczba_sylab, 'sylab')
    print(wynik, 'indeks czytelności')
    zwroc_wynik(wynik)

if __name__ =="__main__":
    import ch1text
    print('Tekst rozdziału 1.:')
    oblicz_czytelnosc(ch1text.tekst)
