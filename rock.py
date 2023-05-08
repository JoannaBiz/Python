import random
zwyciezca = ''
liczba_losowa = random.randint(0,2)

if liczba_losowa == 0:
    wybor_komputera = 'kamień'
if liczba_losowa == 1:
    wybor_komputera = 'papier'
else:
    wybor_komputera = 'nożyce'

wybor_uzytkownika = ''
while (wybor_uzytkownika != 'kamień' and wybor_uzytkownika != 'papier' and wybor_uzytkownika !='nożyce'):
    wybor_uzytkownika = input ('kamień papier czy nożyce? ')
    
if wybor_komputera == wybor_uzytkownika:
    zwyciezca = 'remis'
elif wybor_komputera == 'papier' and wybor_uzytkownika == 'kamień':
    zwyciezca = 'komputer'
elif wybor_komputera == 'kamień' and wybor_uzytkownika == 'nożyce':
    zwyciezca = 'komputer'
elif wybor_komputera == 'nożyce' and wybor_uzytkownika == 'papier':
    zwyciezca = 'komputer'
else:
    zwyciezca = 'uzytkownik'

if zwyciezca == 'remis':
    print('Remis',wybor_komputera + ' ,zagraj ponownie.')
else:
    print('Wygrał', zwyciezca + ',', 'Komputer wybrał', wybor_komputera + '.')
