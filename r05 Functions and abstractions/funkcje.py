def szczekanie(imie,waga):
    if waga >10:
        print(imie,'robi HAU, HAU,HAU')
    else:
        print(imie,'robi hau, hau, hau')

szczekanie("Kodi",18)
szczekanie("Azor",4)
szczekanie("Fafik",6)
szczekanie("Reksio",30)

def jak_tam_dotrzec(kilometry):
    if kilometry >200.0:
        print ('Samolotem')
    elif kilometry >= 3.0:
        print ('Samochodem')
    else:
        print('Pierszo')
jak_tam_dotrzec(800.3)
jak_tam_dotrzec(3.0)
jak_tam_dotrzec(.5)

def pobierz_szczekanie(waga):
    if waga >20:
        return 'HAU HAU'
    else:
        return 'hau hau'
kodi_szczekanie = pobierz_szczekanie(40)
print ("Kodi szczeka", kodi_szczekanie)

def pobierz_ceche(zapytanie, domyslna):
   pytanie = zapytanie + ' [' + domyslna + ']? '
   odpowiedz = input(pytanie)
   if (odpowiedz == ''):
      odpowiedz = domyslna
   print('Wybrałeś/aś:', odpowiedz)
   return odpowiedz

wlosy = pobierz_ceche('Jaki kolor włosów', 'brązowy')
wlosy_dlugosc = pobierz_ceche ('Jaka długość włosów', 'krótkie')
oczy = pobierz_ceche ('Jaki kolor oczu', 'niebieski')
plec = pobierz_ceche ('Jaka płeć', 'kobieta')
okulary = pobierz_ceche ('Okulary', 'nie')
broda = pobierz_ceche ('Broda', 'nie')


    
            
            
        
