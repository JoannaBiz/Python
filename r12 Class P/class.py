class Pies:
    def __init__(self,imie,wiek,waga):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga

def szczekanie(self):
    if self.waga >10:
        print(self.imie, ' robi HAU HAU')
    else:
        print(self.imie, ' robi hau hau')
        
def ludzkie_lata(self):
    wiek_w_ludzkich_latach = self.wiek * 7
    return wiek_w_ludzkich_latach

def __str__(self):
    return "Jestem psem o imieniu" + self.imie

class PiesTowarzyszacy(Pies):
    def __int__(self,imie, wiek, waga,opiekun):
        Pies.__init(self,imie,wiek,waga)
        self.opiekun = opiekun
        self.pelni_sluzbe = False
    def chodzenie(self):
        print(self.imie, ' i jego opiekun', self.opiekun, 'wychodzą na spacer')
    def szczekanie(self):
        if self.pelni_sluzbe:
            print(self.imie, ' mówi: Nie mogę szczekać, bo jestem na służbie')
        else:
            Pies.szczekanie(self)

kodi = Pies('Kodi',12,8)
fafik = Pies('Fafik',9,6)
print(kodi.imie,'miałby jako człowiek',ludzkie_lata(kodi),'lat')
print(fafik.imie,'miałby jako człowiek', ludzkie_lata(fafik),'lat')


