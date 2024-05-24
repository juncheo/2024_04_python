# pandas 라이브러리 설치
import pandas


# Series 한줄 역할하는 객체

# arr = [1 for x in range(101)]
# serise = pandas.Series(arr)
# print(serise)


# 엑셀 그 자체

# data = {
#     'movies': ["혹성탈출","범죄도시","설계자","퓨리오사"],
#     'popcorn': ["오리지널 팝콘","어니언 팝콘","카라멜 팝콘","치즈 팝콘"],
#     'beverage': ["콜라","제로콜라","사이다","제로사이다"],
# }
#
# df = pandas.DataFrame(data)
# print(df)



# 학생이름 학년 전공 평균학점
import random
import math
from faker import Faker



f = Faker('ko_KR')

majorList = ["수학","과학","사회","국어","영어","도덕","중국어","일본어","체육","무용"]
round(random.uniform(1,4.5),2)
# def makeName():
#     return random.choice(list("abcdefghijklmnopqrstuvwxyz")) + random.choice(list("abcdefghijklmnopqrstuvwxyz")) + random.choice(list("abcdefghijklmnopqrstuvwxyz"))

data1 = {
    'student': [f.name() for x in range(1000)],
    'school_year': [random.randint(1,5) for x in range(1000)],
    'major': [random.choice(majorList) for x in range(1000)],
    'sum': [round(random.uniform(1,4.5),2) for x in range(1000)]
}

df = pandas.DataFrame(data1)
print(df)

# 아무거나 만들어주는 라이브러리 faker

df.to_csv('university.csv',index=False, encoding='cp949')







