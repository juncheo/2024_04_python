# 1. 문자열 잘라서 정렬하기
# 문자열 mystring 이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한
# 배열을 return 하는 solution 함수를 완성해주세요


# myString =  "dxccxbbbxaaaa"
# result = ["a","b","c","d"]
# a = list(filter(lambda x: x != "", "axbxcxdx".split("x")))
# b = list(filter(lambda x: x!="","dxccxbbbxaaaa".split("x")))
# a.sort()
# b.sort()
def solution(myString):
    filterdList = list(filter(lambda x: x != "",myString("x")))
    filterdList.sort()
    return  filterdList


# 배열 원소 삭제하기
# 정수배열arr과 delete_list 가 있습니다. arr 의 원소 중 delete_list의 원소를 모두 삭제하고
# 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작겅해주세요

arr = [293, 1000,395,678,94]
delete_list = [94,777,104,1000,1,12]
# result = [293,395,678]
#
# list(filter(lambda x: x not in delete_list,arr))


def solution2(arr,delete_list):
    return list(filter(lambda x: x not in delete_list,arr))



# 최댓값 만들기
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을
# return 하도록 solution 함수를 완성해주세요


a = [1,2,-3,4,-5]
b = [0,-31,24,10,10,9]
c = [10,20,30,5,5,20,-5]
a.sort()
b.sort()
c.sort()

def solution3(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]
        return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]







