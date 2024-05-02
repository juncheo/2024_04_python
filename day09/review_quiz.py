# 이메일 주소 분리 퀴즈
# 사용자로부터 전체 이메일 주소를 입력받습니다. 예를 들어,
# username@example.com 과 같은 형식입니다. 프로그램은 입력받은 이메일 주소에서
# 사용자 이름 부분과 도메인 부분을 분리하여 출력합니다. 사용자 이름과 도메인이 어떻게 구분되는지 확인

# email = input("이메일 입력 : ")
#
# def splitEamil(email):
#     arr = email.split("@")
#     return {"user": arr[0], "domain": arr[1]}
#
# print(splitEamil("itKorea@naver.com"))



# 문자열 변환 마법 퀴즈
# 사용자로부터 문자열을 입력받습니다. 입력된 문자열은 두 가지 마법적 변환을 거치게 됩니다.
# 하나는 무자열을 뒤집어 순서를 바꾸고, 다른 하나는 문자열의 문자들을 알파벳 순서로 정렬합니다.
# 예를 들어, 'mega'를 입력하면 뒤집힌 'agem'과 알파벳 순으로 정렬된 'aemg'가 결과로 나타납니다.


def spellingMagic(word):
    spellingList = list(word)
    spellingList.sort()
    result = "".join(spellingList)

    spellingList1 = list(word)
    spellingList1.reverse()
    result1 = "".join(spellingList1)
    return {"sorted":result , "reverse": result1}
print(spellingMagic("koreait"))





# 정수 n이 주어졌을 때, 홀수면 "odd" 짝수면 "even"을 돌려주는 함수 만들기

def word(n):
    if n % 2 == 1:
        return "odd"
    else:
        return "even"




