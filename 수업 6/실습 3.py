while (1):
    evenOrOdd = input("\"홀수\" or \"짝수\"를 입력하시오 : ")
    sum = 0
    
    if evenOrOdd == '짝수' :
        for i in range(2, 101, 2):
            sum += i
        print(sum)
        break

    elif evenOrOdd == '홀수' :
        for i in range(1, 101, 2):
            sum += i
        print(sum)
        break

    else :
        continue
