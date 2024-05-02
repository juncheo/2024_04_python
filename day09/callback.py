def a(x):
    print("a함수실행")
    x()
def b():
    print("b함수실행")
a(b)



# 게임 몬스터 프로그램

def killingMonster(monster,event):
    print(f"{monster}를 처치 했습니다!")
    event()


def getGold():
    print("골드 획득!")

def getFood():
    print("음식 획득!")

killingMonster("슬라임",getFood())
killingMonster("늑대",getGold())