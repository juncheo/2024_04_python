# 메가커피 당일 매출 기록표
# 이름 메뉴 몇시 결제수단 매장/ 포장

import pandas
import random
import datetime
from faker import Faker
f = Faker('ko_KR')
coffeeName = ["아이스아메리카노","라떼","바닐라라떼","자몽에이드","레몬에이드","마끼야또","오레오쉐이크","블루베리요거트"]
payList = ["카카오페이","토스","카드","삼성페이","네이버페이","현금"]

# def get_random_time():
#     s = datetime.datetime.strftime("07:00","%H:%M")
#     e = datetime.datetime.strftime("22:00","%H:%M")
#     total = int((e-s).total_seconds() / 60) # 전체 몇분
#     random_minutes = random.randint(0,total)
#     return s + datetime.timedelta(minutes=random_minutes)
#
# print(get_random_time().strftime("%H:%M"))

magaCoffee = {
    'person': [f.name() for x in range(1000)],
    'name': [random.choice(coffeeName) for x in range(1000)],
    'Payment': [random.choice(payList) for x in range(1000)],
    'choice': [random.choice(["포장","매장"]) for x in range(1000)]
}

df =  pandas.DataFrame(magaCoffee)
df.to_csv('mega.csv',index=False,encoding='cp949')
