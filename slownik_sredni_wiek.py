uzytkownicy = {}
uzytkownicy['Kasia'] = {'email' : 'kasia@przyklad.com', 'płeć' : 'k', 'wiek' : 27, 'przyjaciele' : ['Jan', 'Jacek']}
uzytkownicy['Jan'] = {'email' : 'jan@abc.com', 'płeć' : 'm', 'wiek' : 24, 'przyjaciele' : ['Kasia', 'Jacek']}
uzytkownicy['Jacek'] = {'email' : 'jacek@xyz.com', 'płeć' : 'm', 'wiek' : 32, 'przyjaciele' : ['Kasia']}


def srednia_wieku(nazwa_uzytkownika):
    uzytkownik = uzytkownicy[nazwa_uzytkownika]
    przyjaciele = uzytkownik['przyjaciele']

    suma = 0

    for imie in przyjaciele:
        przyjaciel = uzytkownicy[imie]
        suma = suma + przyjaciel['wiek']

    srednia = suma/len(przyjaciele)
    print('Srednia wieku przyjaciół użytkownika', nazwa_uzytkownika, 'to', srednia) 

srednia_wieku('Kasia')
srednia_wieku('Jan')
srednia_wieku('Jacek')


max = 1000
for imie in uzytkownicy:
    uzytkownik = uzytkownicy[imie]
    przyjaciele = uzytkownik['przyjaciele']
    if len(przyjaciele) < max:
        najbardziej_aspoleczny = imie
        max = len(przyjaciele)
print('Najbardziej aspolecznym uzytkownikiem jest ', najbardziej_aspoleczny)
