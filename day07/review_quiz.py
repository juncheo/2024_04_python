# 문자열 문자 반복 프로그램
# 주어진 문자열 word의 문자를 정수 n만큼 반복하여 새로운 문자열을 생성하는 프로그램 작성

# 예시 word = "abc" ,n = 3
# 결과 "aaabbbccc"

#
# word = input("단어 입력: ")
# count = int(input("횟수 입력: "))
#
# newWord = ""
# for x in word:
#     newWord += x * count
# print(newWord)

# 모음 대문자화 프로그램
# 사용자로부터 문자열을 입력받아, 그 문자열 내의 모든 모음(aeiuo)만 대문자로 변환하는 프로그램을 작성
# 다른 문자들은 원래의 상태응 유지합니다.

# word = input("단어 입력: ")
#
# newWord = ""
# for x in word:
#     if x in "aeiou":
#         newWord += x.upper()
#     else:
#         newWord += x
# print(newWord)



# 입력 : "cccCCC"
# 출력 : "CCCccc"
# 입력 : "abCdEfghIJ"
# 출력 : "ABcDeFGHij"

# word = input("단어 입력: ")
#
# newWord = ""
# for x in word:
#     if x.isupper():
#         newWord += x.lower()
#     else:
#         newWord += x.upper()
# print(newWord)



# 단어를 입력 했을 때
# 자음은 대문자화 해서 출력

# word = input("단어 입력: ")
#
# newWord = ""
# for x in word:
#     if x not in "aeiou":
#         newWord += x.upper()
#     else:
#         newWord += x
# print(newWord)





