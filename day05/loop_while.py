# loop_while

# x = 10
# while x > 0:
#     print("집가서 자야지")
#     x -= 1




# while True:
#     x = int(input("숫자 0을 넣어야 멈춤 :"))
#     if x == 0:
#         break


# 1 아이스 아메리카노
# 2 아이스 라떼
# 숫자 0을 넣으면 멈춤


# while True:
#     x = int(input("1아메리 2라떼 0 멈춤:"))
#     if x == 1:
#         print("아메리카노")
#     elif x == 2:
#         print("아이스 라떼")
#     elif x == 0:
#         break




# 1 python
# 2 java
# 3 c++
# 4 프로그램 종료
# 그 외는 숫자를 잘못 입력 하였습니다.


# while True:
#     x = int(input("숫자 입력:"))
#     if x == 1:
#         print("python")
#     elif x == 2:
#         print("java")
#     elif x == 3:
#         print("c++")
#     elif x == 4:
#         print("프로그램 종료!")
#         break
#     else:
#         print("숫자를 잘못 입력하였습니다.")





# 계산기 프로그램
# 유저에게 0. 프로그램 종료 1. 더하기 2. 빼기 3. 곱하기 4. 제곱 5. 나누기(몫)


while True:
    num = int(input("0. 프로그램 종료 1. 더하기 2. 빼기 3. 곱하기 4. 제곱 5. 나누기"))
    x = int(input("숫자 입력:"))
    y = int(input("숫자 입력:"))
    if num == 0:
        print("프로그램 종료")
        break
    elif num == 1:
        print(x + y)
    elif num == 2:
        print(x - y)
    elif num == 3:
        print(x * y)
    elif num == 4:
        print(x ** y)
    elif num == 5:
        print(x / y)
    else:
        print("숫자를 잘못입력하셨습니다.")






