# control statement
# condition statement[조건문]
# if 조건:
# [들여쓰기] 코드
# elif 조건:
# else:
# pass 는 코드를 넘겨주는 역할


# loop statement[반복문]

# for 문: 개발자가 끝이 언제일지 알 때,
# for x in range(n) -> 0 ~ n-1
# for x in "hello"  -> h,e,l,l,o
# for x in [1,2,3,4,5] -> 1,2,3,4,5
# for x,y in dict.item() -> k,v / k,v / k,v
# for x in set -> a,b,c,d (순서 보장 안됨)(중복 안됨)
coffee = {"name":"아메리카노", "price":3000}
for x,y in coffee.items():
    print(f"{x},{y}")

# coffee.keys() # name , price
# coffee.values() # 아메리카노 3000



# while 문: 개발자가 끝이 언제일지 모를 때,
# while 조건:
#  로직
#  무한루프 막는 방법: break or 조건을 수정







