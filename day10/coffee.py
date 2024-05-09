class Coffee:
    def __init__(self, a, b, c):
        self.name = a
        self.price = b
        seif.caffeein = c
    def intro(self):
        return f"{self.name}, {self.price}, {self.caffeein}"

coffeList = [{'name':'아메리카노', 'price': 2000}, {'name':'라떼', 'price': 2500}, {'name':'바닐라라떼', 'price': 3000}]
while True:
    codeNumber = int(input("1.커피 판매 2. 커피 추가 3.프로그램 종료"))
    if codeNumber == 1:
        for index, item in enumerate(coffeeList):
            print(f"{index}, {item['name']}, {item['price']}원int")
        coffeeNumber = int(input("번호입력"))
    elif codeNumber == 2:
        newCoffeeName = input("커피 이름")
        newCoffeePrice = int(input("커피 가격"))
        newCoffeeMenu = {'name': newCoffeeName, 'price': newCoffeePrice}
        coffeeList.append(newCoffeeMenu)
        print(f"{newCoffeeName}이 추가 되었습니다.")
    elif codeNumber == 3:
        print("프로그램 종료")
        break