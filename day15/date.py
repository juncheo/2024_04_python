import datetime

a = datetime.datetime.now()
print(a)


b = datetime.datetime.now().strftime("%Y-%m-%d")
c = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(b)
print(c)

d = datetime.date.today()
print(d)

# 두 날짜나 시간 사이의 기간표기법
today = datetime.date.today()
next_week = today + datetime.timedelta(days=7) # 7일의 기간
print(next_week.strftime("%Y-%m-%d"))





