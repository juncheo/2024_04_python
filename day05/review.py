# variable, input/print, dataType, operator
# 조건문[if-elif-else]
# 반복문 for x in range(n)

# 1.정수 평균 계산 프로그램

# num1 = int(input("정수 입력:"))
# num2 = int(input("정수 입력:"))
# num3 = int(input("정수 입력:"))
#
# print(f"평균 : {(num1 + num2 + num3) / 3}")

# 2.가장 큰 정수 찾기 프로그램
# 사용자로부터 3개의 정수{숫자모두다름}를 입력받아, 가장 큰 정수를 찾아 출력 하세요


# a = int(input("정수 입력:"))
# b = int(input("정수 입력:"))
# c = int(input("정수 입력:"))
#
# if a > c and a > b:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)


# 3. 입력한 정수의 배수 출력 프로그램
# 사용자로부터 정수를 입력받아, 해당 정수의 배수를 100까지 출력

num =int(input("정수 입력:"))

for x in range(101):
    if x % num == 0:
        print(x)
