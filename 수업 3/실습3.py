weight = float(input("몸무게를 kg단위로 입력하시오 : ")) #사용자로부터 몸무게를 입력받는다.
height = float(input("키를 m단위로 입력하시오 : ")) #사용자로부터 키를 입력받는다.
BMI = weight/height**2 #키, 몸무게 -> BMI
print("당신의 BMI =", BMI) #계산한 BMI를 출력한다.
