#201802062 김산하
inputMoney = int(input("투입한 돈 : ")) #사용자로부터 투입한 돈을 입력받는다.
price = int(input("물건값 : ")) #사용자로부터 물건값을 입력받는다.
charge = inputMoney - price #투입한 돈, 물건값 -> 거스름돈
print("거스름돈 : ", charge) #거스름돈의 액수를 출력시킨다.
fiveHundred = charge//500 #거스름돈의 500원의 개수를 구한다.(나눗셈의 몫계산 이용)
oneHundred = (charge-fiveHundred*500)//100 #거스름돈의 100원의 개수를 구한다.
print("500원 동전의 개수 : ", fiveHundred) #500원의 개수를 출력한다.
print("100원 동전의 개수 : ", oneHundred) #100원의 개수를 출력한다.

