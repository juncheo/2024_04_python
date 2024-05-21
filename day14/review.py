# # 1.제일 작은 수 제거하기
# # 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# # 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# # 예를들어 arr이[4,3,2,1]인 경우는 [4,3,2]를 리턴하고, [10]면[-1]을 리턴합니다.
#
# # arr [4,3,2,1]  [10]
# # return [4,3,2] [-1]
# a = [1,3,2,4,10]
# a.remove(min(a))
# # del  a[0]
#
# def solution(arr):
#     if len(arr) == 1:
#         return [-1]
#     else:
#         arr.remove(min(arr))
#         return arr
#
#
# # 2. 문자열 섞기
# # 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return하는 solution함수를 완성해주세요.
#
# # str1 "aaaaa"
# # str2 "bbbbb"
# # result "ababababab"
#
#
# def solution1(str1,str2):
#     text = ""
#     for x in range(len(str1)):
#         text += str1[x]
#         text += str2[x]
#     return text
# print(solution1("aaaaa","bbbbb"))




# 3. x 사이의 개수
# 문제: 문자열 myString 이 주어집니다. myString을 문자"x"룰 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로
# 저장한 배열을 return 하는 solution함수를 완성해주세요.

# myString "oxooxoxox"  "xabcxdefxghi"
# result  [1,2,1,1]   [3,3,3]


def solution3(str):
    return list(map(lambda x: len(x),filter(lambda x: len(x)> 0,"oxooxoxxox".split("x"))))




# 4.5명씩
# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담신 문자열 리스트 names가 주어질 때 앞에서 부터
# 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return 하도록 solution함수를 완성 해주세요.
# 마지막 그룹이5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.


arr = ["nami", "ahri","jayce","garen","ivern","vex","jinx"]

def solution4(arr):
    return [item for index,item in enumerate(arr) if index % 5 == 0]


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리 내는 중"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


    def speak(self):
        return f"{super().speak()} ... 멍멍"


a = Dog("흰둥이","하얀개")
print(a.speak())



