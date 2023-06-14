#moj_plik = open('lib.txt','r')
#moj_tekst = moj_plik.read()
#print(moj_tekst)
#moj_plik.close()

import sys
def utworz_szalona_historie(nazwa_pliku):
    try:
        
        plik = open(nazwa_pliku,'r')

        tekst = ''
        for wiersz in plik:
            tekst = tekst + przetworz_wiersz(wiersz)
        plik.close()

        return tekst
    except FileNotFoundError:
        print("Nie znaleziono pliku", nazwa_pliku + '.')
    except IsADirectoryError:
        print(nazwa_pliku, 'jest katalogiem')
    except:
        print("Nie można odczytać", nazwa_pliku)

znaczniki = ['MIANOWNIK','DOPEŁNIACZ','BIERNIK','NARZĘDNIK','MIEJSCOWNIK']
def przetworz_wiersz(wiersz):
    global znaczniki
    przetworzony_wiersz = ''

    slowa = wiersz.split()
    for slowo in slowa:
        oczyszczone = slowo.strip('.,;?!')
        if oczyszczone in znaczniki:
            odpowiedz = input('Podaj ' + oczyszczone + ':')
            przetworzony_wiersz = przetworzony_wiersz + odpowiedz
            if slowo[-1] in ('.,;?!'):
                przetworzony_wiersz = przetworzony_wiersz + slowo[-1] + ' '
                
        else:
            przetworzony_wiersz = przetworzony_wiersz + slowo + ' '
    return  przetworzony_wiersz + '\n'

def zapisz_szalona_historie(nazwa_pliku, tekst):
    try:
        plik = open(nazwa_pliku,'w')
        plik.write(tekst)
        plik.close
    except:
        print("Nie dało się zapisać pliku", nazwa_pliku)

def main():
    if len(sys.argv) != 2:
        print("crazy.py <nazwa_pliku>")
    else:
        nazwa_pliku = sys.argv[1]
        historia = utworz_szalona_historie(nazwa_pliku)
        if (historia != None):
            zapisz_szalona_historie('crazy_' +nazwa_pliku, historia)
    print(historia)

if __name__ == '__main__':
    main()
