import turtle
import random
tim = turtle.Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(round(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(120)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(10)
screen = turtle.Screen()
screen.exitonclick()