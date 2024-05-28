import pandas



df = pandas.read_csv("company.csv",encoding='cp949')

# 기본 열 뽑기
# print(df['name']) # 하나 열
# print(df[['name','age','salary']]) # 다중 열


# 조건으로 열 뽑기
# print(df[df['salary']>= 7000])
# print(df[df['years_at_company'] >= 7])

# a = df['salary'] >= 5000
# b = df['years_at_company'] >= 10
# print(df[a & b])


# 근속연도 10, 만족도 8 , 수행도 80

# a = df['years_at_company'] >= 10
# b = df['job_satisfaction'] >= 8
# c = df['performance'] >= 80
#
# print(df[a & b & c])


# 열 추가

# df['test'] = 50
# print(df)


# df['test'] = df['age'] * df['years_at_company']
# print(df)

# 근속일년수에 따른 직급
# 5년 이하이면 사원
# 10년 이하 과장
# 15년 이하 부장
# def makeRnak(x):
#     if x <= 5:
#         return "사원"
#     elif x <= 10:
#         return "과장"
#     else:
#         return "부장"
# apply함수
# df['rank'] = df['years_at_company'].apply(makeRnak)


# performance_score 20점 - 권고사직 50점 - 직급유지  80점- 보너스 100점 - 승진

def make_performance(x):
    if x <= 20:
        return "권고사직"
    elif x <= 50:
        return "직급유지"
    elif x <= 80:
        return "보너스"
    else:
        return "승진"

df['rate'] = df['performance'].apply(make_performance)



# 데이터프레임 정보 확인
print(df.info())


# 데이터프레임 통계 정보
print(df.describe())


print(df.sort_values(by='age'))

