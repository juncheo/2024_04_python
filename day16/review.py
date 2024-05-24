# 1. 조건에 맞게 수열 변환하기
# 정수 배열 arr와 자연수 k가 주어집니다. 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
# k가 짝수라면 arr의 모든 원소에 k를 더합니다.
# 이러한 변환을 마친 후의 arr를 return하는 solution함수를 완성해 주세요.

# arr [1,2,3,100,99,98],[1,2,3,100,99,98]
# k 3,2
# result  [3,6,9,300,297,294],[3,4,5,102,101,100]


# k = 2
# def solution1(arr,k):
#     return [x * k if k % 2 == 1 else x + k for x in arr]
#
# arr1 = [1,2,3,100,99,98]
# print(solution1(arr1,2))
# print(solution1(arr1,3))


# 2. A강조 하기
# 문자열 mystring 이 주어집니다. mystring 에서 알파벳"a"가 등장하면 전부 "A"로 변환하고,
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return하는 solution1 함수를 완성하세요.
#
# myString = "abstract algebra"
#
# def solution2(myString):
#     return "".join(['A' if x == 'a' else x.lower() for x in myString])
#
# print(solution2("abstract algebra"))
#
#

# 3. 오늘 날짜 [05-24,......06-24]

import datetime


def solution3(x):
    today = datetime.date.today()
    future_time = today + datetime.timedelta(days=x)
    return future_time.strftime("%m-%d")

a = [solution3(x) for x in range(31)]

print(a)

