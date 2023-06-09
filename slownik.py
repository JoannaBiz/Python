moj_slownik = {}

moj_slownik['joanna'] = '867-5309'
moj_slownik['wiek'] = 27
moj_slownik['42'] = 'odpowiedz'
moj_slownik['wyniki'] = [92,87,99]
moj_slownik['piotr'] = '555-1201'
moj_slownik['dawid'] = '321-6617'
moj_slownik['jerzy'] = '771-0091'
moj_slownik['piotr'] = '443-0000'

numer_telefonu = moj_slownik['joanna']
print("Numer telefonu Joanny:", numer_telefonu)
print('---------------------------------------------------')

if 'joanna' in moj_slownik:
    print('Znalazła się: ', moj_slownik['joanna'])
    print('---------------------------------------------------')
else:
    print('Nie ma jej numeru')
    print('---------------------------------------------------')

for klucz in moj_slownik:
    print(klucz, ':' ,moj_slownik[klucz])
    print('---------------------------------------------------')
    
uzytkownicy = {'Kasia' : 'kasia@przyklad.com',
               'Jan' : 'jan@abc.com',
               'Jacek' : 'jacek@xyz.com'}

wlasciwosc = {'email' : 'kasia@przyklad.com',
              'plec' : 'k',
              'wiek' : 27,
              'przyjaciele' : ['Jan', 'Jacek']}
print(uzytkownicy)
print('---------------------------------------------------')
print(wlasciwosc)
print('---------------------------------------------------')
uzytkownicy ={}
uzytkownicy['Kasia'] = wlasciwosc
uzytkownicy['Jan'] = {'email' : 'jan@abc.com', 'plec' : 'm', 'wiek' : 24, 'przyjaciele' : ['Kasia','Jacek']}
uzytkownicy['Jacek'] = {'email' : 'jacek@xyz.com', 'plec' : 'm' , 'wiek' : 32, 'przyjaciele' : ['Kasia']}
print(uzytkownicy)
print('---------------------------------------------------')
