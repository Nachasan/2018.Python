import turtle
t=turtle.Turtle()
t.shape('turtle')

for i in range(3):
    t.forward(100)
    t.left(360/3)

t.penup()
t.forward(200)
t.pendown()

for j in range(4):
    t.forward(100)
    t.left(360/4)
