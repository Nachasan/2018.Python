##사용자로부터 점수를 입력받아 그에 따른 학점으로 turtle을 보낸다.

import turtle #turtle 그래픽 추가
t=turtle.Turtle() #turtle을 변수로 축약
t.shape("turtle") #turtle 그래픽의 모양을 거북이로 변경

t.penup() #turtle의 움직임을 선으로 출력하지 않게 설정

##turtle을 움직이며 위치에 따른 학점을 출력한다.
t.goto(100,100)
t.write("A학점 입니다.")
t.goto(100,50)
t.write("B학점 입니다.")
t.goto(100,0)
t.write("C학점 입니다.")
t.goto(100,-50)
t.write("D학점 입니다.")
t.goto(100,-100)
t.write("F학점 입니다.")
t.goto(0,0)
t.pendown() #turtle의 움직임을 선으로 출력하도록 설정


##turtlr그래픽으로 점수를 입력하게 한다.
score = int(turtle.textinput("", "성적을 입력하시오"))

##입력받은 정수에 따라 turtle의 위치를 옮겨 학점을 나타낸다.
if score >= 90:
    t.goto(100,100)
elif score >= 80:
    t.goto(100,50)
elif score >= 70:
    t.goto(100,0)
elif score >= 60:
    t.goto(100,-50)
else:
    t.goto(100,-100)
