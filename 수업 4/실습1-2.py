import turtle #터틀그래픽을 실행시킨다.
t=turtle.Turtle() #t를 선언하여 원할한 코딩을 이룬다.
t.shape("turtle") #움직이는 물체의 모양을 거북이로 바꾼다.

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

s = turtle.textinput("","이름을 입력하시오 : ")
t.write("안녕하세요? "+s+"씨, 터틀 인사드립니다.")
