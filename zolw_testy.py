import turtle

powolniak = turtle.Turtle()
powolniak.shape('turtle')
powolniak.color('blue')
powolniak.penup()
powolniak.setposition(-120,0)
powolniak.pendown()
powolniak.circle(50)


powolniak.pencolor('red')
powolniak.penup()
powolniak.setposition(120,0)
powolniak.pendown()
powolniak.circle(50)

def narysuj_kwadrat(zolw):
    for i in range(5):
        powolniak.forward(100)
        powolniak.right(144)



narysuj_kwadrat(powolniak)

turtle.mainloop()
