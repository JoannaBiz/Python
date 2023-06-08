import turtle

powolniak = turtle.Turtle()
powolniak.shape('turtle')
powolniak.color('blue')
maruda = turtle.Turtle()
maruda.shape('turtle')
maruda.color('red')

def narysuj_kwadrat(zolw):
    for i in range(0,4):
        zolw.forward(100)
        zolw.right(90)

def narysuj_spirale(zolw):
    for i in range(0,36):
        narysuj_kwadrat(zolw)
        zolw.right(10)
        
#narysuj_kwadrat(powolniak)
#maruda.right(45)
#narysuj_kwadrat(maruda)
narysuj_spirale(powolniak)
maruda.right(5)
narysuj_kwadrat(maruda)

turtle.mainloop()
