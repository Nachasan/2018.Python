## 터틀그래픽이용하여 사용자로부터 숫자를 받아 도형을 그리는 프로그램

## 터틀그래픽을 실행
import turtle
t=turtle.Turtle()
t.shape('turtle')

## 터틀그래픽에 입력창을 추가해 사용자로부터 숫자를 입력받음
polygon = int(turtle.textinput("","몇각형을 원하시나요?"))

## 입력받은 숫자로 도형을 그림
for i in range(1,polygon+1,1):
    t.forward(100)
    t.left(360/polygon)
    
