import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Budget Pac-Man")
wn.addshape("Left.gif")
wn.addshape("Right.gif")
wn.addshape("Up.gif")
wn.addshape("Down.gif")

pellets = []

def walls():
    w = turtle.Turtle()
    w.speed(8)
    # outer walls
    w.pencolor("blue")
    w.penup()
    w.pensize(5)
    w.goto(-500,-500)
    w.pendown()
    w.goto(-500,500)
    w.goto(500,500)
    w.goto(500,-500)
    w.goto(-500,-500)   
    #southwest walls
    w.penup()
    w.goto(-300,-500)
    w.pendown()
    w.goto(-300,-100)
    w.goto(-100,-100)
    w.goto(-100,-300)
    #northwest walls
    w.penup()
    w.goto(300,500)
    w.pendown()
    w.goto(300,100)
    w.goto(100,100)
    w.goto(100,300)
    #northwest walls
    w.penup()
    w.goto(-500,300)
    w.pendown()
    w.goto(-300,300)
    w.goto(-300,100)
    w.goto(-100,100)
    w.goto(-100,300)
    # south east walls
    w.penup()
    w.goto(500,-300)
    w.pendown()
    w.goto(300,-300)
    w.goto(300,-100)
    w.goto(100,-100)
    w.goto(100,-300)
    w.hideturtle()

def create_pellets():
    for _ in range(25):
        pellet = turtle.Turtle()
        pellets.append(pellet)
        pellet.penup()
        pellet.speed(8)
        pellet.shape("circle")

    for pellet in pellets:
        pellet.fillcolor("yellow")
        pellet.pencolor ("yellow")
        pellet.turtlesize(1)
        pellet.goto(-400,-400)

    start_x = -400
    start_y = -400
    spacing = 200
    for i, pellet in enumerate(pellets):
        x = start_x + (i % 5) * spacing
        y = start_y + (i // 5) * spacing
        pellet.goto(x, y)

walls()
create_pellets()
  
PM = turtle.Turtle()
PM.penup()
PM.goto(-400,-400)
PM.shape("Up.gif")
PM.setheading(90)

step = 200
instructions = [
    "pass", "up", "up", "up", "down", "right", "right", "right", "right",
    "up", "up", "down", "down", "down", "up", "left", "left", "up", "up",
    "left", "left", "right", "down", "up", "right", "right", "down", "up",
    "left", "down", "down", "down", "down", "left", "up", "down", "right",
    "right", "up", "down", "right"
]

for i in instructions:
    if i == "up":
        PM.setheading(90)
        PM.shape("Up.gif")
        PM.forward(step)
    if i == "down":
        PM.setheading(270)
        PM.shape("Down.gif")
        PM.forward(step)
    if i == "left":
        PM.setheading(180)
        PM.shape("Left.gif")
        PM.forward(step)
    if i == "right":
        PM.setheading(0)
        PM.shape("Right.gif")
        PM.forward(step)
    for pellet in pellets:
        if abs((pellet.xcor() - PM.xcor())) < 20:
            if abs((pellet.ycor() - PM.ycor())) < 20:
                pellet.hideturtle()
                pellets.remove(pellet)

wn.mainloop()