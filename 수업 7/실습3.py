##터틀그래픽에서 클릭하는 위치부터 시작해 네모를 그리도록 하는 프로그램

#터틀그래픽을 실행시키고 커서의 색을 초록색으로 바꾼다.
import turtle
t=turtle.Turtle()
t.color("green")

#square함수를 정의하여 네모를 그리도록 한다.
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

#drawit함수를 정의하여고 square함수를 이용해 이동해서 네모를 그리도록 한다. 
def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    square(100)
    t.end_fill()

#터틀그래픽에 클릭시 drawit함수가 작동하도록 한다.
s=turtle.Screen()
s.onscreenclick(drawit)
