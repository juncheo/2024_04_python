# comprehension
# [0~100]리스트 출력


# newList = []
# for x in range(101):
#     newList.append(x)
# print(newList)


a = [x for x in range(101)]
print(a)

# "apple" => [a,p,p,l,e]

b = [x for x in "apple"]
print(b)

c= [x for x in range(11)]
print(c)

c= [x for x in range(11) if x % 2 == 0]
print(c)

# 0~100 홀수만 리스트

d = [x for x in range(101) if x % 2 == 1]
print(d)



# 0~100 짝수를 제곱인 형태인 리스트

e = [x ** 2 for x in range(101) if x % 2 == 0]
print(e)


# 0~10 홀수에서 10을 더한 리스트

f = [x + 10 for x in range(11) if x % 2 == 1]
print(f)


fruits = ["apple", "banana", "kiwi", "grape", "orange"]

g = [len(x) for x in fruits]
print(g)

fruits = ["apple", "banana", "kiwi", "grape", "orange"]

h = [len(x) for x in fruits if "i" in x]
print(h)



# 매핑 컴프리헨션
#홀수 10 짝수 20
i = [x + 10 if x % 2 == 1 else x + 20 for x in range(101)]
print(i)




fruits = ["apple", "banana", "kiwi", "grape", "orange"]

# 5글자 이하이면, 글자의 길이로 나타내고, 아니면 대문자화 하기

j = [len(x) if len(x) <= 5 else x.upper() for x in fruits]
print(j)

