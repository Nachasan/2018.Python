##함수를 이용하여 터틀그래픽이 회전하며 도형을 그리도록 하는 프로그램

#터틀그래픽을 실행시킨다.
import turtle
t=turtle.Turtle()
t.shape("turtle")

#polygon함수를 정의하여 도형을 그리며 회전하도록 한다.
def polygon(n):
    for i in range(1,n+1,1):
        t.forward(80)
        t.left(360/n)

#사용자로부터 도형의 모양을 입력받는다.
n=int(turtle.textinput("","몇각형인가요?"))

#반복문을 이용하여 도형을 그린다.
for i in range(18):
    polygon(n)
    t.left(360/18)
