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

# colors = ["light pink","pale goldenrod","green yellow","firebrick","dark sea green","pale turquoise","light steel blue","gold","medium purple","dark green","navy","medium orchid","maroon"]
direction = [0,90,180,270]
tim.speed("fastest")
for i in range(200):
    tim.pensize(15)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))