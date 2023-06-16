import requests, json,turtle

def rusz_iss(dlugosc,szerokosc):
    global iss
    iss.penup()
    iss.goto(szerokosc,dlugosc)
    iss.pendown()

ekran = turtle.Screen()
ekran.setup(1000,500)
ekran.bgpic('earth.gif')
ekran.setworldcoordinates(-180,-90,190,90)

iss = turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

url = 'http://api.open-notify.org/iss-now.json'
odpowiedz = requests.get(url)


if odpowiedz.status_code == 200:
    odpowiedz_slownik = json.loads(odpowiedz.text)
    polozenie = odpowiedz_slownik['iss_position']
    print('Współrzędne ISS to ' + polozenie['latitude']+','+ polozenie['longitude'])
    dlugosc = float(polozenie['latitude'])
    szerokosc = float(polozenie['longitude'])
    rusz_iss(dlugosc,szerokosc)
else:
    print('Huston mamy problem',odpowiedz.status_code)



turtle.mainloop()
