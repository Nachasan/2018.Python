score = int(input("점수를 입력하시오. : "))
if score >= 60:
    print("합격입니다.")
    if score >= 90:
        print("장학금도 받을 수 있습니다.")
else:
    print("불합격입니다.")
