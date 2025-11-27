import turtle
import sys

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")

def draw_shape(color, radius, side_number, x, y):
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.circle(radius,None,side_number)
    t.end_fill()

try:
    color = input("What color is your shape? ")
    t.fillcolor(color)
except:
    print("That's not a valid color.")
    sys.exit()

try:
    radius = int(input("How big is your shape? "))
    side_number = int(input("How many sides does your shape have? "))
except:
    print("That's not a valid number.")
    sys.exit()

if side_number == 0:
    side_number = None

if side_number in [1, 2]:
    radius = 25
    draw_shape(color, radius, 3, -50, -50)
    draw_shape(color, radius, 4, -50, 50)
    draw_shape(color, radius, 5, 50, -50)
    draw_shape(color, radius, 6, 50, 50)
else:
    t.penup()
    t.goto(0, -radius)
    t.begin_fill()
    t.circle(radius,None,side_number)
    t.end_fill()

t.hideturtle()
turtle.done()