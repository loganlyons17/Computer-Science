import turtle

screen = turtle.Screen()
screen.bgcolor("cornflower blue")

t = turtle.Turtle()
t.speed(6)
t.turtlesize(0.1, 0.1, 0.1)

#house base
t.pensize(2)
t.penup()
t.goto(-100, -100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

#roof
t.penup()
t.goto(-100, 100)
t.pendown()
t.pensize(3)
t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(141)
t.right(90)
t.forward(141)
t.right(135)
t.forward(200)
t.end_fill()

#door
t.pensize(1)
t.penup()
t.goto(-25, -100)
t.setheading(90)
t.pendown()
t.fillcolor("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

#window
t.penup()
t.goto(0, 20)
t.setheading(0)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
t.circle(30)
t.end_fill()

# window cross
t.setheading(90)
t.forward(60)
t.right(180)
t.forward(30)
t.right(90)
t.forward(30)
t.right(180)
t.forward(60)
t.penup()

# doorknob
t.goto(19, -55)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

#grass
t.goto(-500, -100)
t.setheading(0)
t.pensize(1)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.forward(1000)
t.right(90)
t.forward(300)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(300)
t.end_fill()
t.penup()

#path
t.goto(-25, -100)
t.setheading(270)
t.right(10)
t.pendown()
t.fillcolor("peru")
t.begin_fill()
t.forward(350)
t.setheading(0)
t.forward(150)

t.penup()
t.goto(-25, -100)
t.setheading(0)
t.pendown()
t.forward(50)
t.setheading(270)
t.left(10)
t.forward(350)
t.setheading(180)
t.forward(22)
t.end_fill()
t.penup()

# sun
t.goto(300, 250)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()


turtle.done()