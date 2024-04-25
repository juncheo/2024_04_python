# length
# len : 문자열 또는 리스트의 길이를 알려주는 기능
# print(len("hello"))
# print(len([2,4,6,8,10]))
#
# # max, min 최댓값 , 최솟값
# print(max([2,3,4,5,545456,3,2,34]))
# print(min([2,3,4,5,545456,3,2,34]))
#
# # sum 합계
# print(sum([2,3,4,5,545456,3,2,34]))


# QUIZ 1
# 영어 기사 스크랩 해오고, 단어 길이가 6글자 이상인 단어들만 출력하기

# news = """Lawyers for Mr Trump and Special Counsel Jack Smith will square off in a hearing on whether former presidents have immunity from criminal prosecution for actions they take while in office.
#
# Mr Smith charged the former president last year with allegedly attempting to overturn the results of the 2020 election. But Mr Trump said he could not be indicted under the US Constitution. The trial has been on hold while the dispute made its way up to the top court in the country.
#
# The case is already historic - Mr Trump is the first former president to have been charged with federal crimes.
#
# And the Supreme Court decision, which may not come until June, will be historic as well."""
#
# word = news.split()
#
# for x in word:
#     if len(x) >= 6:
#         print(x)



# QUIZ 2

# 문자 길이가 5글자 이하이고 알파벳 a,e 포함되면 대문자로 출력하고
# 그게아니면 그 과일의 문자 길이를 출력하는 프로그램

# fruits = ["apple", "banana","kiwi","mango","strawberry","pineapple","melon"]
#
#
# for x in fruits:
#     if len(x) <= 5 and ("a" in x or "e" in x):
#         print(x.upper())
#     else:
#         print(len(x))







