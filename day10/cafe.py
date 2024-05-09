from coffee import Coffee


coffeList = [Coffee("아메리카노",2000,100), Coffee("라떼",2500,150), Coffee("바닐라라떼", 3000,200)]
while True:
    codeNumber = int(input("1.커피 판매 2. 커피 추가 3.프로그램 종료"))
    if codeNumber == 1:
        for x in coffeList:
            print(x.intro())
        coffeeNumber = int(input("번호입력"))
    elif codeNumber == 2:
        newCoffeeName = input("커피 이름")
        newCoffeePrice = int(input("커피 가격"))
        coffeeList.append(Coffee(newCoffeeName,newCoffeePrice))
        print(f"{newCoffeeName}이 추가 되었습니다.")
    elif codeNumber == 3:
        print("프로그램 종료")
        break
