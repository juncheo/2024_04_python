# map(how, target) : 어떠한 것을 바꿔주기(targer을 바꿔줌)
#
# numList = [x for x in range(101)]
# result = list(map(lambda x:x+100,numList))
# print(result)
#
#
# # filter: target을 필터링해줌
#
# result1 = list(filter(lambda x:x%2==0,numList))
# print(result1)
#
#
#
# fruits = ["apple", "banana","cherry","kiwi"]
#
# filter(lambda x: len(x)<= 5,fruits)
# filter(lambda x: 'a' in x,fruits)

emailList = ["abc@naver.com", "mega@gmail.com","korea@daum.net"]

result2 = list(map(lambda x:x.split("@")[0],emailList))
print(result2)




