# 1. 정수를 입력받고
# 양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수
# 판별해주는 프로그램
# ex) -5 => 음의 홀수 , 0=> 0 , 3 => 양의 홀수

# num = int(input("정수 입력:"))
#
# if num > 0:
#     if num % 2 == 1:
#         print("양의 홀수입니다.")
#     else:
#         print("양의 짝수입니다.")
# elif num == 0:
#     print("0입니다.")
# elif num < 0:
#     if num % 2 == 0:
#         print("음의 짝수입니다.")
#     else:
#         print("음의 홀수입니다.")


#
# num = int(input("정수 입력:"))
#
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0
# if isPositive and isOdd:
#     print("양의 홀수입니다.")
# elif isPositive and isEven:
#     print("음의 짝수입니다.")
# elif isNegative and isOdd:
#     print("음의 홀수입니다.")
# elif isNegative and isEven:
#     print("음의 짝수입니다.")


# 좌표 평면에서 위치 판별 프로그램
# 사용자로 부터x축과 y축의 좌표값 x와y를 입력받아, 해당 좌표가 좌표 평면의 어느 사분면에 위치하는지 판별하는 프로그램
# 좌표가 각각의 사분면에 위치하는 경우 '입력하신 좌표는 제 1 사분면에 위치 합니다.' 등과 같이 출력하고
# 좌표가 축 위에 있는 경우는 'X축 위에 위치 합니다.' '원점에 위치합니다.' 등과 같이 구체적으로 알려주는 프로그램

x = int(input("x축의 좌표값:"))
y = int(input("y축의 좌표값:"))

if x > 0 and y < 0:
    print("제 1 사분면에 위치합니다.")
elif x > 0 and y > 0:
    print("제 2 사분면에 위치합니다.")
elif x < 0 and y < 0:
    print("제 3 사분면에 위치합니다.")
elif x == 0 and y == 0:
    print("원점입니다.")
elif y == 0:
    print("x축에 존재합니다.")
elif x == 0:
    print("y축에 존재합니다.")
else:
    print("제 4 분면에 위치합니다.")




# 마트 할인 적용 프로그램
# 사용자로부터 마트에서 구매한 총 금액을 입력받아, 그 금액에 따라 할인율을 적용하는 프로그램
# 구매 금액이 50000원 이상이면 5% 100000원 이상이면 10% 200000원 이상이면 20% 할인을 적용합니다.
# 사용자가 금액에 따라 적용된 할인율과 할인된 금액을 계산하여
# '구매 금액은 [원본 금액]원, 할인율 []% 할인 금액[]원 최종 결제 금액[] 원이 나오는 프로그램


# num = int(input("총 금액:"))
#
# if num >= 50000:
#     print(f"구매 금액은 {num}원,할인율 {5}%, 할인금액 {num * 0.05}원 최종금액 {num - (num * 0.05)}원")
# elif num >= 100000:
#     print(f"구매 금액은 {num}원,할인율 {10}%, 할인금액 {num * 0.1}원 최종금액 {num - (num * 0.1)}원")
# elif num >= 200000:
#     print(f"구매 금액은 {num}원,할인율 {20}%, 할인금액 {num * 0.2}원 최종금액 {num - (num * 0.2)}원")
# else:
#     print(f"구매 금액은 {num}원,할인율 {0}%, 할인금액 {num * 0}원 최종금액 {num - (num * 0)}원")





