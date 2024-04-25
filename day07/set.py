# data-type : int, str, float, bool, list
# set (집합)
# 중복 허용 안되는 타입

# a = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8}
# print(a)
#
burgerking = {"새우와퍼","치즈와퍼","불고기와퍼","스테이크와퍼"}
momstouch = {"새우와퍼","치즈와퍼","싸이버거","불고기버거"}
# x = burgerking.intersection(momstouch)
# print(x)
#
#
# # 합집합(|)
# union = burgerking | momstouch
#
# # 교집합(&)
# intersection =  burgerking & momstouch
#
# # 차집합(-)
# difference = burgerking - momstouch
#
# print(union)
# print(intersection)
# print(difference)

# 추가
burgerking.add("에그와퍼")

# 삭제
burgerking.remove("새우와퍼") # 구문법 없는 요소 빼면 에러
burgerking.discard("새우와퍼") # 신문법 없는 요소 빼면 에러 발생 안함

# 전체삭제
burgerking.clear()



# set() (중요)
result = set([1,2,3,1,2,3])
print(list(result))

# quiz

news = """Lawyers for Mr Trump and Special Counsel Jack Smith will square off in a hearing on whether former presidents have immunity from criminal prosecution for actions they take while in office.

Mr Smith charged the former president last year with allegedly attempting to overturn the results of the 2020 election. But Mr Trump said he could not be indicted under the US Constitution. The trial has been on hold while the dispute made its way up to the top court in the country.

The case is already historic - Mr Trump is the first former president to have been charged with federal crimes.

And the Supreme Court decision, which may not come until June, will be historic as well."""

word = news.split()
noDuplicationWords = list(set(word))
noDuplicationWords.sort()
print(noDuplicationWords)








