# 1. 태어난 년도로 띠 알아보기
# 사용자에게 태어난 년도를 입력 받아 그 해에 해당하는 띠를 알려주는 기능을 구현하려고 합니다.
# 12간지(띠)를 활용하여 태어난 년도를 입력하면 그 해의 띠를 반환하는 함수를 작성하세요



def yeerToZodiac(year):
    zodiac = {
    0: "원숭이",
    1: "닭",
    2: "개",
    3: "돼지",
    4: "소",
    5: "쥐",
    6: "호랑이",
    7: "토끼",
    8: "용",
    9: "뱀",
    10: "말",
    11: "양"
}
    return zodiac[year % 12]
print(yeerToZodiac(1990))








# 2. 숫자 뒤집기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태 돌려주는 solution 함수를 만들어주세요
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# def makeReverseList(x):
#     a = list(str(x))
#     a.reverse()
#     b = list(map(lambda x: int(x),a))
#     return b

# def makeReversedNumber(x):
#     return list(map(lambda x: int(x), reversed(list(str(x)))))
# print(makeReversedNumber(12345))




# 3. 짝수는 싫어요
# 정수n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록
# solution 함수를 완성해주세요.
# def solution(num):
#     return [x for x in range(16) if x % 2 == 1]



# 랜덤을 사용해서 띠함수를 사용하여
# 100개 띠들이 있는 리스트 만들기

#
# import random
#
# # a = [yeerToZodiac(random.randint(1930,2025)) for x in range(100)]
# # print(a)
#
# # random.randint(0,100)
# # random.choice(["콜라","사이다","환타"])
# # random.shuffle() # 랜덤으로 섞기
#
# b = ["콜라","사이다","환타"]
# c = [6,2,1]
# d = random.choices(b, weights=c, k=1000)
# print(d)
