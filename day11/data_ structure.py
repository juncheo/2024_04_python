# 기본자료 구조: 데이터를 어떻게 보관하고 다루는지에 대한 방법들
# list: 순서 있고, 중복 가능
# set: 순서 없고, 중복 안됨
# dict: k[중복 안됨]- v[중복 가능] 형태로 저장
# tuple: (사과,바나나,키위) 수정 불가능


# 심화 자료 구조:
# graph : 그래프 자료구조[지도, 미니맵, 경로 최적화]
# tree : 트리 자료구조[단어 검색]








# names = ['아메리카노','라떼','바닐라']
# prices = [2000, 2500, 3000]
# menu = []
# for index, item in enumerate(names):
#     menu.append({'name': item, 'price': prices[index]})
# print(menu)



# names = ['아메리카노','라떼','바닐라']
# prices = [2000, 2500, 3000]
# x = dict(zip(names, prices))
# print(x)


# 과일 이름 리스트:
# 과일 가격 리스트:
#zip으로ㅓ 묶어서 k-v형태 나타내기

# fruits = ['apple','banana','cherry']
# fruitsPrice =[700,500,800]
# fruitsMenu = dict(zip(fruits,fruitsPrice))
# print(fruitsMenu)



# fruits = ['apple','banana','cherry']
# fruitsPrice =[700,500,800]
#
# for index, item in enumerate(zip(fruits, fruitsPrice)):
#     print(f"{index},{item}")

# fruits = ['apple','banana','cherry']
# fruitsPrice =[700,500,800]
#
# for index,(x,y) in enumerate(zip(fruits,fruitsPrice)):
#     print(f"{index+1}. {x},{y}")

# fruits = ['apple','banana','cherry']
# fruitsPrice =[700,500,800]
#
# menu = [{'name': x, 'price': y} for (x,y) in zip(fruits,fruitsPrice)]
# print(menu)



















# names = ['아메리카노', '라떼','바닐라라떼']
# prices = [2000,3000,5000]
#
# coffeeMenu = [{'names':x, 'prices':y} for (x,y) in zip(names,prices)]
# print(coffeeMenu)
#
#
# for index,(x,y) in enumerate(zip(names,prices)):
#     print(f"{index+1},{x} {y}")











#
# text = "apple banana apple strawberry banana"
#
# # [{"단어":"apple","글자수":5},...]
#
# a = [{"단어":x,"글자수":len(x)} for x in text.split(" ")]
# print(a)


















