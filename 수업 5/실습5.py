import turtle
t = turtle.Turtle()
t.shape("turtle")

shape = str(turtle.textinput("","도형을 입력하시오."))

if shape == '사각형':
    width = int(turtle.textinput("","가로"))
    height = int(turtle.textinput("","세로"))
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
elif shape == '삼각형':
    length = int(turtle.textinput("","한 변의 길이"))
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
else:
    radius = int(turtle.textinput("","반지름"))
    t.circle(radius)
