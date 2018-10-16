##함수를 이용하여 터틀이 네모를 그리도록 하는 프로그램

#터틀 그래픽을 실행시킨다
import turtle
t=turtle.Turtle()
t.shape("turtle")


#spuare함수를 정의한다.
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

#반복문을 통해 square함수가 실행되도록 한다.
for n in range(3):
    square(100)
    t.penup()
    t.forward(200)
    t.pendown()
