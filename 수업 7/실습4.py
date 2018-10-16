#터틀그래픽을 이용하여 터틀을 클릭하는 위치로 옮기도록 하는 프로그램

#터틀그래픽을 실행시킨다.
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.pensize(5) #터틀이 움직일 때 생기는 선의 두께를 정한다.

#함수 move를 정의해 터틀이 움직이도록 한다.
def move (x,y):
    t.goto(x,y)

#터틀그래픽에 클릭시 move함수가 실행되도락 한다.
s = turtle.Screen()
s.onscreenclick(move)
