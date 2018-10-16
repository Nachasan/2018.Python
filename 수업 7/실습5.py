##터틀그래픽을 이용하여 나무를 그리는 프랙탈을 실행시키는 프로그램

#터틀그래픽을 실행시킨다
import turtle
t=turtle.Turtle()
t.color("green") #터틀의 색을 초록색으로 바꾼다
t.left(90) #터틀이 위로 움직이도록 돌려준다.

#fractal함수를 정의하여 나무를 그리도록 한다.
def fractal(length):    
    if length>5: #터틀이 어느순간 멈추도록 조건문을 걸어준다.
        t.forward(length)
        t.right(25)
        fractal(length-15) #recursion을 이용
        t.left(50)
        fractal(length-15) #recursion을 이용
        t.right(25)
        t.back(length)

t.speed(1000) #터틀이 움직이는 속도를 올려준다.
fractal(90) #fractal함수를 실행시킨다.

