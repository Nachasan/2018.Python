savedID = 'radium96'
savedPassword = 'qwe123'
ID = str(input("아이디를 입력하시오 : "))

if savedID==ID:
    password = str(input("비밀번호를 입력하시오 : "))
    if savedPassword==password:
        print("환영합니다.")
    else:
        print("비밀번호를 확인하시오.")
else:
    print("아이디를 찾을 수 없습니다.")
