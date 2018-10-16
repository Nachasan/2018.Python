n = int(input("정수를 입력하시오 : "))
factoria = 1
for i in range(1,n+1,1):
    factoria *= i
print("%s!은" % n,factoria, "이다.")
