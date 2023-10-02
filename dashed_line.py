import turtle

tur = turtle.Turtle()
tur.pencolor('green')
dash_length = 10 #length of each dash
gap_length = 5 #gap between each dash

for i in range(10):
    tur.forward(dash_length)#draw a dash
    tur.penup()
    tur.forward(gap_length)
    tur.pendown()


screen = turtle.Screen()
screen.exitonclick()

